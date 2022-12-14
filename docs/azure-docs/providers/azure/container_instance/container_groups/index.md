---
title: container_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - container_groups
  - container_instance
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
<tr><td><b>Id</b></td><td><code>azure.container_instance.container_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The container group properties |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The resource type. |
| `zones` | `array` | The zones for the container group. |
| `identity` | `object` | Identity for the container group. |
| `location` | `string` | The resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ContainerGroups_Get` | `SELECT` | `containerGroupName, resourceGroupName, subscriptionId` | Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| `ContainerGroups_List` | `SELECT` | `subscriptionId` | Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| `ContainerGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| `ContainerGroups_CreateOrUpdate` | `INSERT` | `containerGroupName, resourceGroupName, subscriptionId` | Create or update container groups with specified configurations. |
| `ContainerGroups_Delete` | `DELETE` | `containerGroupName, resourceGroupName, subscriptionId` | Delete the specified container group in the specified subscription and resource group. The operation does not delete other resources provided by the user, such as volumes. |
| `ContainerGroups_GetOutboundNetworkDependenciesEndpoints` | `EXEC` | `containerGroupName, resourceGroupName, subscriptionId` | Gets all the network dependencies for this container group to allow complete control of network setting and configuration. For container groups, this will always be an empty list. |
| `ContainerGroups_Restart` | `EXEC` | `containerGroupName, resourceGroupName, subscriptionId` | Restarts all containers in a container group in place. If container image has updates, new image will be downloaded. |
| `ContainerGroups_Start` | `EXEC` | `containerGroupName, resourceGroupName, subscriptionId` | Starts all containers in a container group. Compute resources will be allocated and billing will start. |
| `ContainerGroups_Stop` | `EXEC` | `containerGroupName, resourceGroupName, subscriptionId` | Stops all containers in a container group. Compute resources will be deallocated and billing will stop. |
| `ContainerGroups_Update` | `EXEC` | `containerGroupName, resourceGroupName, subscriptionId` | Updates container group tags with specified values. |
