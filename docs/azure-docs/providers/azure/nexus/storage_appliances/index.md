---
title: storage_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_appliances
  - nexus
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
<tr><td><b>Name</b></td><td><code>storage_appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.storage_appliances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, storageApplianceName, subscriptionId` | Get properties of the provided storage appliance. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of storage appliances in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of storage appliances in the provided subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, storageApplianceName, subscriptionId, data__extendedLocation, data__properties` | Create a new storage appliance or update the properties of the existing one.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| `delete` | `DELETE` | `resourceGroupName, storageApplianceName, subscriptionId` | Delete the provided storage appliance.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of storage appliances in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of storage appliances in the provided subscription. |
| `disable_remote_vendor_management` | `EXEC` | `resourceGroupName, storageApplianceName, subscriptionId` | Disable remote vendor management of the provided storage appliance. |
| `enable_remote_vendor_management` | `EXEC` | `resourceGroupName, storageApplianceName, subscriptionId` | Enable remote vendor management of the provided storage appliance. |
| `update` | `EXEC` | `resourceGroupName, storageApplianceName, subscriptionId` | Update properties of the provided storage appliance, or update tags associated with the storage appliance Properties and tag updates can be done independently. |
