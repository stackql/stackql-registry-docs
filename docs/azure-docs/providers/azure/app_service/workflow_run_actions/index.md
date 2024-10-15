---
title: workflow_run_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_actions
  - app_service
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

Creates, updates, deletes, gets or lists a <code>workflow_run_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_run_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.workflow_run_actions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_run_actions', value: 'view', },
        { label: 'workflow_run_actions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the workflow run action name. |
| <CopyableCode code="actionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="code" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="inputs_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="outputs_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retry_history" /> | `text` | field from the `properties` object |
| <CopyableCode code="runName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tracked_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="tracking_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the workflow run action type. |
| <CopyableCode code="workflowName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the workflow run action name. |
| <CopyableCode code="properties" /> | `object` | The workflow run action properties. |
| <CopyableCode code="type" /> | `string` | Gets the workflow run action type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionName, name, resourceGroupName, runName, subscriptionId, workflowName" /> | Gets a workflow run action. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, runName, subscriptionId, workflowName" /> | Gets a list of workflow run actions. |

## `SELECT` examples

Gets a list of workflow run actions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_run_actions', value: 'view', },
        { label: 'workflow_run_actions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
actionName,
code,
correlation,
end_time,
error,
inputs_link,
outputs_link,
resourceGroupName,
retry_history,
runName,
start_time,
status,
subscriptionId,
tracked_properties,
tracking_id,
type,
workflowName
FROM azure.app_service.vw_workflow_run_actions
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runName = '{{ runName }}'
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
FROM azure.app_service.workflow_run_actions
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runName = '{{ runName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```
</TabItem></Tabs>

