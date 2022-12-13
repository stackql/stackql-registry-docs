---
title: event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - event_subscriptions
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
<tr><td><b>Name</b></td><td><code>event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.event_subscriptions</code></td></tr>
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
| `EventSubscriptions_Get` | `SELECT` | `eventSubscriptionName, scope` | Get properties of an event subscription. |
| `EventSubscriptions_ListByDomainTopic` | `SELECT` | `domainName, resourceGroupName, subscriptionId, topicName` | List all event subscriptions that have been created for a specific domain topic. |
| `EventSubscriptions_ListByResource` | `SELECT` | `providerNamespace, resourceGroupName, resourceName, resourceTypeName, subscriptionId` | List all event subscriptions that have been created for a specific resource. |
| `EventSubscriptions_CreateOrUpdate` | `INSERT` | `eventSubscriptionName, scope` | Asynchronously creates a new event subscription or updates an existing event subscription based on the specified scope. |
| `EventSubscriptions_Delete` | `DELETE` | `eventSubscriptionName, scope` | Delete an existing event subscription. |
| `EventSubscriptions_GetDeliveryAttributes` | `EXEC` | `eventSubscriptionName, scope` | Get all delivery attributes for an event subscription. |
| `EventSubscriptions_GetFullUrl` | `EXEC` | `eventSubscriptionName, scope` | Get the full endpoint URL for an event subscription. |
| `EventSubscriptions_ListGlobalByResourceGroup` | `EXEC` | `resourceGroupName, subscriptionId` | List all global event subscriptions under a specific Azure subscription and resource group. |
| `EventSubscriptions_ListGlobalByResourceGroupForTopicType` | `EXEC` | `resourceGroupName, subscriptionId, topicTypeName` | List all global event subscriptions under a resource group for a specific topic type. |
| `EventSubscriptions_ListGlobalBySubscription` | `EXEC` | `subscriptionId` | List all aggregated global event subscriptions under a specific Azure subscription. |
| `EventSubscriptions_ListGlobalBySubscriptionForTopicType` | `EXEC` | `subscriptionId, topicTypeName` | List all global event subscriptions under an Azure subscription for a topic type. |
| `EventSubscriptions_ListRegionalByResourceGroup` | `EXEC` | `location, resourceGroupName, subscriptionId` | List all event subscriptions from the given location under a specific Azure subscription and resource group. |
| `EventSubscriptions_ListRegionalByResourceGroupForTopicType` | `EXEC` | `location, resourceGroupName, subscriptionId, topicTypeName` | List all event subscriptions from the given location under a specific Azure subscription and resource group and topic type. |
| `EventSubscriptions_ListRegionalBySubscription` | `EXEC` | `location, subscriptionId` | List all event subscriptions from the given location under a specific Azure subscription. |
| `EventSubscriptions_ListRegionalBySubscriptionForTopicType` | `EXEC` | `location, subscriptionId, topicTypeName` | List all event subscriptions from the given location under a specific Azure subscription and topic type. |
| `EventSubscriptions_Update` | `EXEC` | `eventSubscriptionName, scope` | Asynchronously updates an existing event subscription. |
