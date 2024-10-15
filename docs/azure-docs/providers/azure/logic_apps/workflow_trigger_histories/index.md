---
title: workflow_trigger_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_trigger_histories
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

Creates, updates, deletes, gets or lists a <code>workflow_trigger_histories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_trigger_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflow_trigger_histories" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_trigger_histories', value: 'view', },
        { label: 'workflow_trigger_histories', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the workflow trigger history name. |
| <CopyableCode code="code" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="fired" /> | `text` | field from the `properties` object |
| <CopyableCode code="historyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="inputs_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="outputs_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tracking_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="triggerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the workflow trigger history type. |
| <CopyableCode code="workflowName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the workflow trigger history name. |
| <CopyableCode code="properties" /> | `object` | The workflow trigger history properties. |
| <CopyableCode code="type" /> | `string` | Gets the workflow trigger history type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="historyName, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Gets a workflow trigger history. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, triggerName, workflowName" /> | Gets a list of workflow trigger histories. |
| <CopyableCode code="resubmit" /> | `EXEC` | <CopyableCode code="historyName, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Resubmits a workflow run based on the trigger history. |

## `SELECT` examples

Gets a list of workflow trigger histories.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_trigger_histories', value: 'view', },
        { label: 'workflow_trigger_histories', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
code,
correlation,
end_time,
error,
fired,
historyName,
inputs_link,
outputs_link,
resourceGroupName,
run,
scheduled_time,
start_time,
status,
subscriptionId,
tracking_id,
triggerName,
type,
workflowName
FROM azure.logic_apps.vw_workflow_trigger_histories
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND triggerName = '{{ triggerName }}'
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
FROM azure.logic_apps.workflow_trigger_histories
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND triggerName = '{{ triggerName }}'
AND workflowName = '{{ workflowName }}';
```
</TabItem></Tabs>

