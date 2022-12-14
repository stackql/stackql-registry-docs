---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of the Topic. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Tags of the resource. |
| `identity` | `object` | The identity information for the resource. |
| `location` | `string` | Location of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Topics_Get` | `SELECT` | `resourceGroupName, subscriptionId, topicName` | Get properties of a topic. |
| `Topics_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the topics under a resource group. |
| `Topics_ListBySubscription` | `SELECT` | `subscriptionId` | List all the topics under an Azure subscription. |
| `Topics_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, topicName` | Asynchronously creates a new topic with the specified parameters. |
| `Topics_Delete` | `DELETE` | `resourceGroupName, subscriptionId, topicName` | Delete existing topic. |
| `Topics_ListEventTypes` | `EXEC` | `providerNamespace, resourceGroupName, resourceName, resourceTypeName, subscriptionId` | List event types for a topic. |
| `Topics_ListSharedAccessKeys` | `EXEC` | `resourceGroupName, subscriptionId, topicName` | List the two keys used to publish to a topic. |
| `Topics_RegenerateKey` | `EXEC` | `resourceGroupName, subscriptionId, topicName, data__keyName` | Regenerate a shared access key for a topic. |
| `Topics_Update` | `EXEC` | `resourceGroupName, subscriptionId, topicName` | Asynchronously updates a topic with the specified parameters. |
