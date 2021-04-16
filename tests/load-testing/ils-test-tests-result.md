# Load testing of RERO ILS

## Without delay between requests (benchmark)

### 1 concurrent user
```json=
{
    "transactions": 2189,
    "availability": 100.00,
    "elapsed_time": 119.02,
    "data_transferred": 115.32,
    "response_time": 0.05,
    "transaction_rate": 18.39,
    "throughput": 0.97,
    "concurrency": 1.00,
    "successful_transactions": 2161,
    "failed_transactions": 0,
    "longest_transaction": 0.85,
    "shortest_transaction": 0.00
}
```

### 5 concurrent users
```json=
{
    "transactions": 9227,
    "availability": 100.00,
    "elapsed_time": 119.74,
    "data_transferred": 491.35,
    "response_time": 0.06,
    "transaction_rate": 77.06,
    "throughput": 4.10,
    "concurrency": 4.99,
    "successful_transactions": 9139,
    "failed_transactions": 0,
    "longest_transaction": 1.64,
    "shortest_transaction": 0.00
}
```

### 10 concurrent users
```json=
{
    "transactions": 13972,
    "availability": 100.00,
    "elapsed_time": 119.35,
    "data_transferred": 710.76,
    "response_time": 0.09,
    "transaction_rate": 117.07,
    "throughput": 5.96,
    "concurrency": 9.97,
    "successful_transactions": 13856,
    "failed_transactions": 0,
    "longest_transaction": 2.67,
    "shortest_transaction": 0.00
}
```

### 25 concurrent users
```json=
{
    "transactions": 16796,
    "availability": 100.00,
    "elapsed_time": 119.01,
    "data_transferred": 869.51,
    "response_time": 0.18,
    "transaction_rate": 141.13,
    "throughput": 7.31,
    "concurrency": 24.95,
    "successful_transactions": 16643,
    "failed_transactions": 0,
    "longest_transaction": 3.69,
    "shortest_transaction": 0.00
}
```

### 50 concurrent users
```json=
{
    "transactions": 18760,
    "availability": 100.00,
    "elapsed_time": 119.76,
    "data_transferred": 980.60,
    "response_time": 0.32,
    "transaction_rate": 156.65,
    "throughput": 8.19,
    "concurrency": 49.87,
    "successful_transactions": 18585,
    "failed_transactions": 0,
    "longest_transaction": 3.13,
    "shortest_transaction": 0.00
}
```

### 75 concurrent users
```json=
{
    "transactions": 18696,
    "availability": 100.00,
    "elapsed_time": 119.38,
    "data_transferred": 990.05,
    "response_time": 0.48,
    "transaction_rate": 156.61,
    "throughput": 8.29,
    "concurrency": 74.70,
    "successful_transactions": 18530,
    "failed_transactions": 0,
    "longest_transaction": 4.62,
    "shortest_transaction": 0.00
}
```

### 100 concurrent users
```json=
{
    "transactions": 18483,
    "availability": 100.00,
    "elapsed_time": 119.81,
    "data_transferred": 968.96,
    "response_time": 0.65,
    "transaction_rate": 154.27,
    "throughput": 8.09,
    "concurrency": 99.67,
    "successful_transactions": 18328,
    "failed_transactions": 0,
    "longest_transaction": 4.59,
    "shortest_transaction": 0.00
}
```

### 150 concurrent users
```json=
{
    "transactions": 18942,
    "availability": 100.00,
    "elapsed_time": 119.38,
    "data_transferred": 1005.79,
    "response_time": 0.94,
    "transaction_rate": 158.67,
    "throughput": 8.43,
    "concurrency": 149.28,
    "successful_transactions": 18787,
    "failed_transactions": 0,
    "longest_transaction": 4.83,
    "shortest_transaction": 0.00
}
```

