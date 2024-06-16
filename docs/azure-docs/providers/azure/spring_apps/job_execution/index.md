---
title: job_execution
hide_title: false
hide_table_of_contents: false
keywords:
  - job_execution
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
<tr><td><b>Name</b></td><td><code>job_execution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.job_execution" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobExecutionName, jobName, resourceGroupName, serviceName, subscriptionId" /> | Get details of an execution of an Azure Spring Apps Job |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="jobExecutionName, jobName, resourceGroupName, serviceName, subscriptionId" /> | Terminate execution of a running Azure Spring Apps Job |
