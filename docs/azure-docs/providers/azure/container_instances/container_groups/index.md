---
title: container_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - container_groups
  - container_instances
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
<tr><td><b>Name</b></td><td><code>container_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_instances.container_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | The resource name. |
| `identity` | `object` | Identity for the container group. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The container group properties |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The resource type. |
| `zones` | `array` | The zones for the container group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `containerGroupName, resourceGroupName, subscriptionId` | Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| `list` | `SELECT` | `subscriptionId` | Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| `create_or_update` | `INSERT` | `containerGroupName, resourceGroupName, subscriptionId` | Create or update container groups with specified configurations. |
| `delete` | `DELETE` | `containerGroupName, resourceGroupName, subscriptionId` | Delete the specified container group in the specified subscription and resource group. The operation does not delete other resources provided by the user, such as volumes. |
| `_list` | `EXEC` | `subscriptionId` | Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| `restart` | `EXEC` | `containerGroupName, resourceGroupName, subscriptionId` | Restarts all containers in a container group in place. If container image has updates, new image will be downloaded. |
| `start` | `EXEC` | `containerGroupName, resourceGroupName, subscriptionId` | Starts all containers in a container group. Compute resources will be allocated and billing will start. |
| `stop` | `EXEC` | `containerGroupName, resourceGroupName, subscriptionId` | Stops all containers in a container group. Compute resources will be deallocated and billing will stop. |
| `update` | `EXEC` | `containerGroupName, resourceGroupName, subscriptionId` | Updates container group tags with specified values. |
