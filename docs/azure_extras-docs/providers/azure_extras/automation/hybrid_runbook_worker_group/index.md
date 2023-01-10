---
title: hybrid_runbook_worker_group
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_runbook_worker_group
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
<tr><td><b>Name</b></td><td><code>hybrid_runbook_worker_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.hybrid_runbook_worker_group</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Definition of hybrid runbook worker group property. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HybridRunbookWorkerGroup_Get` | `SELECT` | `automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId` | Retrieve a hybrid runbook worker group. |
| `HybridRunbookWorkerGroup_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of hybrid runbook worker groups. |
| `HybridRunbookWorkerGroup_Create` | `INSERT` | `automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId` | Create a hybrid runbook worker group. |
| `HybridRunbookWorkerGroup_Delete` | `DELETE` | `automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId` | Delete a hybrid runbook worker group. |
| `HybridRunbookWorkerGroup_Update` | `EXEC` | `automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId` | Update a hybrid runbook worker group. |
