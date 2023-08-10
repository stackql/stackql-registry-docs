---
title: http_health_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - http_health_checks
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>http_health_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.http_health_checks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `port` | `integer` | The TCP port number for the HTTP health check request. The default value is 80. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `checkIntervalSec` | `integer` | How often (in seconds) to send a health check. The default value is 5 seconds. |
| `host` | `string` | The value of the host header in the HTTP health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used. |
| `unhealthyThreshold` | `integer` | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2. |
| `healthyThreshold` | `integer` | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#httpHealthCheck for HTTP health checks. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `timeoutSec` | `integer` | How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec. |
| `requestPath` | `string` | The request path of the HTTP health check request. The default value is /. This field does not support query parameters. Must comply with RFC3986. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `httpHealthCheck, project` | Returns the specified HttpHealthCheck resource. |
| `list` | `SELECT` | `project` | Retrieves the list of HttpHealthCheck resources available to the specified project. |
| `insert` | `INSERT` | `project` | Creates a HttpHealthCheck resource in the specified project using the data included in the request. |
| `delete` | `DELETE` | `httpHealthCheck, project` | Deletes the specified HttpHealthCheck resource. |
| `_list` | `EXEC` | `project` | Retrieves the list of HttpHealthCheck resources available to the specified project. |
| `patch` | `EXEC` | `httpHealthCheck, project` | Updates a HttpHealthCheck resource in the specified project using the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| `update` | `EXEC` | `httpHealthCheck, project` | Updates a HttpHealthCheck resource in the specified project using the data included in the request. |
