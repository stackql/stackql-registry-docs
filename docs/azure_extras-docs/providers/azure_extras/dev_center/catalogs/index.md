---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - dev_center
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
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.catalogs</code></td></tr>
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
| `Catalogs_Get` | `SELECT` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Gets a catalog |
| `Catalogs_ListByDevCenter` | `SELECT` | `devCenterName, resourceGroupName, subscriptionId` | Lists catalogs for a devcenter. |
| `Catalogs_CreateOrUpdate` | `INSERT` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Creates or updates a catalog. |
| `Catalogs_Delete` | `DELETE` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Deletes a catalog resource. |
| `Catalogs_Sync` | `EXEC` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Syncs templates for a template source. |
| `Catalogs_Update` | `EXEC` | `catalogName, devCenterName, resourceGroupName, subscriptionId` | Partially updates a catalog. |
