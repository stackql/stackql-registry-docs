---
title: domain_topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_topic_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>domain_topic_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.domain_topic_event_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Properties of the Event Subscription. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DomainTopicEventSubscriptions_Get` | `SELECT` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Get properties of a nested event subscription for a domain topic. |
| `DomainTopicEventSubscriptions_List` | `SELECT` | `domainName, resourceGroupName, subscriptionId, topicName` | List all event subscriptions that have been created for a specific domain topic. |
| `DomainTopicEventSubscriptions_CreateOrUpdate` | `INSERT` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Asynchronously creates a new event subscription or updates an existing event subscription. |
| `DomainTopicEventSubscriptions_Delete` | `DELETE` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Delete a nested existing event subscription for a domain topic. |
| `DomainTopicEventSubscriptions_GetDeliveryAttributes` | `EXEC` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Get all delivery attributes for an event subscription for domain topic. |
| `DomainTopicEventSubscriptions_GetFullUrl` | `EXEC` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Get the full endpoint URL for a nested event subscription for domain topic. |
| `DomainTopicEventSubscriptions_Update` | `EXEC` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId, topicName` | Update an existing event subscription for a domain topic. |
