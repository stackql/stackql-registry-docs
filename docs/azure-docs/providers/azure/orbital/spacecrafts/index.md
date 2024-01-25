---
title: spacecrafts
hide_title: false
hide_table_of_contents: false
keywords:
  - spacecrafts
  - orbital
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
<tr><td><b>Name</b></td><td><code>spacecrafts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.orbital.spacecrafts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | List of Spacecraft Resource Properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, spacecraftName, subscriptionId` | Gets the specified spacecraft in a specified resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Returns list of spacecrafts by resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Returns list of spacecrafts by subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, spacecraftName, subscriptionId, data__properties` | Creates or updates a spacecraft resource. |
| `delete` | `DELETE` | `resourceGroupName, spacecraftName, subscriptionId` | Deletes a specified spacecraft resource. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Returns list of spacecrafts by resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Returns list of spacecrafts by subscription. |
