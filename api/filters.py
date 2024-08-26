import re
import time
from django_filters import rest_framework as filters
from .models import Movies
from datetime import datetime
from rest_framework.exceptions import ValidationError


def validate_date(date_str):
    date_regex = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/([0-9]{4})$"
    if not re.match(date_regex, date_str):
        raise ValidationError(
            f"Date {date_str} is not in the correct format MM/DD/YYYY."
        )


class MoviesFilter(filters.FilterSet):
    min_length = filters.NumberFilter(field_name="seconds", lookup_expr="gte")
    max_length = filters.NumberFilter(field_name="seconds", lookup_expr="lte")
    start_date = filters.CharFilter(
        method="filter_start_date", label="Start Date is greater than or equal to:"
    )
    end_date = filters.CharFilter(
        method="filter_end_date", label="End Date is less than or equal to:"
    )

    class Meta:
        model = Movies
        fields = ["min_length", "max_length", "start_date", "end_date"]

    def filter_start_date(self, queryset, name, value):
        validate_date(value)
        start_date = datetime.strptime(value, "%m/%d/%Y")
        start_timestamp = int(time.mktime(start_date.timetuple()))
        return queryset.filter(time_stamp__gte=start_timestamp)

    def filter_end_date(self, queryset, name, value):
        validate_date(value)
        end_date = datetime.strptime(value, "%m/%d/%Y")
        end_timestamp = int(time.mktime(end_date.timetuple()))
        return queryset.filter(time_stamp__lte=end_timestamp)
