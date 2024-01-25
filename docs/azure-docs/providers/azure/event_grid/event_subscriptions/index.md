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
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the Event Subscription. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `eventSubscriptionName, scope` | Get properties of an event subscription. |
| `list_by_domain_topic` | `SELECT` | `domainName, resourceGroupName, subscriptionId, topicName` | List all event subscriptions that have been created for a specific domain topic. |
| `list_by_resource` | `SELECT` | `providerNamespace, resourceGroupName, resourceName, resourceTypeName, subscriptionId` | List all event subscriptions that have been created for a specific resource. |
| `create_or_update` | `INSERT` | `eventSubscriptionName, scope` | Asynchronously creates a new event subscription or updates an existing event subscription based on the specified scope. |
| `delete` | `DELETE` | `eventSubscriptionName, scope` | Delete an existing event subscription. |
| `_list_by_domain_topic` | `EXEC` | `domainName, resourceGroupName, subscriptionId, topicName` | List all event subscriptions that have been created for a specific domain topic. |
| `_list_by_resource` | `EXEC` | `providerNamespace, resourceGroupName, resourceName, resourceTypeName, subscriptionId` | List all event subscriptions that have been created for a specific resource. |
| `update` | `EXEC` | `eventSubscriptionName, scope` | Asynchronously updates an existing event subscription. |
