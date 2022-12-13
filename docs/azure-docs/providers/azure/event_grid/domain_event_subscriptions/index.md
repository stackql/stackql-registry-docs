---
title: domain_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>domain_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.domain_event_subscriptions</code></td></tr>
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
| `DomainEventSubscriptions_Get` | `SELECT` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Get properties of an event subscription of a domain. |
| `DomainEventSubscriptions_List` | `SELECT` | `domainName, resourceGroupName, subscriptionId` | List all event subscriptions that have been created for a specific topic. |
| `DomainEventSubscriptions_CreateOrUpdate` | `INSERT` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Asynchronously creates a new event subscription or updates an existing event subscription. |
| `DomainEventSubscriptions_Delete` | `DELETE` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Delete an existing event subscription for a domain. |
| `DomainEventSubscriptions_GetDeliveryAttributes` | `EXEC` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Get all delivery attributes for an event subscription for domain. |
| `DomainEventSubscriptions_GetFullUrl` | `EXEC` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Get the full endpoint URL for an event subscription for domain. |
| `DomainEventSubscriptions_Update` | `EXEC` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Update an existing event subscription for a topic. |
