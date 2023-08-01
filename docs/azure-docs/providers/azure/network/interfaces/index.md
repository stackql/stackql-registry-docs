---
title: interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - interfaces
  - network
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
<tr><td><b>Name</b></td><td><code>interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.interfaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | NetworkInterface properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkInterfaces_Get` | `SELECT` | `networkInterfaceName, resourceGroupName, subscriptionId` | Gets information about the specified network interface. |
| `NetworkInterfaces_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all network interfaces in a resource group. |
| `NetworkInterfaces_ListAll` | `SELECT` | `subscriptionId` | Gets all network interfaces in a subscription. |
| `NetworkInterfaces_CreateOrUpdate` | `INSERT` | `networkInterfaceName, resourceGroupName, subscriptionId` | Creates or updates a network interface. |
| `NetworkInterfaces_Delete` | `DELETE` | `networkInterfaceName, resourceGroupName, subscriptionId` | Deletes the specified network interface. |
| `NetworkInterfaces_GetCloudServiceNetworkInterface` | `EXEC` | `api-version, cloudServiceName, networkInterfaceName, resourceGroupName, roleInstanceName, subscriptionId` | Get the specified network interface in a cloud service. |
| `NetworkInterfaces_GetEffectiveRouteTable` | `EXEC` | `networkInterfaceName, resourceGroupName, subscriptionId` | Gets all route tables applied to a network interface. |
| `NetworkInterfaces_GetVirtualMachineScaleSetIpConfiguration` | `EXEC` | `api-version, ipConfigurationName, networkInterfaceName, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex` | Get the specified network interface ip configuration in a virtual machine scale set. |
| `NetworkInterfaces_GetVirtualMachineScaleSetNetworkInterface` | `EXEC` | `api-version, networkInterfaceName, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex` | Get the specified network interface in a virtual machine scale set. |
| `NetworkInterfaces_ListCloudServiceNetworkInterfaces` | `EXEC` | `api-version, cloudServiceName, resourceGroupName, subscriptionId` | Gets all network interfaces in a cloud service. |
| `NetworkInterfaces_ListCloudServiceRoleInstanceNetworkInterfaces` | `EXEC` | `api-version, cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId` | Gets information about all network interfaces in a role instance in a cloud service. |
| `NetworkInterfaces_ListEffectiveNetworkSecurityGroups` | `EXEC` | `networkInterfaceName, resourceGroupName, subscriptionId` | Gets all network security groups applied to a network interface. |
| `NetworkInterfaces_ListVirtualMachineScaleSetIpConfigurations` | `EXEC` | `api-version, networkInterfaceName, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex` | Get the specified network interface ip configuration in a virtual machine scale set. |
| `NetworkInterfaces_ListVirtualMachineScaleSetNetworkInterfaces` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineScaleSetName` | Gets all network interfaces in a virtual machine scale set. |
| `NetworkInterfaces_ListVirtualMachineScaleSetVMNetworkInterfaces` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex` | Gets information about all network interfaces in a virtual machine in a virtual machine scale set. |
| `NetworkInterfaces_UpdateTags` | `EXEC` | `networkInterfaceName, resourceGroupName, subscriptionId` | Updates a network interface tags. |
