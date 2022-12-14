---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - service_bus
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
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_bus.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Description of Subscription Resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Subscriptions_Get` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName` | Returns a subscription description for the specified topic. |
| `Subscriptions_ListByTopic` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId, topicName` | List all the subscriptions under a specified topic. |
| `Subscriptions_CreateOrUpdate` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName` | Creates a topic subscription. |
| `Subscriptions_Delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName` | Deletes a subscription from the specified topic. |
