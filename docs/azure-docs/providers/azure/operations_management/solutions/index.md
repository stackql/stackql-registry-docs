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
| `location` | `string` | Resource location |
| `plan` | `object` | Plan for solution object supported by the OperationsManagement resource provider. |
| `properties` | `object` | Solution properties supported by the OperationsManagement resource provider. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, solutionName, subscriptionId` | Retrieves the user solution. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieves the solution list. It will retrieve both first party and third party solutions |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Retrieves the solution list. It will retrieve both first party and third party solutions |
| `create_or_update` | `INSERT` | `resourceGroupName, solutionName, subscriptionId` | Creates or updates the Solution. |
| `delete` | `DELETE` | `resourceGroupName, solutionName, subscriptionId` | Deletes the solution in the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieves the solution list. It will retrieve both first party and third party solutions |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Retrieves the solution list. It will retrieve both first party and third party solutions |
| `update` | `EXEC` | `resourceGroupName, solutionName, subscriptionId` | Patch a Solution. Only updating tags supported. |