### 200 concurrent users
```json=
{
    "transactions": 19708,
    "availability": 100.00,
    "elapsed_time": 119.91,
    "data_transferred": 1036.24,
    "response_time": 1.21,
    "transaction_rate": 164.36,
    "throughput": 8.64,
    "concurrency": 198.68,
    "successful_transactions": 19543,
    "failed_transactions": 0,
    "longest_transaction": 7.98,
    "shortest_transaction": 0.00
}
```

### 250 concurrent users
```json=
{
    "transactions": 18041,
    "availability": 100.00,
    "elapsed_time": 119.76,
    "data_transferred": 870.75,
    "response_time": 1.65,
    "transaction_rate": 150.64,
    "throughput": 7.27,
    "concurrency": 247.96,
    "successful_transactions": 17896,
    "failed_transactions": 0,
    "longest_transaction": 7.86,
    "shortest_transaction": 0.00
}
```

## With a random delay between 1 and 10 seconds

### 1 concurrent user
```json=
{
    "transactions": 128,
    "availability": 100.00,
    "elapsed_time": 119.07,
    "data_transferred": 6.75,
    "response_time": 0.05,
    "transaction_rate": 1.07,
    "throughput": 0.06,
    "concurrency": 0.06,
    "successful_transactions": 127,
    "failed_transactions": 0,
    "longest_transaction": 0.46,
    "shortest_transaction": 0.00
}
```

### 5 concurrent users
```json=
{
    "transactions": 817,
    "availability": 100.00,
    "elapsed_time": 119.71,
    "data_transferred": 44.03,
    "response_time": 0.05,
    "transaction_rate": 6.82,
    "throughput": 0.37,
    "concurrency": 0.37,
    "successful_transactions": 808,
    "failed_transactions": 0,
    "longest_transaction": 1.72,
    "shortest_transaction": 0.00
}
```

### 10 concurrent users
```json=
{
    "transactions": 1277,
    "availability": 100.00,
    "elapsed_time": 119.06,
    "data_transferred": 67.49,
    "response_time": 0.06,
    "transaction_rate": 10.73,
    "throughput": 0.57,
    "concurrency": 0.62,
    "successful_transactions": 1267,
    "failed_transactions": 0,
    "longest_transaction": 0.78,
    "shortest_transaction": 0.00
}
```

### 25 concurrent users
```json=
{
    "transactions": 3533,
    "availability": 100.00,
    "elapsed_time": 119.09,
    "data_transferred": 184.10,
    "response_time": 0.06,
    "transaction_rate": 29.67,
    "throughput": 1.55,
    "concurrency": 1.80,
    "successful_transactions": 3503,
    "failed_transactions": 0,
    "longest_transaction": 2.25,
    "shortest_transaction": 0.00
}
```

### 50 concurrent users
```json=
{
    "transactions": 6576,
    "availability": 100.00,
    "elapsed_time": 119.88,
    "data_transferred": 340.07,
    "response_time": 0.08,
    "transaction_rate": 54.85,
    "throughput": 2.84,
    "concurrency": 4.16,
    "successful_transactions": 6509,
    "failed_transactions": 0,
    "longest_transaction": 2.05,
    "shortest_transaction": 0.00
}
```

### 75 concurrent users
```json=
{
    "transactions": 9499,
    "availability": 100.00,
    "elapsed_time": 119.42,
    "data_transferred": 488.65,
    "response_time": 0.09,
    "transaction_rate": 79.54,
    "throughput": 4.09,
    "concurrency": 6.94,
    "successful_transactions": 9408,
    "failed_transactions": 0,
    "longest_transaction": 2.93,
    "shortest_transaction": 0.00
}
```

### 100 concurrent users
```json=
{
    "transactions": 13192,
    "availability": 100.00,
    "elapsed_time": 119.81,
    "data_transferred": 681.91,
    "response_time": 0.11,
    "transaction_rate": 110.11,
    "throughput": 5.69,
    "concurrency": 11.61,
    "successful_transactions": 13094,
    "failed_transactions": 0,
    "longest_transaction": 3.74,
    "shortest_transaction": 0.00
}
```

