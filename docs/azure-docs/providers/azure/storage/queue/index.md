---
title: queue
hide_title: false
hide_table_of_contents: false
keywords:
  - queue
  - storage
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
<tr><td><b>Name</b></td><td><code>queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.queue</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` |  |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Queue_Get` | `SELECT` | `accountName, queueName, resourceGroupName, subscriptionId` | Gets the queue with the specified queue name, under the specified account if it exists. |
| `Queue_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets a list of all the queues under the specified storage account |
| `Queue_Create` | `INSERT` | `accountName, queueName, resourceGroupName, subscriptionId` | Creates a new queue with the specified queue name, under the specified account. |
| `Queue_Delete` | `DELETE` | `accountName, queueName, resourceGroupName, subscriptionId` | Deletes the queue with the specified queue name, under the specified account if it exists. |
| `Queue_Update` | `EXEC` | `accountName, queueName, resourceGroupName, subscriptionId` | Creates a new queue with the specified queue name, under the specified account. |
