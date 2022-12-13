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
| `properties` | `object` | Class representing the Traffic Manager profile properties. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The Azure Region where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Profiles_Get` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Gets a Traffic Manager profile. |
| `Profiles_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Traffic Manager profiles within a resource group. |
| `Profiles_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all Traffic Manager profiles within a subscription. |
| `Profiles_CreateOrUpdate` | `INSERT` | `profileName, resourceGroupName, subscriptionId` | Create or update a Traffic Manager profile. |
| `Profiles_Delete` | `DELETE` | `profileName, resourceGroupName, subscriptionId` | Deletes a Traffic Manager profile. |
| `Profiles_CheckTrafficManagerRelativeDnsNameAvailability` | `EXEC` |  | Checks the availability of a Traffic Manager Relative DNS name. |
| `Profiles_Update` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Update a Traffic Manager profile. |
