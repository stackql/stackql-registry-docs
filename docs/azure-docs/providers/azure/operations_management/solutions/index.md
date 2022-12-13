---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
  - operations_management
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
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operations_management.solutions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `plan` | `object` | Plan for solution object supported by the OperationsManagement resource provider. |
| `properties` | `object` | Solution properties supported by the OperationsManagement resource provider. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type. |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Solutions_Get` | `SELECT` | `resourceGroupName, solutionName, subscriptionId` | Retrieves the user solution. |
| `Solutions_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieves the solution list. It will retrieve both first party and third party solutions |
| `Solutions_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieves the solution list. It will retrieve both first party and third party solutions |
| `Solutions_CreateOrUpdate` | `INSERT` | `resourceGroupName, solutionName, subscriptionId` | Creates or updates the Solution. |
| `Solutions_Delete` | `DELETE` | `resourceGroupName, solutionName, subscriptionId` | Deletes the solution in the subscription. |
| `Solutions_Update` | `EXEC` | `resourceGroupName, solutionName, subscriptionId` | Patch a Solution. Only updating tags supported. |
