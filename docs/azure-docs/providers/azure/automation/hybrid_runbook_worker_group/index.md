---
title: hybrid_runbook_worker_group
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_runbook_worker_group
  - automation
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
<tr><td><b>Name</b></td><td><code>hybrid_runbook_worker_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.hybrid_runbook_worker_group</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Definition of hybrid runbook worker group property. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId` | Retrieve a hybrid runbook worker group. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of hybrid runbook worker groups. |
| `create` | `INSERT` | `automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId` | Create a hybrid runbook worker group. |
| `delete` | `DELETE` | `automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId` | Delete a hybrid runbook worker group. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of hybrid runbook worker groups. |
| `update` | `EXEC` | `automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId` | Update a hybrid runbook worker group. |
