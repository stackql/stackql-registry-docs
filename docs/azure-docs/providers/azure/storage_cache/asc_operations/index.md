---
title: asc_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - asc_operations
  - storage_cache
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
<tr><td><b>Name</b></td><td><code>asc_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_cache.asc_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The operation Id. |
| `name` | `string` | The operation name. |
| `properties` | `object` | Additional operation-specific output. |
| `startTime` | `string` | The start time of the operation. |
| `status` | `string` | The status of the operation. |
| `endTime` | `string` | The end time of the operation. |
| `error` | `object` | Describes the format of Error response. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AscOperations_Get` | `SELECT` | `location, operationId, subscriptionId` |
