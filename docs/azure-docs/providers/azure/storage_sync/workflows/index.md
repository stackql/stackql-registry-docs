---
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
  - storage_sync
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

Creates, updates, deletes, gets or lists a <code>workflows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.workflows" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflows', value: 'view', },
        { label: 'workflows', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="command_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_operation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_status_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_step_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="steps" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageSyncServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workflowId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Workflow Properties object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, workflowId" /> | Get Workflows resource |
| <CopyableCode code="list_by_storage_sync_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId" /> | Get a Workflow List |
| <CopyableCode code="abort" /> | `EXEC` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, workflowId" /> | Abort the given workflow. |

## `SELECT` examples

Get a Workflow List

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflows', value: 'view', },
        { label: 'workflows', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
command_name,
created_timestamp,
last_operation_id,
last_status_timestamp,
last_step_name,
operation,
resourceGroupName,
status,
steps,
storageSyncServiceName,
subscriptionId,
workflowId
FROM azure.storage_sync.vw_workflows
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.storage_sync.workflows
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageSyncServiceName = '{{ storageSyncServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

