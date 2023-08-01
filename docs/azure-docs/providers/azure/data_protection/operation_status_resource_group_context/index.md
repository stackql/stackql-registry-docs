---
title: operation_status_resource_group_context
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status_resource_group_context
  - data_protection
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
<tr><td><b>Name</b></td><td><code>operation_status_resource_group_context</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.operation_status_resource_group_context</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | It should match what is used to GET the operation result |
| `name` | `string` | It must match the last segment of the "id" field, and will typically be a GUID / system generated value |
| `properties` | `object` | Operation Extended Info |
| `startTime` | `string` | Start time of the operation |
| `status` | `string` |  |
| `endTime` | `string` | End time of the operation |
| `error` | `object` | The resource management error response. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationStatusResourceGroupContext_Get` | `SELECT` | `api-version, operationId, resourceGroupName, subscriptionId` |
