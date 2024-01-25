---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_bus.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The Topic Properties definition. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Returns a description for the specified topic. |
| `list_by_namespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets all the topics in a namespace. |
| `create_or_update` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Creates a topic in the specified namespace. |
| `delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Deletes a topic from the specified namespace and resource group. |
| `_list_by_namespace` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets all the topics in a namespace. |
| `regenerate_keys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, topicName, data__keyType` | Regenerates primary or secondary connection strings for the topic. |
