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
| `extendedLocation` | `object` | Definition of an Extended Location |
| `identity` | `object` | The identity information for the resource. |
| `kind` | `string` | Kind of the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the Topic. |
| `sku` | `object` | Describes an EventGrid Resource Sku. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, topicName` | Get properties of a topic. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the topics under a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the topics under an Azure subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, topicName` | Asynchronously creates a new topic with the specified parameters. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, topicName` | Delete existing topic. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the topics under a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the topics under an Azure subscription. |
| `regenerate_key` | `EXEC` | `resourceGroupName, subscriptionId, topicName, data__keyName` | Regenerate a shared access key for a topic. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, topicName` | Asynchronously updates a topic with the specified parameters. |
