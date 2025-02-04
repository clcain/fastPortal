#!/usr/bin/env python

import csv
import math
import os
import sys

import yaml

DEFAULT_TEMPLATE = 'templates/portal.html'


def get_html_template(template_file_path=DEFAULT_TEMPLATE):
    with open(template_file_path, 'r') as f:
        return f.read()


class Portal:

    @classmethod
    def load(cls, yaml_file_path):
        print(f'Loading portal: {yaml_file_path}')
        with open(yaml_file_path, 'r') as f:
            data = yaml.safe_load(f)

        return cls(
            portal_title=data.get('portal', ''),
            portal_header_tag=data.get('header_tag', ''),
            services_groups=data.get('groups', ''),
        )

    def __init__(self,
                 portal_title,
                 portal_header_tag,
                 services_groups,
                 ):
        self.portal_title = portal_title
        self.portal_header_tag = portal_header_tag
        self.services_groups = services_groups

    def render_template(self, template, html_file_path):
        print(f'Writing rendered page: {html_file_path}')
        with open(html_file_path, 'w') as f:
            f.write(template.format(
                title=self.portal_title,
                header_tag=self.portal_header_tag,
                services=Portal._generate_services_html(self.services_groups),
            ))

    @staticmethod
    def _split_services_groups(services_groups):
        total_services_count = 0
        total_services_count_by_group_i = {}
        for i in range(0, len(services_groups)):
            total_services_count += len(services_groups[i].get('services', []))
            total_services_count_by_group_i[i] = total_services_count

        services_group_midpoint_i = 0

        for group_i, aggregate_services_count in total_services_count_by_group_i.items():
            if aggregate_services_count * 2 >= total_services_count:
                services_group_midpoint_i = group_i + 1
                break

        services_column_1 = services_groups[0:services_group_midpoint_i]
        services_column_2 = services_groups[services_group_midpoint_i:]

        return services_column_1, services_column_2

    @ staticmethod
    def _generate_services_html(services_groups):
        services_groups_column_1, services_groups_column_2 = Portal._split_services_groups(services_groups)

        html = []
        for services_column in [services_groups_column_1, services_groups_column_2]:
            if len(services_column) > 0:
                html.append('<div class="services-column">')
                for services_group in services_column:
                    html.append(Portal._generate_services_group_html(services_group))
                html.append('</div>')
        return '\n'.join(html)

    @ staticmethod
    def _generate_services_group_html(services_group):
        html = []
        html.append('<div class="services-group">')
        html.append('<div class="services-group-label">')
        html.append(services_group.get('label', ''))
        html.append('</div>')
        for service in services_group.get('services', ''):
            html.append(Portal._generate_service_html(service))
        html.append('</div>')
        return '\n'.join(html)

    @ staticmethod
    def _generate_service_html(service):
        service_url = service.get('url', '')
        service_icon = service.get('icon', '')
        service_title = service.get('title', '')
        service_description = service.get('description', '')

        if not os.path.exists(f'./static/{service_icon}'):
            service_icon = 'img/web.png'

        html = []
        html.append(f'<a class="service" href="{service_url}" target="_blank" rel="noopener noreferrer">')
        html.append(f'<img class="service-img" src="{service_icon}">')
        html.append(f'<div class="service-text">')
        html.append(f'<h1 class="service-title">{service_title}</h1>')
        html.append(f'<h2 class="service-description">{service_description}</h2>')
        html.append('</div>')
        html.append('</a>')
        return '\n'.join(html)


def main():
    if len(sys.argv) < 2:
        print('Usage: ./fastPortal.py SITE_YAML SITE_HTML')
        sys.exit(1)

    site_yaml_file_path = sys.argv[1]
    site_html_file_path = sys.argv[2]

    template = get_html_template()

    portal = Portal.load(site_yaml_file_path)
    portal.render_template(template, site_html_file_path)


if __name__ == "__main__":
    main()