### 150 concurrent users
```json=
{
    "transactions": 16572,
    "availability": 100.00,
    "elapsed_time": 119.32,
    "data_transferred": 853.90,
    "response_time": 0.24,
    "transaction_rate": 138.89,
    "throughput": 7.16,
    "concurrency": 33.99,
    "successful_transactions": 16431,
    "failed_transactions": 0,
    "longest_transaction": 5.92,
    "shortest_transaction": 0.00
}
```

### 200 concurrent users
```json=
{
    "transactions": 18937,
    "availability": 100.00,
    "elapsed_time": 119.19,
    "data_transferred": 984.45,
    "response_time": 0.43,
    "transaction_rate": 158.88,
    "throughput": 8.26,
    "concurrency": 69.07,
    "successful_transactions": 18761,
    "failed_transactions": 0,
    "longest_transaction": 5.01,
    "shortest_transaction": 0.00
}
```

### 250 concurrent users
```json=
{
    "transactions": 18837,
    "availability": 100.00,
    "elapsed_time": 119.77,
    "data_transferred": 975.82,
    "response_time": 0.75,
    "transaction_rate": 157.28,
    "throughput": 8.15,
    "concurrency": 118.02,
    "successful_transactions": 18665,
    "failed_transactions": 0,
    "longest_transaction": 7.08,
    "shortest_transaction": 0.00
}
```

## List of executed commands
```shell=
siege --benchmark --time=120S --concurrent=1 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="B-1" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --benchmark --time=120S --concurrent=5 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="B-5" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --benchmark --time=120S --concurrent=10 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="B-10" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --benchmark --time=120S --concurrent=25 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="B-25" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --benchmark --time=120S --concurrent=50 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="B-50" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --benchmark --time=120S --concurrent=75 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="B-75" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --benchmark --time=120S --concurrent=100 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="B-100" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --benchmark --time=120S --concurrent=150 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="B-150" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --benchmark --time=120S --concurrent=200 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="B-200" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --benchmark --time=120S --concurrent=250 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="B-250" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --delay=10 --time=120S --concurrent=1 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="D-1" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --delay=10 --time=120S --concurrent=5 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="D-5" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --delay=10 --time=120S --concurrent=10 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="D-10" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --delay=10 --time=120S --concurrent=25 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="D-25" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --delay=10 --time=120S --concurrent=50 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="D-50" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --delay=10 --time=120S --concurrent=75 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="D-75" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --delay=10 --time=120S --concurrent=100 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="D-100" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --delay=10 --time=120S --concurrent=150 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="D-150" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --delay=10 --time=120S --concurrent=200 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="D-200" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
siege --delay=10 --time=120S --concurrent=250 --internet --log="/Users/sebastiendeleze/Desktop/siege.log" --file="/Users/sebastiendeleze/Desktop/urls" --mark="D-250" --header "Authorization: Bearer QPr7oUsjUsG6c5uCCPWOq6vA7a1OzejAU1dwyLuhGqC0hDfX8SACJPswZLW1"
```

## List of links

