---
title: remote_rendering_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - remote_rendering_accounts
  - mixed_reality
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
<tr><td><b>Name</b></td><td><code>remote_rendering_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mixed_reality.remote_rendering_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `kind` | `object` | The resource model definition representing SKU |
| `location` | `string` | The geo-location where the resource lives |
| `plan` | `object` | Identity for the resource. |
| `properties` | `object` | Common Properties shared by Mixed Reality Accounts |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieve a Remote Rendering Account. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List Resources by Resource Group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List Remote Rendering Accounts by Subscription |
| `create` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creating or Updating a Remote Rendering Account. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete a Remote Rendering Account. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List Resources by Resource Group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List Remote Rendering Accounts by Subscription |
| `regenerate_keys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Regenerate specified Key of a Remote Rendering Account |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updating a Remote Rendering Account |
