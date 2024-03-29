---
title: operation_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_statuses
  - log_analytics
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operation_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.log_analytics.operation_statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The operation Id. |
| `name` | `string` | The operation name. |
| `endTime` | `string` | The end time of the operation. |
| `error` | `object` | Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.) |
| `startTime` | `string` | The start time of the operation. |
| `status` | `string` | The status of the operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `asyncOperationId, location, subscriptionId` |
