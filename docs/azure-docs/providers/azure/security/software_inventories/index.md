---
title: software_inventories
hide_title: false
hide_table_of_contents: false
keywords:
  - software_inventories
  - security
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
<tr><td><b>Name</b></td><td><code>software_inventories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.software_inventories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Software Inventory resource properties |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SoftwareInventories_Get` | `SELECT` | `api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, softwareName, subscriptionId` | Gets a single software data of the virtual machine. |
| `SoftwareInventories_ListByExtendedResource` | `SELECT` | `api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, subscriptionId` | Gets the software inventory of the virtual machine. |
| `SoftwareInventories_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets the software inventory of all virtual machines in the subscriptions. |
