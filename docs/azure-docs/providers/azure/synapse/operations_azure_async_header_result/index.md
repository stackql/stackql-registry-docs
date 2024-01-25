---
title: operations_azure_async_header_result
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_azure_async_header_result
  - synapse
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
<tr><td><b>Name</b></td><td><code>operations_azure_async_header_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.operations_azure_async_header_result</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Operation ID |
| `name` | `string` | Operation name |
| `endTime` | `string` | Operation start time |
| `error` | `object` | The error detail. |
| `percentComplete` | `number` | Completion percentage of the operation |
| `properties` | `object` | Operation properties |
| `startTime` | `string` | Operation start time |
| `status` | `string` | Operation status |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `operationId, resourceGroupName, subscriptionId, workspaceName` |
