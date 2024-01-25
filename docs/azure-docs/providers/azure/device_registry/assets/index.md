---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - device_registry
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
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.device_registry.assets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Asset resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `assetName, resourceGroupName, subscriptionId` | Retrieve a single asset. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all assets in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all assets in a subscription. |
| `create_or_replace` | `INSERT` | `assetName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a new asset or replace an existing asset. |
| `delete` | `DELETE` | `assetName, resourceGroupName, subscriptionId` | Delete an asset. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all assets in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all assets in a subscription. |
| `update` | `EXEC` | `assetName, resourceGroupName, subscriptionId` | Update specific asset properties. |
