---
title: object_anchors_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - object_anchors_accounts
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
<tr><td><b>Name</b></td><td><code>object_anchors_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mixed_reality.object_anchors_accounts</code></td></tr>
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
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieve an Object Anchors Account. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List Resources by Resource Group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List Object Anchors Accounts by Subscription |
| `create` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creating or Updating an object anchors Account. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete an Object Anchors Account. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List Resources by Resource Group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List Object Anchors Accounts by Subscription |
| `regenerate_keys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Regenerate specified Key of an object anchors Account |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updating an Object Anchors Account |
