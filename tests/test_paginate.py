import re

import lxml.html

try:
    from django.template.loader import get_template_from_string
except ImportError:
    from django.template import Engine

    get_template_from_string = Engine.get_default().from_string

from django.template import Context
import django.http
from django.core.paginator import Paginator


class TestPaginateTestCase:
    def test_example(self):
        template = get_template_from_string(
            """
            {% load bootstrap_pagination %}
            {% bootstrap_paginate page_obj range=10 %}
        """,
        )

        objects = ["obj%02x" % idx for idx in range(30)]

        paginator = Paginator(objects, 10)

        c = Context(
            {"page_obj": paginator.page(2), "request": django.http.HttpRequest()},
        )
        html = lxml.html.fragment_fromstring(template.render(c))
        assert html.get("class").strip() == "pagination"
        assert html.cssselect('[title="Current Page"]')[0].text.strip() == "2"

    def test_html_output(self):
        template = get_template_from_string(
            """
            {% load bootstrap_pagination %}
            {% bootstrap_paginate page_obj range=10 %}
        """,
        )

        objects = ["obj%02x" % idx for idx in range(30)]

        paginator = Paginator(objects, 10)

        c = Context(
            {"page_obj": paginator.page(2), "request": django.http.HttpRequest()},
        )
        html_string = template.render(c)
        html_lines = re.split(r"\s*\n[\n\s]*", html_string)
        assert html_lines == [
            "",
            '<ul class="pagination ">',
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Previous Page"',
            'title="Previous Page"',
            'href="?page=1"><span aria-hidden="true">&larr;</span></a>',
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 1 of 3"',
            'title="Page 1 of 3"',
            'href="?page=1">',
            "1",
            "</a>",
            "</li>",
            '<li class="page-item active">',
            '<span class="page-link"',
            'aria-label="Current Page"',
            'title="Current Page">',
            "2",
            "</span>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 3 of 3"',
            'title="Page 3 of 3"',
            'href="?page=3">',
            "3",
            "</a>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Next Page"',
            'title="Next Page"',
            'href="?page=3"><span aria-hidden="true">&rarr;</span></a>',
            "</li>",
            "</ul>",
            "",
        ]

    def test_long_html_output(self):
        template = get_template_from_string(
            """
            {% load bootstrap_pagination %}
            {% bootstrap_paginate page_obj range=10 %}
        """,
        )

        objects = ["obj%02x" % idx for idx in range(300)]

        paginator = Paginator(objects, 10)

        c = Context(
            {"page_obj": paginator.page(2), "request": django.http.HttpRequest()},
        )
        html_string = template.render(c)
        html_lines = re.split(r"\s*\n[\n\s]*", html_string)
        assert html_lines == [
            "",
            '<ul class="pagination ">',
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Previous Page"',
            'title="Previous Page"',
            'href="?page=1"><span aria-hidden="true">&larr;</span></a>',
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 1 of 30"',
            'title="Page 1 of 30"',
            'href="?page=1">',
            "1",
            "</a>",
            "</li>",
            '<li class="page-item active">',
            '<span class="page-link"',
            'aria-label="Current Page"',
            'title="Current Page">',
            "2",
            "</span>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 3 of 30"',
            'title="Page 3 of 30"',
            'href="?page=3">',
            "3",
            "</a>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 4 of 30"',
            'title="Page 4 of 30"',
            'href="?page=4">',
            "4",
            "</a>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 5 of 30"',
            'title="Page 5 of 30"',
            'href="?page=5">',
            "5",
            "</a>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 6 of 30"',
            'title="Page 6 of 30"',
            'href="?page=6">',
            "6",
            "</a>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 7 of 30"',
            'title="Page 7 of 30"',
            'href="?page=7">',
            "7",
            "</a>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 8 of 30"',
            'title="Page 8 of 30"',
            'href="?page=8">',
            "8",
            "</a>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 9 of 30"',
            'title="Page 9 of 30"',
            'href="?page=9">',
            "9",
            "</a>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Page 10 of 30"',
            'title="Page 10 of 30"',
            'href="?page=10">',
            "10",
            "</a>",
            "</li>",
            '<li class="page-item">',
            '<a class="page-link"',
            'aria-label="Next Page"',
            'title="Next Page"',
            'href="?page=3"><span aria-hidden="true">&rarr;</span></a>',
            "</li>",
            "</ul>",
            "",
        ]
