---
title: resource_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_groups
  - resources
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
<tr><td><b>Name</b></td><td><code>resource_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resources.resource_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource group. |
| `name` | `string` | The name of the resource group. |
| `managedBy` | `string` | The ID of the resource that manages this resource group. |
| `properties` | `object` | The resource group properties. |
| `tags` | `object` | The tags attached to the resource group. |
| `type` | `string` | The type of the resource group. |
| `location` | `string` | The location of the resource group. It cannot be changed after the resource group has been created. It must be one of the supported Azure locations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ResourceGroups_Get` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a resource group. |
| `ResourceGroups_List` | `SELECT` | `subscriptionId` | Gets all the resource groups for a subscription. |
| `ResourceGroups_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, data__location` | Creates or updates a resource group. |
| `ResourceGroups_Delete` | `DELETE` | `resourceGroupName, subscriptionId` | When you delete a resource group, all of its resources are also deleted. Deleting a resource group deletes all of its template deployments and currently stored operations. |
| `ResourceGroups_CheckExistence` | `EXEC` | `resourceGroupName, subscriptionId` | Checks whether a resource group exists. |
| `ResourceGroups_ExportTemplate` | `EXEC` | `resourceGroupName, subscriptionId` | Captures the specified resource group as a template. |
| `ResourceGroups_Update` | `EXEC` | `resourceGroupName, subscriptionId` | Resource groups can be updated through a simple PATCH operation to a group address. The format of the request is the same as that for creating a resource group. If a field is unspecified, the current value is retained. |
