---
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
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
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_bus.queues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The Queue Properties definition. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `namespaceName, queueName, resourceGroupName, subscriptionId` | Returns a description for the specified queue. |
| `list_by_namespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets the queues within a namespace. |
| `create_or_update` | `INSERT` | `namespaceName, queueName, resourceGroupName, subscriptionId` | Creates or updates a Service Bus queue. This operation is idempotent. |
| `delete` | `DELETE` | `namespaceName, queueName, resourceGroupName, subscriptionId` | Deletes a queue from the specified namespace in a resource group. |
| `_list_by_namespace` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets the queues within a namespace. |
| `regenerate_keys` | `EXEC` | `authorizationRuleName, namespaceName, queueName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the primary or secondary connection strings to the queue. |
