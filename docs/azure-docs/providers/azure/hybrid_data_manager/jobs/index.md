---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - hybrid_data_manager
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.jobs" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Id of the object. |
| <CopyableCode code="name" /> | `text` | Name of the object. |
| <CopyableCode code="bytes_processed" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_sink_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | Top level error for the job. |
| <CopyableCode code="is_cancellable" /> | `text` | field from the `properties` object |
| <CopyableCode code="items_processed" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | Status of the job. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_bytes_to_process" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_items_to_process" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="endTime" /> | `string` | Time at which the job ended in UTC ISO 8601 format. |
| <CopyableCode code="error" /> | `object` | Top level error for the job. |
| <CopyableCode code="properties" /> | `object` | Job Properties |
| <CopyableCode code="startTime" /> | `string` | Time at which the job was started in UTC ISO 8601 format. |
| <CopyableCode code="status" /> | `string` | Status of the job. |
| <CopyableCode code="type" /> | `string` | Type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId" /> | This method gets a data manager job given the jobId. |
| <CopyableCode code="list_by_data_manager" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | This method gets all the jobs at the data manager resource level. |
| <CopyableCode code="list_by_data_service" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, resourceGroupName, subscriptionId" /> | This method gets all the jobs of a data service type in a given resource. |
| <CopyableCode code="list_by_job_definition" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId" /> | This method gets all the jobs of a given job definition. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId" /> | Cancels the given job. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId" /> | Resumes the given job. |

## `SELECT` examples

This method gets all the jobs at the data manager resource level.

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
bytes_processed,
dataManagerName,
dataServiceName,
data_sink_name,
data_source_name,
details,
end_time,
error,
is_cancellable,
items_processed,
jobDefinitionName,
jobId,
resourceGroupName,
start_time,
status,
subscriptionId,
total_bytes_to_process,
total_items_to_process,
type
FROM azure.hybrid_data_manager.vw_jobs
WHERE dataManagerName = '{{ dataManagerName }}'
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
properties,
startTime,
status,
type
FROM azure.hybrid_data_manager.jobs
WHERE dataManagerName = '{{ dataManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

