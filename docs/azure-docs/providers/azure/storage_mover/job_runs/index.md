---
title: job_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - job_runs
  - storage_mover
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

Creates, updates, deletes, gets or lists a <code>job_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_mover.job_runs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_runs', value: 'view', },
        { label: 'job_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agent_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="bytes_excluded" /> | `text` | field from the `properties` object |
| <CopyableCode code="bytes_failed" /> | `text` | field from the `properties` object |
| <CopyableCode code="bytes_no_transfer_needed" /> | `text` | field from the `properties` object |
| <CopyableCode code="bytes_scanned" /> | `text` | field from the `properties` object |
| <CopyableCode code="bytes_transferred" /> | `text` | field from the `properties` object |
| <CopyableCode code="bytes_unsupported" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="execution_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="execution_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="items_excluded" /> | `text` | field from the `properties` object |
| <CopyableCode code="items_failed" /> | `text` | field from the `properties` object |
| <CopyableCode code="items_no_transfer_needed" /> | `text` | field from the `properties` object |
| <CopyableCode code="items_scanned" /> | `text` | field from the `properties` object |
| <CopyableCode code="items_transferred" /> | `text` | field from the `properties` object |
| <CopyableCode code="items_unsupported" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobRunName" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_definition_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_status_update" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scan_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageMoverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Job run properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobDefinitionName, jobRunName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Gets a Job Run resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Lists all Job Runs in a Job Definition. |

## `SELECT` examples

Lists all Job Runs in a Job Definition.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_runs', value: 'view', },
        { label: 'job_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
agent_name,
agent_resource_id,
bytes_excluded,
bytes_failed,
bytes_no_transfer_needed,
bytes_scanned,
bytes_transferred,
bytes_unsupported,
error,
execution_end_time,
execution_start_time,
items_excluded,
items_failed,
items_no_transfer_needed,
items_scanned,
items_transferred,
items_unsupported,
jobDefinitionName,
jobRunName,
job_definition_properties,
last_status_update,
projectName,
provisioning_state,
resourceGroupName,
scan_status,
source_name,
source_properties,
source_resource_id,
status,
storageMoverName,
subscriptionId,
system_data,
target_name,
target_properties,
target_resource_id
FROM azure.storage_mover.vw_job_runs
WHERE jobDefinitionName = '{{ jobDefinitionName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.storage_mover.job_runs
WHERE jobDefinitionName = '{{ jobDefinitionName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

