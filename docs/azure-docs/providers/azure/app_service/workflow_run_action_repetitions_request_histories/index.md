---
title: workflow_run_action_repetitions_request_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_action_repetitions_request_histories
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

Creates, updates, deletes, gets or lists a <code>workflow_run_action_repetitions_request_histories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_run_action_repetitions_request_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.workflow_run_action_repetitions_request_histories" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_run_action_repetitions_request_histories', value: 'view', },
        { label: 'workflow_run_action_repetitions_request_histories', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="actionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="repetitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="request" /> | `text` | field from the `properties` object |
| <CopyableCode code="requestHistoryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="response" /> | `text` | field from the `properties` object |
| <CopyableCode code="runName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
| <CopyableCode code="workflowName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The request history. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionName, name, repetitionName, requestHistoryName, resourceGroupName, runName, subscriptionId, workflowName" /> | Gets a workflow run repetition request history. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="actionName, name, repetitionName, resourceGroupName, runName, subscriptionId, workflowName" /> | List a workflow run repetition request history. |

## `SELECT` examples

List a workflow run repetition request history.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_run_action_repetitions_request_histories', value: 'view', },
        { label: 'workflow_run_action_repetitions_request_histories', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
actionName,
end_time,
location,
repetitionName,
request,
requestHistoryName,
resourceGroupName,
response,
runName,
start_time,
subscriptionId,
tags,
type,
workflowName
FROM azure.app_service.vw_workflow_run_action_repetitions_request_histories
WHERE actionName = '{{ actionName }}'
AND name = '{{ name }}'
AND repetitionName = '{{ repetitionName }}'
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
FROM azure.app_service.workflow_run_action_repetitions_request_histories
WHERE actionName = '{{ actionName }}'
AND name = '{{ name }}'
AND repetitionName = '{{ repetitionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runName = '{{ runName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```
</TabItem></Tabs>

