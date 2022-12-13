---
title: system_topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - system_topic_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>system_topic_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.system_topic_event_subscriptions</code></td></tr>
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
| `SystemTopicEventSubscriptions_Get` | `SELECT` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Get an event subscription. |
| `SystemTopicEventSubscriptions_ListBySystemTopic` | `SELECT` | `resourceGroupName, subscriptionId, systemTopicName` | List event subscriptions that belong to a specific system topic. |
| `SystemTopicEventSubscriptions_CreateOrUpdate` | `INSERT` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Asynchronously creates or updates an event subscription with the specified parameters. Existing event subscriptions will be updated with this API. |
| `SystemTopicEventSubscriptions_Delete` | `DELETE` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Delete an existing event subscription of a system topic. |
| `SystemTopicEventSubscriptions_GetDeliveryAttributes` | `EXEC` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Get all delivery attributes for an event subscription. |
| `SystemTopicEventSubscriptions_GetFullUrl` | `EXEC` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Get the full endpoint URL for an event subscription of a system topic. |
| `SystemTopicEventSubscriptions_Update` | `EXEC` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Update an existing event subscription of a system topic. |
