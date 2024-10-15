---
title: job_steps
hide_title: false
hide_table_of_contents: false
keywords:
  - job_steps
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

Creates, updates, deletes, gets or lists a <code>job_steps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_steps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_steps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_steps', value: 'view', },
        { label: 'job_steps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="action" /> | `text` | field from the `properties` object |
| <CopyableCode code="credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="execution_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobAgentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobVersion" /> | `text` | field from the `properties` object |
| <CopyableCode code="output" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="stepName" /> | `text` | field from the `properties` object |
| <CopyableCode code="step_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_group" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a job step. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId" /> | Gets a job step in a job's current version. |
| <CopyableCode code="get_by_version" /> | `SELECT` | <CopyableCode code="jobAgentName, jobName, jobVersion, resourceGroupName, serverName, stepName, subscriptionId" /> | Gets the specified version of a job step. |
| <CopyableCode code="list_by_job" /> | `SELECT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, subscriptionId" /> | Gets all job steps for a job's current version. |
| <CopyableCode code="list_by_version" /> | `SELECT` | <CopyableCode code="jobAgentName, jobName, jobVersion, resourceGroupName, serverName, subscriptionId" /> | Gets all job steps in the specified job version. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId" /> | Creates or updates a job step. This will implicitly create a new job version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId" /> | Deletes a job step. This will implicitly create a new job version. |

## `SELECT` examples

Gets all job steps for a job's current version.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_steps', value: 'view', },
        { label: 'job_steps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
action,
credential,
execution_options,
jobAgentName,
jobName,
jobVersion,
output,
resourceGroupName,
serverName,
stepName,
step_id,
subscriptionId,
target_group
FROM azure.sql.vw_job_steps
WHERE jobAgentName = '{{ jobAgentName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.job_steps
WHERE jobAgentName = '{{ jobAgentName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_steps</code> resource.

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
INSERT INTO azure.sql.job_steps (
jobAgentName,
jobName,
resourceGroupName,
serverName,
stepName,
subscriptionId,
properties
)
SELECT 
'{{ jobAgentName }}',
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ stepName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: stepId
          value: integer
        - name: targetGroup
          value: string
        - name: credential
          value: string
        - name: action
          value:
            - name: type
              value: string
            - name: source
              value: string
            - name: value
              value: string
        - name: output
          value:
            - name: type
              value: string
            - name: subscriptionId
              value: string
            - name: resourceGroupName
              value: string
            - name: serverName
              value: string
            - name: databaseName
              value: string
            - name: schemaName
              value: string
            - name: tableName
              value: string
            - name: credential
              value: string
        - name: executionOptions
          value:
            - name: timeoutSeconds
              value: integer
            - name: retryAttempts
              value: integer
            - name: initialRetryIntervalSeconds
              value: integer
            - name: maximumRetryIntervalSeconds
              value: integer
            - name: retryIntervalBackoffMultiplier
              value: number

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>job_steps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.job_steps
WHERE jobAgentName = '{{ jobAgentName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND stepName = '{{ stepName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
