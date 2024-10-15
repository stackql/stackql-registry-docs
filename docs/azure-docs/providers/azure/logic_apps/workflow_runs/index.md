---
title: workflow_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_runs
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>workflow_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflow_runs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_runs', value: 'view', },
        { label: 'workflow_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the workflow run name. |
| <CopyableCode code="code" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="outputs" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="response" /> | `text` | field from the `properties` object |
| <CopyableCode code="runName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="trigger" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the workflow run type. |
| <CopyableCode code="wait_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="workflow" /> | `text` | field from the `properties` object |
| <CopyableCode code="workflowName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the workflow run name. |
| <CopyableCode code="properties" /> | `object` | The workflow run properties. |
| <CopyableCode code="type" /> | `string` | Gets the workflow run type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, runName, subscriptionId, workflowName" /> | Gets a workflow run. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Gets a list of workflow runs. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="resourceGroupName, runName, subscriptionId, workflowName" /> | Cancels a workflow run. |

## `SELECT` examples

Gets a list of workflow runs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_runs', value: 'view', },
        { label: 'workflow_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
code,
correlation,
correlation_id,
end_time,
error,
outputs,
resourceGroupName,
response,
runName,
start_time,
status,
subscriptionId,
trigger,
type,
wait_end_time,
workflow,
workflowName
FROM azure.logic_apps.vw_workflow_runs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.logic_apps.workflow_runs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```
</TabItem></Tabs>

