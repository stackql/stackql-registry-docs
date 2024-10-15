---
title: job_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_executions
  - sql
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_executions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_executions', value: 'view', },
        { label: 'job_executions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="create_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_attempt_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_attempts" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobAgentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobExecutionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_execution_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="step_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="step_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties for an Azure SQL Database Elastic job execution. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId" /> | Gets a job execution. |
| <CopyableCode code="list_by_agent" /> | `SELECT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Lists all executions in a job agent. |
| <CopyableCode code="list_by_job" /> | `SELECT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, subscriptionId" /> | Lists a job's executions. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, subscriptionId" /> | Starts an elastic job execution. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a job execution. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId" /> | Requests cancellation of a job execution. |

## `SELECT` examples

Lists all executions in a job agent.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_executions', value: 'view', },
        { label: 'job_executions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
create_time,
current_attempt_start_time,
current_attempts,
end_time,
jobAgentName,
jobExecutionId,
jobName,
job_execution_id,
job_version,
last_message,
lifecycle,
provisioning_state,
resourceGroupName,
serverName,
start_time,
step_id,
step_name,
subscriptionId,
target
FROM azure.sql.vw_job_executions
WHERE jobAgentName = '{{ jobAgentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.job_executions
WHERE jobAgentName = '{{ jobAgentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_executions</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.sql.job_executions (
jobAgentName,
jobName,
resourceGroupName,
serverName,
subscriptionId
)
SELECT 
'{{ jobAgentName }}',
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>
