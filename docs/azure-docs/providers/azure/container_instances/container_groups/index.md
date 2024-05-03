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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_instances.container_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="identity" /> | `object` | Identity for the container group. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The container group properties |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
| <CopyableCode code="zones" /> | `array` | The zones for the container group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Create or update container groups with specified configurations. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Delete the specified container group in the specified subscription and resource group. The operation does not delete other resources provided by the user, such as volumes. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Restarts all containers in a container group in place. If container image has updates, new image will be downloaded. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Starts all containers in a container group. Compute resources will be allocated and billing will start. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Stops all containers in a container group. Compute resources will be deallocated and billing will stop. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Updates container group tags with specified values. |
