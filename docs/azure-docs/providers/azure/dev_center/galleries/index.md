---
title: galleries
hide_title: false
hide_table_of_contents: false
keywords:
  - galleries
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
<tr><td><b>Name</b></td><td><code>galleries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_center.galleries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of a gallery. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `devCenterName, galleryName, resourceGroupName, subscriptionId` | Gets a gallery |
| `list_by_dev_center` | `SELECT` | `devCenterName, resourceGroupName, subscriptionId` | Lists galleries for a devcenter. |
| `create_or_update` | `INSERT` | `devCenterName, galleryName, resourceGroupName, subscriptionId` | Creates or updates a gallery. |
| `delete` | `DELETE` | `devCenterName, galleryName, resourceGroupName, subscriptionId` | Deletes a gallery resource. |
| `_list_by_dev_center` | `EXEC` | `devCenterName, resourceGroupName, subscriptionId` | Lists galleries for a devcenter. |
