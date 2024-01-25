---
title: namespace_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - namespace_topics
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
<tr><td><b>Name</b></td><td><code>namespace_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.namespace_topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the namespace topic. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Get properties of a namespace topic. |
| `list_by_namespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | List all the namespace topics under a namespace. |
| `create_or_update` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Asynchronously creates a new namespace topic with the specified parameters. |
| `delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Delete existing namespace topic. |
| `_list_by_namespace` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | List all the namespace topics under a namespace. |
| `regenerate_key` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId, topicName, data__keyName` | Regenerate a shared access key for a namespace topic. |
| `update` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Asynchronously updates a namespace topic with the specified parameters. |
