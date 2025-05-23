---
title: workflow_run_action_repetitions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_action_repetitions
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

Creates, updates, deletes, gets or lists a <code>workflow_run_action_repetitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_run_action_repetitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.workflow_run_action_repetitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_run_action_repetitions', value: 'view', },
        { label: 'workflow_run_action_repetitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="actionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="inputs" /> | `text` | field from the `properties` object |
| <CopyableCode code="inputs_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="iteration_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="outputs" /> | `text` | field from the `properties` object |
| <CopyableCode code="outputs_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="repetitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="repetition_indexes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retry_history" /> | `text` | field from the `properties` object |
| <CopyableCode code="runName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="tracked_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="tracking_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
| <CopyableCode code="workflowName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The workflow run action repetition properties definition. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionName, name, repetitionName, resourceGroupName, runName, subscriptionId, workflowName" /> | Get a workflow run action repetition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="actionName, name, resourceGroupName, runName, subscriptionId, workflowName" /> | Get all of a workflow run action repetitions. |

## `SELECT` examples

Get all of a workflow run action repetitions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_run_action_repetitions', value: 'view', },
        { label: 'workflow_run_action_repetitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
actionName,
inputs,
inputs_link,
iteration_count,
location,
outputs,
outputs_link,
repetitionName,
repetition_indexes,
resourceGroupName,
retry_history,
runName,
subscriptionId,
tags,
tracked_properties,
tracking_id,
type,
workflowName
FROM azure.app_service.vw_workflow_run_action_repetitions
WHERE actionName = '{{ actionName }}'
AND name = '{{ name }}'
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
location,
properties,
tags,
type
FROM azure.app_service.workflow_run_action_repetitions
WHERE actionName = '{{ actionName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runName = '{{ runName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```
</TabItem></Tabs>

