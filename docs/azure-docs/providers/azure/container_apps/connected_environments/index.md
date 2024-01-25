---
title: connected_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments
  - container_apps
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
<tr><td><b>Name</b></td><td><code>connected_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.connected_environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The complex type of the extended location. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | ConnectedEnvironment resource specific properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectedEnvironmentName, resourceGroupName, subscriptionId` | Get the properties of an connectedEnvironment. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all connectedEnvironments in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get all connectedEnvironments for a subscription. |
| `create_or_update` | `INSERT` | `connectedEnvironmentName, resourceGroupName, subscriptionId` | Creates or updates an connectedEnvironment. |
| `delete` | `DELETE` | `connectedEnvironmentName, resourceGroupName, subscriptionId` | Delete an connectedEnvironment. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all connectedEnvironments in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get all connectedEnvironments for a subscription. |
| `check_name_availability` | `EXEC` | `connectedEnvironmentName, resourceGroupName, subscriptionId` | Checks if resource connectedEnvironmentName is available. |
| `update` | `EXEC` | `connectedEnvironmentName, resourceGroupName, subscriptionId` | Patches a Managed Environment. Only patching of tags is supported currently |
