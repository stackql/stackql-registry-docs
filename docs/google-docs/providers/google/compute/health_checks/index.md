---
title: health_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - health_checks
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.health_checks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in 3339 text format. |
| `kind` | `string` | Type of the resource. |
| `logConfig` | `object` | Configuration of logging on a health check. If logging is enabled, logs will be exported to Stackdriver. |
| `sslHealthCheck` | `object` |  |
| `httpsHealthCheck` | `object` |  |
| `timeoutSec` | `integer` | How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec. |
| `http2HealthCheck` | `object` |  |
| `checkIntervalSec` | `integer` | How often (in seconds) to send a health check. The default value is 5 seconds. |
| `tcpHealthCheck` | `object` |  |
| `region` | `string` | [Output Only] Region where the health check resides. Not applicable to global health checks. |
| `grpcHealthCheck` | `object` |  |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `type` | `string` | Specifies the type of the healthCheck, either TCP, SSL, HTTP, HTTPS, HTTP2 or GRPC. Exactly one of the protocol-specific health check fields must be specified, which must match type field. |
| `httpHealthCheck` | `object` |  |
| `healthyThreshold` | `integer` | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2. |
| `unhealthyThreshold` | `integer` | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `healthChecks_get` | `SELECT` | `healthCheck, project` | Returns the specified HealthCheck resource. Gets a list of available health checks by making a list() request. |
| `healthChecks_list` | `SELECT` | `project` | Retrieves the list of HealthCheck resources available to the specified project. |
| `healthChecks_insert` | `INSERT` | `project` | Creates a HealthCheck resource in the specified project using the data included in the request. |
| `healthChecks_delete` | `DELETE` | `healthCheck, project` | Deletes the specified HealthCheck resource. |
| `healthChecks_patch` | `EXEC` | `healthCheck, project` | Updates a HealthCheck resource in the specified project using the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| `healthChecks_update` | `EXEC` | `healthCheck, project` | Updates a HealthCheck resource in the specified project using the data included in the request. |
