---
title: system_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - system_topics
  - event_grid
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
<tr><td><b>Name</b></td><td><code>system_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.system_topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The identity information for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the System Topic. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, systemTopicName` | Get properties of a system topic. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the system topics under a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the system topics under an Azure subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, systemTopicName` | Asynchronously creates a new system topic with the specified parameters. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, systemTopicName` | Delete existing system topic. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the system topics under a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the system topics under an Azure subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, systemTopicName` | Asynchronously updates a system topic with the specified parameters. |
