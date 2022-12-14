---
title: device_security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - device_security_groups
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
<tr><td><b>Name</b></td><td><code>device_security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.device_security_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | describes properties of a security group. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeviceSecurityGroups_Get` | `SELECT` | `api-version, deviceSecurityGroupName, resourceId` | Use this method to get the device security group for the specified IoT Hub resource. |
| `DeviceSecurityGroups_List` | `SELECT` | `api-version, resourceId` | Use this method get the list of device security groups for the specified IoT Hub resource. |
| `DeviceSecurityGroups_CreateOrUpdate` | `INSERT` | `api-version, deviceSecurityGroupName, resourceId` | Use this method to creates or updates the device security group on a specified IoT Hub resource. |
| `DeviceSecurityGroups_Delete` | `DELETE` | `api-version, deviceSecurityGroupName, resourceId` | User this method to deletes the device security group. |
