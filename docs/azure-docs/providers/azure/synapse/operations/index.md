---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name |
| `display` | `object` | Description of an available operation |
| `isDataAction` | `string` | Whether this operation is a data action |
| `origin` | `string` | Operation origin |
| `properties` | `object` | What is this? |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Operations_List` | `SELECT` |  | Get all available operations |
| `Operations_CheckNameAvailability` | `EXEC` | `subscriptionId` | Check whether a workspace name is available |
| `Operations_GetAzureAsyncHeaderResult` | `EXEC` | `operationId, resourceGroupName, subscriptionId, workspaceName` | Get the status of an operation |
| `Operations_GetLocationHeaderResult` | `EXEC` | `operationId, resourceGroupName, subscriptionId, workspaceName` | Get the result of an operation |
