---
title: job_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_executions
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>job_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.job_executions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Job execution Name. |
| <CopyableCode code="endTime" /> | `string` | Job execution end time. |
| <CopyableCode code="jobSnapshot" /> | `object` | Job resource properties payload |
| <CopyableCode code="startTime" /> | `string` | Job execution start time. |
| <CopyableCode code="status" /> | `string` | Current state of the job execution |
| <CopyableCode code="template" /> | `object` | Job's execution template, containing configuration for an execution |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, serviceName, subscriptionId" /> |
