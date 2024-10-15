---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="backup_point_in_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="download_progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | The job error information containing List of JobErrorItem. |
| <CopyableCode code="install_progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_cancellable" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_stages" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_complete" /> | `integer` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_device_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="stats" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | Current status of the job |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="endTime" /> | `string` | The UTC time at which the job completed |
| <CopyableCode code="error" /> | `object` | The job error information containing List of JobErrorItem. |
| <CopyableCode code="percentComplete" /> | `integer` | The percentage of the job that is already complete |
| <CopyableCode code="properties" /> | `object` | properties for the job |
| <CopyableCode code="startTime" /> | `string` | The UTC time at which the job was started |
| <CopyableCode code="status" /> | `string` | Current status of the job |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, jobName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified job name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the jobs in a device. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the jobs in a manager. |

## `SELECT` examples

Retrieves all the jobs in a manager.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backup_point_in_time,
deviceName,
device_id,
download_progress,
end_time,
entity_id,
entity_type,
error,
install_progress,
is_cancellable,
jobName,
job_stages,
job_type,
managerName,
percent_complete,
resourceGroupName,
source_device_id,
start_time,
stats,
status,
subscriptionId,
target_id,
target_type,
type
FROM azure_extras.storsimple_1200_series.vw_jobs
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
endTime,
error,
percentComplete,
properties,
startTime,
status,
type
FROM azure_extras.storsimple_1200_series.jobs
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

