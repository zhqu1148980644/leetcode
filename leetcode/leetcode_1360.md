---
title:  Number of Days Between Two Dates
date: 2021-01-04
---
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

```
Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
```

 

#### Constraints:

-    The given dates are valid dates between the years 1971 and 2100.



#### Solutions


1. ##### staight forward

```cpp

int numleaps(int y) {
    return y / 4 - y / 100 + y / 400;
}

int getday(int y, int m, int d) {
    const int month[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int day = (y - 1) * 365;
    day += m <= 2 ? numleaps(y - 1) : numleaps(y);
    for (int i = 0; i < m - 1; i++)
        day += month[i];
    day += d;
    return day;
}

int daysBetweenDates(char * date1, char * date2){
    int y, m, n;
    sscanf(date1, "%d-%d-%d", &y, &m, &n);
    int day1 = getday(y, m, n);
    sscanf(date2, "%d-%d-%d", &y, &m, &n);
    int day2 = getday(y, m, n);

    return abs(day1 - day2);
}


```

- or python version

```python
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import datetime
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d1 - d2).days)
```