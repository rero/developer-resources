# Load testing

To test the website load, a tool named [`Siege`](https://github.com/JoeDog/siege) is used. Siege can simulate the navigation of concurrent users trough the website.

Siege comes with multiple options to simulate a real navigation on the website or to test the limits of the system.

## Installation

Siege can be easily installed with the following command in MacOS:

```shell
brew install siege
```

## Options

Here's the list of useful options to use with the software.

1. `--benchmark`: With this option, there's no delay between requests. That don't represent a real world example, but it's great to test the server capabilities.
2. `--delay=10`: Waits randomly from 0 to 10 seconds between each requests. This option has no effect if the `benchmark` option is set.
3. `--time=60S`: This is the duration of the test. If the option is not filled, the user have to manually stop the test.
4. `--concurrent=100`: Number of concurrent users. This option is great to simulate a number of users using the website at the same time.
5. `--file="/path/to/urls"`: A file containing the URLs, one URL per line.
6. `--internet`: Takes randomly an URL in the file instead of taking them sequentially.

## Authentication

If a URL need an authentication, a token can be passed with the header option:

```shell
--header "Authorization: Bearer ACCESS_TOKEN"
```

## Output

After the test, a JSON output is displayed, like the following:

```
{
    "transactions": 2189, // Total transactions done
    "availability": 100.00, // Percentage of the availibility of the server
    "elapsed_time": 119.02, // Total duration of the test
    "data_transferred": 115.32, // Amount of data transferred.
    "response_time": 0.05, // Average amount of time the web server took to respond to a request
    "transaction_rate": 18.39, // Average number of transactions per second.
    "throughput": 0.97, // Amount of data per second
    "concurrency": 1.00, // Average number of simultaneous connections.
    "successful_transactions": 2161, // Success transactions (status code 2xx or 3xx)
    "failed_transactions": 0, // Failed transactions (status code 4xx or 5xx)
    "longest_transaction": 0.85, // The longest transaction in seconds.
    "shortest_transaction": 0.00 // The shortest transaction in seconds.
}
```

## Annexes

* [Test result on RERO ILS](./ils-test-tests-result.md).