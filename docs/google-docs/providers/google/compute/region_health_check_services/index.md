---
title: region_health_check_services
hide_title: false
hide_table_of_contents: false
keywords:
  - region_health_check_services
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
<tr><td><b>Name</b></td><td><code>region_health_check_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_health_check_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a HealthCheckService. An up-to-date fingerprint must be provided in order to patch/update the HealthCheckService; Otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the HealthCheckService. |
| `healthStatusAggregationPolicy` | `string` | Optional. Policy for how the results from multiple health checks for the same endpoint are aggregated. Defaults to NO_AGGREGATION if unspecified. - NO_AGGREGATION. An EndpointHealth message is returned for each pair in the health check service. - AND. If any health check of an endpoint reports UNHEALTHY, then UNHEALTHY is the HealthState of the endpoint. If all health checks report HEALTHY, the HealthState of the endpoint is HEALTHY. . |
| `region` | `string` | [Output Only] URL of the region where the health check service resides. This field is not applicable to global health check services. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `networkEndpointGroups` | `array` | A list of URLs to the NetworkEndpointGroup resources. Must not have more than 100. For regional HealthCheckService, NEGs must be in zones in the region of the HealthCheckService. |
| `healthChecks` | `array` | A list of URLs to the HealthCheck resources. Must have at least one HealthCheck, and not more than 10. HealthCheck resources must have portSpecification=USE_SERVING_PORT or portSpecification=USE_FIXED_PORT. For regional HealthCheckService, the HealthCheck must be regional and in the same region. For global HealthCheckService, HealthCheck must be global. Mix of regional and global HealthChecks is not supported. Multiple regional HealthChecks must belong to the same region. Regional HealthChecks must belong to the same region as zones of NEGs. |
| `notificationEndpoints` | `array` | A list of URLs to the NotificationEndpoint resources. Must not have more than 10. A list of endpoints for receiving notifications of change in health status. For regional HealthCheckService, NotificationEndpoint must be regional and in the same region. For global HealthCheckService, NotificationEndpoint must be global. |
| `kind` | `string` | [Output only] Type of the resource. Always compute#healthCheckServicefor health check services. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `regionHealthCheckServices_get` | `SELECT` | `healthCheckService, project, region` | Returns the specified regional HealthCheckService resource. |
| `regionHealthCheckServices_list` | `SELECT` | `project, region` | Lists all the HealthCheckService resources that have been configured for the specified project in the given region. |
| `regionHealthCheckServices_insert` | `INSERT` | `project, region` | Creates a regional HealthCheckService resource in the specified project and region using the data included in the request. |
| `regionHealthCheckServices_delete` | `DELETE` | `healthCheckService, project, region` | Deletes the specified regional HealthCheckService. |
| `regionHealthCheckServices_patch` | `EXEC` | `healthCheckService, project, region` | Updates the specified regional HealthCheckService resource with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
