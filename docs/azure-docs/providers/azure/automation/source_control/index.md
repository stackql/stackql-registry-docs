---
title: source_control
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control
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
<tr><td><b>Name</b></td><td><code>source_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.source_control" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId" /> | Retrieve the source control identified by source control name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of source controls. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId, data__properties" /> | Create a source control. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId" /> | Delete the source control. |
| <CopyableCode code="_list_by_automation_account" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of source controls. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId" /> | Update a source control. |
