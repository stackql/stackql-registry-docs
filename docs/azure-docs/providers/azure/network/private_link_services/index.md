---
title: private_link_services
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services
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
<tr><td><b>Name</b></td><td><code>private_link_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.private_link_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the private link service. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Gets the specified private link service by resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all private link services in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets all private link service in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Creates or updates an private link service in the specified resource group. |
| `delete` | `DELETE` | `resourceGroupName, serviceName, subscriptionId` | Deletes the specified private link service. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all private link services in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets all private link service in a subscription. |
| `check_private_link_service_visibility` | `EXEC` | `location, subscriptionId` | Checks whether the subscription is visible to private link service. |
| `check_private_link_service_visibility_by_resource_group` | `EXEC` | `location, resourceGroupName, subscriptionId` | Checks whether the subscription is visible to private link service in the specified resource group. |
