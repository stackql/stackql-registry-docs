---
title: public_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ip_addresses
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
<tr><td><b>Name</b></td><td><code>public_ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.public_ip_addresses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `zones` | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
| `type` | `string` | Resource type. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Public IP address properties. |
| `sku` | `object` | SKU of a public IP address. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PublicIPAddresses_Get` | `SELECT` | `publicIpAddressName, resourceGroupName, subscriptionId` | Gets the specified public IP address in a specified resource group. |
| `PublicIPAddresses_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all public IP addresses in a resource group. |
| `PublicIPAddresses_ListAll` | `SELECT` | `subscriptionId` | Gets all the public IP addresses in a subscription. |
| `PublicIPAddresses_CreateOrUpdate` | `INSERT` | `publicIpAddressName, resourceGroupName, subscriptionId` | Creates or updates a static or dynamic public IP address. |
| `PublicIPAddresses_Delete` | `DELETE` | `publicIpAddressName, resourceGroupName, subscriptionId` | Deletes the specified public IP address. |
| `PublicIPAddresses_GetCloudServicePublicIPAddress` | `EXEC` | `api-version, cloudServiceName, ipConfigurationName, networkInterfaceName, publicIpAddressName, resourceGroupName, roleInstanceName, subscriptionId` | Get the specified public IP address in a cloud service. |
| `PublicIPAddresses_GetVirtualMachineScaleSetPublicIPAddress` | `EXEC` | `api-version, ipConfigurationName, networkInterfaceName, publicIpAddressName, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex` | Get the specified public IP address in a virtual machine scale set. |
| `PublicIPAddresses_ListCloudServicePublicIPAddresses` | `EXEC` | `api-version, cloudServiceName, resourceGroupName, subscriptionId` | Gets information about all public IP addresses on a cloud service level. |
| `PublicIPAddresses_ListCloudServiceRoleInstancePublicIPAddresses` | `EXEC` | `api-version, cloudServiceName, ipConfigurationName, networkInterfaceName, resourceGroupName, roleInstanceName, subscriptionId` | Gets information about all public IP addresses in a role instance IP configuration in a cloud service. |
| `PublicIPAddresses_ListVirtualMachineScaleSetPublicIPAddresses` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineScaleSetName` | Gets information about all public IP addresses on a virtual machine scale set level. |
| `PublicIPAddresses_ListVirtualMachineScaleSetVMPublicIPAddresses` | `EXEC` | `api-version, ipConfigurationName, networkInterfaceName, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex` | Gets information about all public IP addresses in a virtual machine IP configuration in a virtual machine scale set. |
| `PublicIPAddresses_UpdateTags` | `EXEC` | `publicIpAddressName, resourceGroupName, subscriptionId` | Updates public IP address tags. |
| `PublicIpAddresses_DdosProtectionStatus` | `EXEC` | `publicIpAddressName, resourceGroupName, subscriptionId` | Gets the Ddos Protection Status of a Public IP Address |
