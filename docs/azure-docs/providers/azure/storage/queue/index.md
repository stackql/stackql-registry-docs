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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.queue" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, queueName, resourceGroupName, subscriptionId" /> | Gets the queue with the specified queue name, under the specified account if it exists. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets a list of all the queues under the specified storage account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, queueName, resourceGroupName, subscriptionId" /> | Creates a new queue with the specified queue name, under the specified account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, queueName, resourceGroupName, subscriptionId" /> | Deletes the queue with the specified queue name, under the specified account if it exists. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets a list of all the queues under the specified storage account |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, queueName, resourceGroupName, subscriptionId" /> | Creates a new queue with the specified queue name, under the specified account. |
