---
title: spaces
hide_title: false
hide_table_of_contents: false
keywords:
  - spaces
  - integration_environment
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
<tr><td><b>Name</b></td><td><code>spaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.integration_environment.spaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of space. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, spaceName, subscriptionId` | Get a Space |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List Space resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List Space resources by subscription ID |
| `create_or_update` | `INSERT` | `resourceGroupName, spaceName, subscriptionId` | Create a Space |
| `delete` | `DELETE` | `resourceGroupName, spaceName, subscriptionId` | Delete a Space |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List Space resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List Space resources by subscription ID |
| `patch` | `EXEC` | `resourceGroupName, spaceName, subscriptionId` | Update a Space |
