---
title: async_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - async_operation_status
  - redis
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
<tr><td><b>Name</b></td><td><code>async_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.redis.async_operation_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ID for the async operation. |
| `name` | `string` | Name of the async operation. |
| `status` | `string` | Operation status. |
| `startTime` | `string` | The start time of the operation. |
| `properties` | `object` | Additional properties from RP, only when operation is successful |
| `operations` | `array` | The operations list. |
| `percentComplete` | `number` | Percent of the operation that is complete. |
| `endTime` | `string` | The end time of the operation. |
| `error` | `object` | The error detail. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AsyncOperationStatus_Get` | `SELECT` | `location, operationId, subscriptionId` |
