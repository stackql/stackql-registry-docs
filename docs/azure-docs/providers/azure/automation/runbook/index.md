---
title: runbook
hide_title: false
hide_table_of_contents: false
keywords:
  - runbook
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
<tr><td><b>Name</b></td><td><code>runbook</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.runbook" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Gets or sets the etag of the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Definition of the runbook property type. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Retrieve the runbook identified by runbook name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of runbooks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId, data__properties" /> | Create the runbook identified by runbook name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Delete the runbook by name. |
| <CopyableCode code="_list_by_automation_account" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of runbooks. |
| <CopyableCode code="publish" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Publish runbook draft. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Update the runbook identified by runbook name. |
