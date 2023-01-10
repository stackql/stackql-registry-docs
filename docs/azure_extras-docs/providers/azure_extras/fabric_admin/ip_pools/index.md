---
title: ip_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_pools
  - fabric_admin
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
<tr><td><b>Name</b></td><td><code>ip_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.fabric_admin.ip_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of an IpPool. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IpPools_Get` | `SELECT` | `ipPool, location, resourceGroupName, subscriptionId` | Return the requested IP pool. |
| `IpPools_List` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a list of all IP pools at a certain location. |
| `IpPools_CreateOrUpdate` | `INSERT` | `ipPool, location, resourceGroupName, subscriptionId` | Create an IP pool.  Once created an IP pool cannot be deleted. |
