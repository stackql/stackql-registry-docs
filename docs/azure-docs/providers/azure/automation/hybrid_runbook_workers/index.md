---
title: hybrid_runbook_workers
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_runbook_workers
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
<tr><td><b>Name</b></td><td><code>hybrid_runbook_workers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.hybrid_runbook_workers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Definition of hybrid runbook worker property. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId" /> | Retrieve a hybrid runbook worker. |
| <CopyableCode code="list_by_hybrid_runbook_worker_group" /> | `SELECT` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Retrieve a list of hybrid runbook workers. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId, data__properties" /> | Create a hybrid runbook worker. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId" /> | Delete a hybrid runbook worker. |
| <CopyableCode code="_list_by_hybrid_runbook_worker_group" /> | `EXEC` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Retrieve a list of hybrid runbook workers. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId" /> | Move a hybrid worker to a different group. |
