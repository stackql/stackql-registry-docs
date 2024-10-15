---
title: job_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_executions
  - spring_apps
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>job_executions</code> resource.

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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobExecutionName, jobName, resourceGroupName, serviceName, subscriptionId" /> | Get details of an execution of an Azure Spring Apps Job |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, serviceName, subscriptionId" /> | Get executions of a Azure Spring Apps Job |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="jobExecutionName, jobName, resourceGroupName, serviceName, subscriptionId" /> | Terminate execution of a running Azure Spring Apps Job |

## `SELECT` examples

Get executions of a Azure Spring Apps Job


```sql
SELECT
name,
endTime,
jobSnapshot,
startTime,
status,
template
FROM azure.spring_apps.job_executions
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```