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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hybrid_runbook_worker_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.hybrid_runbook_worker_group" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Definition of hybrid runbook worker group property. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Retrieve a hybrid runbook worker group. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of hybrid runbook worker groups. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Create a hybrid runbook worker group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Delete a hybrid runbook worker group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Update a hybrid runbook worker group. |
