---
title: operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status
  - storage_sync
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
<tr><td><b>Name</b></td><td><code>operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_sync.operation_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation Id |
| `startTime` | `string` | Start time of the operation |
| `status` | `string` | Operation status |
| `endTime` | `string` | End time of the operation |
| `error` | `object` | Error type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationStatus_Get` | `SELECT` | `locationName, operationId, resourceGroupName, subscriptionId, workflowId` |
| `LocationOperationStatus` | `EXEC` | `locationName, operationId, subscriptionId` |
