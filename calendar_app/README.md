# calendar_app

calendar_app

## jpholiday

```console
$ pipenv install jpholiday
```

```python
# import
import jpholiday
import datetime

# 元旦
jpholiday.is_holiday_name(datetime.date(2017, 1, 1))

# 振替休日も出力できる
jpholiday.is_holiday_name(datetime.date(2017, 1, 2))


# 何もない日はNoneが帰ってくる
jpholiday.is_holiday_name(datetime.date(2017, 1, 5))
```

# Links

- [Lalcs/jpholiday](https://github.com/Lalcs/jpholiday)
