---
title: async_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - async_operations
  - storage_admin
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
<tr><td><b>Name</b></td><td><code>async_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_admin.async_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The operation id. |
| `httpStatus` | `string` | Http status for the async operation. |
| `response` | `string` | Response for the async operation. |
| `operation` | `object` | Async operation content |
| `operationStartTime` | `string` | Operation start time. |
| `locationHeader` | `string` | Location header for async operation. |
| `subscriptionId` | `string` | Subscription id for async operation. |
| `context` | `object` | Operation request context. |
| `operationEndTime` | `string` | Operation end time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AsyncOperations_Get` | `SELECT` | `asyncOperationId, location, subscriptionId` |
