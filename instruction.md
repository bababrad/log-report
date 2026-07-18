# Access log summary report

An Apache-style access log is available at `/app/access.log` in the working
directory. Parse it and produce a small JSON summary report describing the
traffic.

## Output

Write your report to `/app/report.json` as a single JSON object with exactly
these three keys:

- `total_requests` (integer): the number of non-empty request lines in the log.
- `unique_ips` (integer): the number of distinct client IP addresses (the first
  whitespace-separated field of each line).
- `top_path` (string): the request path that appears most frequently across all
  requests (the path from the quoted request line, e.g. `/index.html`).

Example shape (illustrative values, not the answer):

```json
{"total_requests": 42, "unique_ips": 7, "top_path": "/some/path"}
```

## Success criteria

1. A file exists at `/app/report.json` containing a single JSON object.
2. `total_requests` equals the number of non-empty lines in `/app/access.log`.
3. `unique_ips` equals the number of distinct client IP addresses in the log.
4. `top_path` equals the most frequently requested path in the log.
