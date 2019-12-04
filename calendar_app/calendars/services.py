import jpholiday
import datetime

from datetime import timedelta

from django.utils import timezone
from django.utils.timezone import localtime


class ViewHolidayCalendar:

    def __init__(self):
        self.jp_timezone_now = localtime(timezone.now())
        self.range_days = 30

        self.days_list = []

    def execute(self):
        for day in range(self.range_days):
            # add one day
            t_datetime = self.jp_timezone_now + timedelta(days=(day + 1))

            # convert datetime to date
            t_date = datetime.date(
                t_datetime.year, t_datetime.month, t_datetime.day
            )

            holiday = self.is_holiday(t_date)
            t_data_dict = {
                'date': str(t_date),
                'holiday': holiday[0],
                'holiday_name': holiday[1],
                'weekday': self.get_weekday(t_date)
            }
            self.days_list.append(t_data_dict)

    def is_holiday(self, t_date):
        holiday_name = jpholiday.is_holiday_name(t_date)

        if t_date.weekday() in [5, 6]:
            return True, holiday_name
        return jpholiday.is_holiday(t_date), holiday_name

    def get_weekday(self, t_date):
        jp_weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        return jp_weekday[t_date.weekday()]

    @property
    def get_days_list(self):
        return self.days_list
