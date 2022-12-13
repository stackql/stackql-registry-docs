---
title: consumer_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_groups
  - event_hub
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
<tr><td><b>Name</b></td><td><code>consumer_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_hub.consumer_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `` | Single item in List or Get Consumer group operation |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConsumerGroups_Get` | `SELECT` | `consumerGroupName, eventHubName, namespaceName, resourceGroupName, subscriptionId` | Gets a description for the specified consumer group. |
| `ConsumerGroups_ListByEventHub` | `SELECT` | `eventHubName, namespaceName, resourceGroupName, subscriptionId` | Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group exists in the Namespace. |
| `ConsumerGroups_CreateOrUpdate` | `INSERT` | `consumerGroupName, eventHubName, namespaceName, resourceGroupName, subscriptionId` | Creates or updates an Event Hubs consumer group as a nested resource within a Namespace. |
| `ConsumerGroups_Delete` | `DELETE` | `consumerGroupName, eventHubName, namespaceName, resourceGroupName, subscriptionId` | Deletes a consumer group from the specified Event Hub and resource group. |
