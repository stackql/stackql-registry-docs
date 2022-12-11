---
title: resource_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_requests
  - cloud_control
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloud_control.resource_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `StatusMessage` | `string` |
| `EventTime` | `number` |
| `TypeName` | `string` |
| `ResourceModel` | `string` |
| `RequestToken` | `string` |
| `ErrorCode` | `string` |
| `Identifier` | `string` |
| `Operation` | `string` |
| `OperationStatus` | `string` |
| `RetryAfter` | `number` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_resource_request` | `SELECT` | `data__RequestToken` |
| `list_resource_requests` | `SELECT` | `data__ResourceRequestStatusFilter` |
| `cancel_resource_request` | `DELETE` | `data__RequestToken` |
