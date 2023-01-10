---
title: hybrid_runbook_workers
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_runbook_workers
  - automation
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>hybrid_runbook_workers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.hybrid_runbook_workers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Definition of hybrid runbook worker property. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HybridRunbookWorkers_Get` | `SELECT` | `automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId` | Retrieve a hybrid runbook worker. |
| `HybridRunbookWorkers_ListByHybridRunbookWorkerGroup` | `SELECT` | `automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId` | Retrieve a list of hybrid runbook workers. |
| `HybridRunbookWorkers_Create` | `INSERT` | `automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId, data__properties` | Create a hybrid runbook worker. |
| `HybridRunbookWorkers_Delete` | `DELETE` | `automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId` | Delete a hybrid runbook worker. |
| `HybridRunbookWorkers_Move` | `EXEC` | `automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId` | Move a hybrid worker to a different group. |
