---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
  - container_registry
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
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.webhooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The properties of a webhook. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `registryName, resourceGroupName, subscriptionId, webhookName` | Gets the properties of the specified webhook. |
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the webhooks for the specified container registry. |
| `create` | `INSERT` | `registryName, resourceGroupName, subscriptionId, webhookName, data__location` | Creates a webhook for a container registry with the specified parameters. |
| `delete` | `DELETE` | `registryName, resourceGroupName, subscriptionId, webhookName` | Deletes a webhook from a container registry. |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Lists all the webhooks for the specified container registry. |
| `ping` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Triggers a ping event to be sent to the webhook. |
| `update` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Updates a webhook with the specified parameters. |
