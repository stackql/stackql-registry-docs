---
title: source_control_sync_job
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_sync_job
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
<tr><td><b>Name</b></td><td><code>source_control_sync_job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.source_control_sync_job" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the job. |
| <CopyableCode code="properties" /> | `object` | Definition of source control sync job properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, sourceControlSyncJobId, subscriptionId" /> | Retrieve the source control sync job identified by job id. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId" /> | Retrieve a list of source control sync jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, sourceControlSyncJobId, subscriptionId, data__properties" /> | Creates the sync job for a source control. |
| <CopyableCode code="_list_by_automation_account" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId" /> | Retrieve a list of source control sync jobs. |
