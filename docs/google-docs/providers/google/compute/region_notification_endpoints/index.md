---
title: region_notification_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - region_notification_endpoints
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
<tr><td><b>Name</b></td><td><code>region_notification_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_notification_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] A unique identifier for this resource type. The server generates this identifier. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `grpcSettings` | `object` | Represents a gRPC setting that describes one gRPC notification endpoint and the retry duration attempting to send notification to this endpoint. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#notificationEndpoint for notification endpoints. |
| `region` | `string` | [Output Only] URL of the region where the notification endpoint resides. This field applies only to the regional resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `regionNotificationEndpoints_get` | `SELECT` | `notificationEndpoint, project, region` | Returns the specified NotificationEndpoint resource in the given region. |
| `regionNotificationEndpoints_list` | `SELECT` | `project, region` | Lists the NotificationEndpoints for a project in the given region. |
| `regionNotificationEndpoints_insert` | `INSERT` | `project, region` | Create a NotificationEndpoint in the specified project in the given region using the parameters that are included in the request. |
| `regionNotificationEndpoints_delete` | `DELETE` | `notificationEndpoint, project, region` | Deletes the specified NotificationEndpoint in the given region |
