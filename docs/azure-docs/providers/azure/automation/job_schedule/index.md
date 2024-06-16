---
title: job_schedule
hide_title: false
hide_table_of_contents: false
keywords:
  - job_schedule
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
<tr><td><b>Name</b></td><td><code>job_schedule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.job_schedule" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets the name of the variable. |
| <CopyableCode code="properties" /> | `object` | Definition of job schedule parameters. |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, jobScheduleId, resourceGroupName, subscriptionId" /> | Retrieve the job schedule identified by job schedule name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of job schedules. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, jobScheduleId, resourceGroupName, subscriptionId, data__properties" /> | Create a job schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, jobScheduleId, resourceGroupName, subscriptionId" /> | Delete the job schedule identified by job schedule name. |
