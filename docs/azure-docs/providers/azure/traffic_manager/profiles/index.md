---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - traffic_manager
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
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.traffic_manager.profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The Azure Region where the resource lives |
| `properties` | `object` | Class representing the Traffic Manager profile properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Gets a Traffic Manager profile. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Traffic Manager profiles within a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all Traffic Manager profiles within a subscription. |
| `create_or_update` | `INSERT` | `profileName, resourceGroupName, subscriptionId` | Create or update a Traffic Manager profile. |
| `delete` | `DELETE` | `profileName, resourceGroupName, subscriptionId` | Deletes a Traffic Manager profile. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all Traffic Manager profiles within a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all Traffic Manager profiles within a subscription. |
| `check_traffic_manager_name_availability_v2` | `EXEC` | `subscriptionId` | Checks the availability of a Traffic Manager Relative DNS name. |
| `check_traffic_manager_relative_dns_name_availability` | `EXEC` |  | Checks the availability of a Traffic Manager Relative DNS name. |
| `update` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Update a Traffic Manager profile. |
