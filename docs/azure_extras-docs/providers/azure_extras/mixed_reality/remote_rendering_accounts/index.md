---
title: remote_rendering_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - remote_rendering_accounts
  - mixed_reality
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
<tr><td><b>Name</b></td><td><code>remote_rendering_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.mixed_reality.remote_rendering_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Common Properties shared by Mixed Reality Accounts |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the resource. |
| `kind` | `object` | The resource model definition representing SKU |
| `location` | `string` | The geo-location where the resource lives |
| `plan` | `object` | Identity for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RemoteRenderingAccounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieve a Remote Rendering Account. |
| `RemoteRenderingAccounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List Resources by Resource Group |
| `RemoteRenderingAccounts_ListBySubscription` | `SELECT` | `subscriptionId` | List Remote Rendering Accounts by Subscription |
| `RemoteRenderingAccounts_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creating or Updating a Remote Rendering Account. |
| `RemoteRenderingAccounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete a Remote Rendering Account. |
| `RemoteRenderingAccounts_ListKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | List Both of the 2 Keys of a Remote Rendering Account |
| `RemoteRenderingAccounts_RegenerateKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Regenerate specified Key of a Remote Rendering Account |
| `RemoteRenderingAccounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updating a Remote Rendering Account |
