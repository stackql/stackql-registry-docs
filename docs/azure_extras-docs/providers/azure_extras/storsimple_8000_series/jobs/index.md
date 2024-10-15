---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - storsimple_8000_series
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.jobs" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The name of the object. |
| <CopyableCode code="backup_point_in_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_stats" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_label" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | The job error details. Contains list of job error items. |
| <CopyableCode code="is_cancellable" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_stages" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_complete" /> | `integer` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_device_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | The current status of the job. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="endTime" /> | `string` | The UTC time at which the job completed. |
| <CopyableCode code="error" /> | `object` | The job error details. Contains list of job error items. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="percentComplete" /> | `integer` | The percentage of the job that is already complete. |
| <CopyableCode code="properties" /> | `object` | The properties of the job. |
| <CopyableCode code="startTime" /> | `string` | The UTC time at which the job was started. |
| <CopyableCode code="status" /> | `string` | The current status of the job. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, jobName, managerName, resourceGroupName, subscriptionId" /> | Gets the details of the specified job name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets all the jobs for specified device. With optional OData query parameters, a filtered set of jobs is returned. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Gets all the jobs for the specified manager. With optional OData query parameters, a filtered set of jobs is returned. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="deviceName, jobName, managerName, resourceGroupName, subscriptionId" /> | Cancels a job on the device. |

## `SELECT` examples

Gets all the jobs for the specified manager. With optional OData query parameters, a filtered set of jobs is returned.

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
backup_type,
data_stats,
deviceName,
device_id,
end_time,
entity_label,
entity_type,
error,
is_cancellable,
jobName,
job_stages,
job_type,
kind,
managerName,
percent_complete,
resourceGroupName,
source_device_id,
start_time,
status,
subscriptionId,
type
FROM azure_extras.storsimple_8000_series.vw_jobs
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
kind,
percentComplete,
properties,
startTime,
status,
type
FROM azure_extras.storsimple_8000_series.jobs
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

