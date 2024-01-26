---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - vmware_cloud_simple
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.vmware_cloud_simple.virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/virtualMachines/&#123;virtualMachineName&#125; |
| `name` | `string` | &#123;virtualMachineName&#125; |
| `location` | `string` | Azure region |
| `properties` | `object` | Properties of virtual machine |
| `tags` | `object` | Tags model |
| `type` | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` | Get virtual machine |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Returns list of virtual machine within resource group |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | Returns list virtual machine within subscription |
| `create_or_update` | `INSERT` | `Referer, api-version, resourceGroupName, subscriptionId, virtualMachineName, data__location` | Create Or Update Virtual Machine |
| `delete` | `DELETE` | `Referer, api-version, resourceGroupName, subscriptionId, virtualMachineName` | Delete virtual machine |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Returns list of virtual machine within resource group |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | Returns list virtual machine within subscription |
| `start` | `EXEC` | `Referer, api-version, resourceGroupName, subscriptionId, virtualMachineName` | Power on virtual machine |
| `stop` | `EXEC` | `Referer, api-version, resourceGroupName, subscriptionId, virtualMachineName` | Power off virtual machine, options: shutdown, poweroff, and suspend |
| `update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` | Patch virtual machine properties |
