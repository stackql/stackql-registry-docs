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
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Tags of the resource. |
| `identity` | `object` | The identity information for the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of the System Topic. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SystemTopics_Get` | `SELECT` | `resourceGroupName, subscriptionId, systemTopicName` | Get properties of a system topic. |
| `SystemTopics_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the system topics under a resource group. |
| `SystemTopics_ListBySubscription` | `SELECT` | `subscriptionId` | List all the system topics under an Azure subscription. |
| `SystemTopics_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, systemTopicName` | Asynchronously creates a new system topic with the specified parameters. |
| `SystemTopics_Delete` | `DELETE` | `resourceGroupName, subscriptionId, systemTopicName` | Delete existing system topic. |
| `SystemTopics_Update` | `EXEC` | `resourceGroupName, subscriptionId, systemTopicName` | Asynchronously updates a system topic with the specified parameters. |
