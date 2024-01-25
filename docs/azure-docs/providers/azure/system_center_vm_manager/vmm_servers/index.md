---
title: vmm_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - vmm_servers
  - system_center_vm_manager
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
<tr><td><b>Name</b></td><td><code>vmm_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.vmm_servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vmmServerName` | Implements VMMServer GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List of VmmServers in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List of VmmServers in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, vmmServerName, data__extendedLocation, data__properties` | Onboards the SCVMM fabric as an Azure VmmServer resource. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vmmServerName` | Removes the SCVMM fabric from Azure. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List of VmmServers in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List of VmmServers in a subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, vmmServerName` | Updates the VmmServers resource. |
