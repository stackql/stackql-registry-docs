---
title: workflow_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_triggers
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

Creates, updates, deletes, gets or lists a <code>workflow_triggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflow_triggers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_triggers', value: 'view', },
        { label: 'workflow_triggers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the workflow trigger name. |
| <CopyableCode code="changed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_execution_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_execution_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="recurrence" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="triggerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the workflow trigger type. |
| <CopyableCode code="workflow" /> | `text` | field from the `properties` object |
| <CopyableCode code="workflowName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the workflow trigger name. |
| <CopyableCode code="properties" /> | `object` | The workflow trigger properties. |
| <CopyableCode code="type" /> | `string` | Gets the workflow trigger type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, triggerName, workflowName" /> | Gets a workflow trigger. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Gets a list of workflow triggers. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, triggerName, workflowName" /> | Resets a workflow trigger. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, triggerName, workflowName" /> | Runs a workflow trigger. |
| <CopyableCode code="set_state" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, triggerName, workflowName, data__source" /> | Sets the state of a workflow trigger. |

## `SELECT` examples

Gets a list of workflow triggers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_triggers', value: 'view', },
        { label: 'workflow_triggers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
changed_time,
created_time,
last_execution_time,
next_execution_time,
provisioning_state,
recurrence,
resourceGroupName,
state,
status,
subscriptionId,
triggerName,
type,
workflow,
workflowName
FROM azure.logic_apps.vw_workflow_triggers
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
FROM azure.logic_apps.workflow_triggers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```
</TabItem></Tabs>

