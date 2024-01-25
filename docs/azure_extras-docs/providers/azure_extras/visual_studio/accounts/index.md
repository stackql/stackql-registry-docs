---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - visual_studio
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.visual_studio.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of the resource. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Resource properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets the Visual Studio Team Services account resource details. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all Visual Studio Team Services account resources under the resource group linked to the specified Azure subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates or updates a Visual Studio Team Services account resource. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes a Visual Studio Team Services account resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all Visual Studio Team Services account resources under the resource group linked to the specified Azure subscription. |
| `check_name_availability` | `EXEC` | `subscriptionId` | Checks if the specified Visual Studio Team Services account name is available. Resource name can be either an account name or an account name and PUID. |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates tags for Visual Studio Team Services account resource. |
