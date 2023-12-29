---
title: logs
hide_title: false
hide_table_of_contents: false
keywords:
  - logs
  - logs
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.logs.logs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `data` | `array` | Array of logs matching the request. |
| `links` | `object` | Links attributes. |
| `meta` | `object` | The metadata associated with a request |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_logs` | `SELECT` | `dd_site` | List endpoint returns logs that match a log search query.<br />[Results are paginated][1].<br /><br />Use this endpoint to build complex logs filtering and search.<br /><br />**If you are considering archiving logs for your organization,<br />consider use of the Datadog archive capabilities instead of the log list API.<br />See [Datadog Logs Archive documentation][2].**<br /><br />[1]: /logs/guide/collect-multiple-logs-with-pagination<br />[2]: https://docs.datadoghq.com/logs/archives |
| `aggregate_logs` | `EXEC` | `dd_site` | The API endpoint to aggregate events into buckets and compute metrics and timeseries. |
| `submit_log` | `EXEC` | `dd_site` | Send your logs to your Datadog platform over HTTP. Limits per HTTP request are:<br /><br />- Maximum content size per payload (uncompressed): 5MB<br />- Maximum size for a single log: 1MB<br />- Maximum array size if sending multiple logs in an array: 1000 entries<br /><br />Any log exceeding 1MB is accepted and truncated by Datadog:<br />- For a single log request, the API truncates the log at 1MB and returns a 2xx.<br />- For a multi-logs request, the API processes all logs, truncates only logs larger than 1MB, and returns a 2xx.<br /><br />Datadog recommends sending your logs compressed.<br />Add the `Content-Encoding: gzip` header to the request when sending compressed logs.<br />Log events can be submitted with a timestamp that is up to 18 hours in the past.<br /><br />The status codes answered by the HTTP API are:<br />- 202: Accepted: the request has been accepted for processing<br />- 400: Bad request (likely an issue in the payload formatting)<br />- 401: Unauthorized (likely a missing API Key)<br />- 403: Permission issue (likely using an invalid API Key)<br />- 408: Request Timeout, request should be retried after some time<br />- 413: Payload too large (batch is above 5MB uncompressed)<br />- 429: Too Many Requests, request should be retried after some time<br />- 500: Internal Server Error, the server encountered an unexpected condition that prevented it from fulfilling the request, request should be retried after some time<br />- 503: Service Unavailable, the server is not ready to handle the request probably because it is overloaded, request should be retried after some time |
