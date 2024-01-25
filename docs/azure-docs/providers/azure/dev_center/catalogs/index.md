---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - dev_center
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
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_center.catalogs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of a catalog. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Gets a catalog |
| `list_by_dev_center` | `SELECT` | `devCenterName, resourceGroupName, subscriptionId` | Lists catalogs for a devcenter. |
| `create_or_update` | `INSERT` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Creates or updates a catalog. |
| `delete` | `DELETE` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Deletes a catalog resource. |
| `_list_by_dev_center` | `EXEC` | `devCenterName, resourceGroupName, subscriptionId` | Lists catalogs for a devcenter. |
| `connect` | `EXEC` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Connects a catalog to enable syncing. |
| `sync` | `EXEC` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Syncs templates for a template source. |
| `update` | `EXEC` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Partially updates a catalog. |
