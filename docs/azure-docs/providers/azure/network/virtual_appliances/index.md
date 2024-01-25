---
title: virtual_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_appliances
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
<tr><td><b>Name</b></td><td><code>virtual_appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_appliances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Network Virtual Appliance definition. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkVirtualApplianceName, resourceGroupName, subscriptionId` | Gets the specified Network Virtual Appliance. |
| `list` | `SELECT` | `subscriptionId` | Gets all Network Virtual Appliances in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Network Virtual Appliances in a resource group. |
| `create_or_update` | `INSERT` | `networkVirtualApplianceName, resourceGroupName, subscriptionId` | Creates or updates the specified Network Virtual Appliance. |
| `delete` | `DELETE` | `networkVirtualApplianceName, resourceGroupName, subscriptionId` | Deletes the specified Network Virtual Appliance. |
| `_list` | `EXEC` | `subscriptionId` | Gets all Network Virtual Appliances in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all Network Virtual Appliances in a resource group. |
