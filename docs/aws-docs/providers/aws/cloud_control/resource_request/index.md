---
title: resource_request
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_request
  - cloud_control
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_request</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloud_control.resource_request</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `ErrorCode` | `string` |
| `EventTime` | `number` |
| `Identifier` | `string` |
| `Operation` | `string` |
| `OperationStatus` | `string` |
| `RequestToken` | `string` |
| `ResourceModel` | `string` |
| `RetryAfter` | `number` |
| `StatusMessage` | `string` |
| `TypeName` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_resource_request` | `SELECT` | `data__RequestToken, region` |
