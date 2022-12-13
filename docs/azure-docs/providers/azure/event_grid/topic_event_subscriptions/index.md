---
title: topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>topic_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.topic_event_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource. |
| `name` | `string` | Name of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the resource. |
| `properties` | `object` | Properties of the Event Subscription. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TopicEventSubscriptions_Get` | `SELECT` | `eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Get properties of an event subscription of a topic. |
| `TopicEventSubscriptions_List` | `SELECT` | `resourceGroupName, subscriptionId, topicName` | List all event subscriptions that have been created for a specific topic. |
| `TopicEventSubscriptions_CreateOrUpdate` | `INSERT` | `eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Asynchronously creates a new event subscription or updates an existing event subscription. |
| `TopicEventSubscriptions_Delete` | `DELETE` | `eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Delete an existing event subscription for a topic. |
| `TopicEventSubscriptions_GetDeliveryAttributes` | `EXEC` | `eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Get all delivery attributes for an event subscription for topic. |
| `TopicEventSubscriptions_GetFullUrl` | `EXEC` | `eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Get the full endpoint URL for an event subscription for topic. |
| `TopicEventSubscriptions_Update` | `EXEC` | `eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Update an existing event subscription for a topic. |
