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
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the Event Subscription. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Get properties of an event subscription of a partner topic. |
| `list_by_partner_topic` | `SELECT` | `partnerTopicName, resourceGroupName, subscriptionId` | List event subscriptions that belong to a specific partner topic. |
| `create_or_update` | `INSERT` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Asynchronously creates or updates an event subscription of a partner topic with the specified parameters. Existing event subscriptions will be updated with this API. |
| `delete` | `DELETE` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Delete an existing event subscription of a partner topic. |
| `_list_by_partner_topic` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | List event subscriptions that belong to a specific partner topic. |
| `update` | `EXEC` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Update an existing event subscription of a partner topic. |