```
https://ils.test.rero.ch/
https://ils.test.rero.ch/signin/?next=%2F%3F
https://ils.test.rero.ch/signup/
https://ils.test.rero.ch/help/public/
https://ils.test.rero.ch/lost-password/
https://ils.test.rero.ch/global/search/documents?q=&page=1&size=10
https://ils.test.rero.ch/global/search/documents?q=&page=2&size=10
https://ils.test.rero.ch/global/search/documents?q=&page=3&size=10
https://ils.test.rero.ch/global/search/documents?q=&page=4&size=10
https://ils.test.rero.ch/global/search/documents?q=&page=5&size=10
https://ils.test.rero.ch/global/search/documents?q=&page=6&size=10
https://ils.test.rero.ch/global/search/documents?q=&page=7&size=10
https://ils.test.rero.ch/global/search/documents?q=&page=8&size=10
https://ils.test.rero.ch/global/search/documents?q=&page=9&size=10
https://ils.test.rero.ch/global/search/documents?q=&page=10&size=10
https://ils.test.rero.ch/global/documents/2011010
https://ils.test.rero.ch/global/documents/2011009
https://ils.test.rero.ch/global/documents/2011008
https://ils.test.rero.ch/global/documents/2011007
https://ils.test.rero.ch/global/documents/2011006
https://ils.test.rero.ch/global/documents/2000556
https://ils.test.rero.ch/global/documents/2000532
https://ils.test.rero.ch/global/documents/2000537
https://ils.test.rero.ch/global/documents/2000504
https://ils.test.rero.ch/global/documents/2000533
https://ils.test.rero.ch/global/search/persons?q=&page=1&size=10
https://ils.test.rero.ch/global/search/persons?q=&page=2&size=10
https://ils.test.rero.ch/global/search/persons?q=&page=3&size=10
https://ils.test.rero.ch/global/search/persons?q=&page=4&size=10
https://ils.test.rero.ch/global/search/persons?q=&page=5&size=10
https://ils.test.rero.ch/global/search/persons?q=&page=6&size=10
https://ils.test.rero.ch/global/search/persons?q=&page=7&size=10
https://ils.test.rero.ch/global/search/persons?q=&page=8&size=10
https://ils.test.rero.ch/global/search/persons?q=&page=9&size=10
https://ils.test.rero.ch/global/search/persons?q=&page=10&size=10
https://ils.test.rero.ch/global/persons/1221475
https://ils.test.rero.ch/global/persons/5901043
https://ils.test.rero.ch/global/persons/5655672
https://ils.test.rero.ch/global/persons/10201296
https://ils.test.rero.ch/global/persons/5142288
https://ils.test.rero.ch/global/persons/9022437
https://ils.test.rero.ch/global/persons/8573359
https://ils.test.rero.ch/global/persons/3782534
https://ils.test.rero.ch/global/persons/800513
https://ils.test.rero.ch/global/persons/2995795
https://ils.test.rero.ch/global/search/corporate-bodies?q=&page=1&size=10
https://ils.test.rero.ch/global/search/corporate-bodies?q=&page=2&size=10
https://ils.test.rero.ch/global/search/corporate-bodies?q=&page=3&size=10
https://ils.test.rero.ch/global/search/corporate-bodies?q=&page=4&size=10
https://ils.test.rero.ch/global/search/corporate-bodies?q=&page=5&size=10
https://ils.test.rero.ch/global/search/corporate-bodies?q=&page=6&size=10
https://ils.test.rero.ch/global/search/corporate-bodies?q=&page=7&size=10
https://ils.test.rero.ch/global/search/corporate-bodies?q=&page=8&size=10
https://ils.test.rero.ch/global/search/corporate-bodies?q=&page=9&size=10
https://ils.test.rero.ch/global/search/corporate-bodies?q=&page=10&size=10
https://ils.test.rero.ch/global/corporate-bodies/10361408
https://ils.test.rero.ch/global/corporate-bodies/3556692
https://ils.test.rero.ch/global/corporate-bodies/4360604
https://ils.test.rero.ch/global/corporate-bodies/6443319
https://ils.test.rero.ch/global/corporate-bodies/9473715
https://ils.test.rero.ch/global/corporate-bodies/1067255
https://ils.test.rero.ch/global/corporate-bodies/5196282
https://ils.test.rero.ch/global/corporate-bodies/9388716
https://ils.test.rero.ch/global/corporate-bodies/1751988
https://ils.test.rero.ch/global/corporate-bodies/4057685
https://ils.test.rero.ch/patrons/logged_user?resolve
https://ils.test.rero.ch/api/translations/en.json
https://ils.test.rero.ch/api/libraries/?q=&page=1&size=9999&sort=name
https://ils.test.rero.ch/api/item/requested_loans/4
https://ils.test.rero.ch/api/documents/903?resolve=1
https://ils.test.rero.ch/api/documents/942?resolve=1
https://ils.test.rero.ch/api/documents/950?resolve=1
https://ils.test.rero.ch/api/documents/967?resolve=1
https://ils.test.rero.ch/api/patrons/?q=a&page=1&size=2&simple=1&roles=patron
https://ils.test.rero.ch/api/patrons/?q=barcode%3A2050124311&page=1&size=1
https://ils.test.rero.ch/api/patrons/4/circulation_informations
https://ils.test.rero.ch/api/item/loans/4?sort=-transaction_date
https://ils.test.rero.ch/api/loans/?q=patron_pid%3A4%20AND%20state%3AITEM_AT_DESK&page=1&size=9999
https://ils.test.rero.ch/api/patron_types/1?resolve=1
https://ils.test.rero.ch/api/item/barcode/10000000314
https://ils.test.rero.ch/api/item/barcode/10000000274
https://ils.test.rero.ch/api/item/barcode/10000000322
https://ils.test.rero.ch/api/item/barcode/10000000307
https://ils.test.rero.ch/api/item/barcode/10000001738
https://ils.test.rero.ch/api/patron_transactions/?q=loan.pid%3A68%20AND%20type%3Aoverdue%20AND%20status%3Aopen&page=1&size=9999
https://ils.test.rero.ch/api/documents/849?resolve=1
https://ils.test.rero.ch/api/patron_transactions/?q=loan.pid%3A70%20AND%20type%3Aoverdue%20AND%20status%3Aopen&page=1&size=9999
https://ils.test.rero.ch/api/documents/864?resolve=1
https://ils.test.rero.ch/api/patron_transactions/?q=loan.pid%3A65%20AND%20type%3Aoverdue%20AND%20status%3Aopen&page=1&size=9999
https://ils.test.rero.ch/api/documents/854?resolve=1
https://ils.test.rero.ch/api/organisations/1?resolve=0
https://ils.test.rero.ch/api/library/4/closed_dates?from=Sun%20Feb%2028%202021%2009%3A48%3A42%20GMT%2B0100&until=Thu%20Mar%2031%202022%2009%3A48%3A42%20GMT%2B0200
https://ils.test.rero.ch/api/ill_requests/?q=a&page=1&size=10&simple=1
https://ils.test.rero.ch/api/permissions/ill_requests/8
https://ils.test.rero.ch/api/patrons/11?resolve=0
https://ils.test.rero.ch/api/patrons/?q=&page=1&size=10&simple=1
https://ils.test.rero.ch/api/permissions/patrons/10
https://ils.test.rero.ch/api/permissions/patrons/11
https://ils.test.rero.ch/api/permissions/patrons/4
https://ils.test.rero.ch/api/permissions/patrons/6
https://ils.test.rero.ch/api/permissions/patrons/2
https://ils.test.rero.ch/api/permissions/patrons/8
https://ils.test.rero.ch/api/permissions/patrons/7
https://ils.test.rero.ch/api/permissions/patrons/1
https://ils.test.rero.ch/api/permissions/patrons/9
https://ils.test.rero.ch/api/permissions/patrons/12
https://ils.test.rero.ch/api/patrons/10?resolve=1
https://ils.test.rero.ch/api/patrons/11?resolve=1
https://ils.test.rero.ch/api/patrons/4?resolve=1
https://ils.test.rero.ch/api/patrons/6?resolve=1
https://ils.test.rero.ch/api/patrons/2?resolve=1
https://ils.test.rero.ch/api/patrons/8?resolve=1
https://ils.test.rero.ch/api/patrons/7?resolve=1
https://ils.test.rero.ch/api/patrons/1?resolve=1
https://ils.test.rero.ch/api/patrons/9?resolve=1
https://ils.test.rero.ch/api/patrons/12?resolve=1
https://ils.test.rero.ch/api/collections/?q=&page=1&size=10&library=4&simple=1
https://ils.test.rero.ch/api/permissions/collections/10
https://ils.test.rero.ch/api/permissions/collections/11
https://ils.test.rero.ch/api/documents/?q=&page=1&size=10&organisation=1&simple=1
https://ils.test.rero.ch/api/permissions/documents/2011010
https://ils.test.rero.ch/api/permissions/documents/2011009
https://ils.test.rero.ch/api/permissions/documents/2011008
https://ils.test.rero.ch/api/permissions/documents/2011007
https://ils.test.rero.ch/api/permissions/documents/2011006
https://ils.test.rero.ch/api/permissions/documents/2011005
https://ils.test.rero.ch/api/permissions/documents/2011004
https://ils.test.rero.ch/api/permissions/documents/2011003
https://ils.test.rero.ch/api/permissions/documents/2011002
https://ils.test.rero.ch/api/permissions/documents/2011001
https://ils.test.rero.ch/api/documents/2011010?resolve=1
https://ils.test.rero.ch/api/documents/2011009?resolve=1
https://ils.test.rero.ch/api/documents/2011008?resolve=1
https://ils.test.rero.ch/api/documents/2011007?resolve=1
https://ils.test.rero.ch/api/documents/2011006?resolve=1
https://ils.test.rero.ch/api/documents/2011005?resolve=1
https://ils.test.rero.ch/api/documents/2011004?resolve=1
https://ils.test.rero.ch/api/documents/2011003?resolve=1
https://ils.test.rero.ch/api/documents/2011002?resolve=1
https://ils.test.rero.ch/api/documents/2011001?resolve=1
https://ils.test.rero.ch/api/contributions/?q=&page=1&size=10&type=bf%3APerson&simple=1
https://ils.test.rero.ch/api/contributions/1221475?resolve=1
https://ils.test.rero.ch/api/contributions/5901043?resolve=1
https://ils.test.rero.ch/api/contributions/5655672?resolve=1
https://ils.test.rero.ch/api/contributions/10201296?resolve=1
https://ils.test.rero.ch/api/contributions/5142288?resolve=1
https://ils.test.rero.ch/api/contributions/9022437?resolve=1
https://ils.test.rero.ch/api/contributions/8573359?resolve=1
https://ils.test.rero.ch/api/contributions/3782534?resolve=1
https://ils.test.rero.ch/api/contributions/800513?resolve=1
https://ils.test.rero.ch/api/contributions/2995795?resolve=1
https://ils.test.rero.ch/api/vendors/?q=&page=1&size=10&simple=1
https://ils.test.rero.ch/api/acq_orders/?q=&page=1&size=10&simple=1
https://ils.test.rero.ch/api/budgets/?q=&page=1&size=10&simple=1
https://ils.test.rero.ch/api/items/?q=&page=1&size=10&simple=1&or_issue_status=late&or_issue_status=claimed
https://ils.test.rero.ch/api/items/?q=&page=1&size=10&library=4
https://ils.test.rero.ch/api/circ_policies/?q=&page=1&size=10&simple=1
https://ils.test.rero.ch/api/item_types/?q=&page=1&size=10&simple=1
https://ils.test.rero.ch/api/patron_types/?q=&page=1&size=10&simple=1
https://ils.test.rero.ch/api/budgets/?q=organisation.pid%3A1%20AND%20is_active%3Atrue&page=1&size=9999
https://ils.test.rero.ch/api/libraries/4?resolve=1
https://ils.test.rero.ch/api/permissions/locations/13
https://ils.test.rero.ch/api/libraries/?q=&page=1&size=10&simple=1
https://ils.test.rero.ch/api/templates/?q=&page=1&size=10&simple=1
```