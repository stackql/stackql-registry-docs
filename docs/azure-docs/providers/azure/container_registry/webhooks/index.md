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
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | The properties of a webhook. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Webhooks_Get` | `SELECT` | `registryName, resourceGroupName, subscriptionId, webhookName` | Gets the properties of the specified webhook. |
| `Webhooks_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the webhooks for the specified container registry. |
| `Webhooks_Create` | `INSERT` | `registryName, resourceGroupName, subscriptionId, webhookName, data__location` | Creates a webhook for a container registry with the specified parameters. |
| `Webhooks_Delete` | `DELETE` | `registryName, resourceGroupName, subscriptionId, webhookName` | Deletes a webhook from a container registry. |
| `Webhooks_GetCallbackConfig` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Gets the configuration of service URI and custom headers for the webhook. |
| `Webhooks_ListEvents` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Lists recent events for the specified webhook. |
| `Webhooks_Ping` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Triggers a ping event to be sent to the webhook. |
| `Webhooks_Update` | `EXEC` | `registryName, resourceGroupName, subscriptionId, webhookName` | Updates a webhook with the specified parameters. |
