---
title: watcher
hide_title: false
hide_table_of_contents: false
keywords:
  - watcher
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
<tr><td><b>Name</b></td><td><code>watcher</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.watcher" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `string` | Gets or sets the etag of the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Definition of the watcher properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Retrieve the watcher identified by watcher name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of watchers. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Create the watcher identified by watcher name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Delete the watcher by name. |
| <CopyableCode code="_list_by_automation_account" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of watchers. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Resume the watcher identified by watcher name. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Resume the watcher identified by watcher name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Update the watcher identified by watcher name. |
