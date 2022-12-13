---
title: partner_topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_topic_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>partner_topic_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_topic_event_subscriptions</code></td></tr>
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
| `PartnerTopicEventSubscriptions_Get` | `SELECT` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Get properties of an event subscription of a partner topic. |
| `PartnerTopicEventSubscriptions_ListByPartnerTopic` | `SELECT` | `partnerTopicName, resourceGroupName, subscriptionId` | List event subscriptions that belong to a specific partner topic. |
| `PartnerTopicEventSubscriptions_CreateOrUpdate` | `INSERT` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Asynchronously creates or updates an event subscription of a partner topic with the specified parameters. Existing event subscriptions will be updated with this API. |
| `PartnerTopicEventSubscriptions_Delete` | `DELETE` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Delete an existing event subscription of a partner topic. |
| `PartnerTopicEventSubscriptions_GetDeliveryAttributes` | `EXEC` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Get all delivery attributes for an event subscription of a partner topic. |
| `PartnerTopicEventSubscriptions_GetFullUrl` | `EXEC` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Get the full endpoint URL for an event subscription of a partner topic. |
| `PartnerTopicEventSubscriptions_Update` | `EXEC` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Update an existing event subscription of a partner topic. |
