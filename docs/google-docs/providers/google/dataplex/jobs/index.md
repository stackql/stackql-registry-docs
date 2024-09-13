---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - dataplex
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the job, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}/jobs/{job_id}. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time when the job ended. |
| <CopyableCode code="executionSpec" /> | `object` | Execution related settings, like retry and service_account. |
| <CopyableCode code="labels" /> | `object` | Output only. User-defined labels for the task. |
| <CopyableCode code="message" /> | `string` | Output only. Additional information about the current state. |
| <CopyableCode code="retryCount" /> | `integer` | Output only. The number of times the job has been retried (excluding the initial attempt). |
| <CopyableCode code="service" /> | `string` | Output only. The underlying service running a job. |
| <CopyableCode code="serviceJob" /> | `string` | Output only. The full resource name for the job run under a particular service. |
| <CopyableCode code="startTime" /> | `string` | Output only. The time when the job was started. |
| <CopyableCode code="state" /> | `string` | Output only. Execution state for the job. |
| <CopyableCode code="trigger" /> | `string` | Output only. Job execution trigger. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the job. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_data_scans_jobs_get" /> | `SELECT` | <CopyableCode code="dataScansId, jobsId, locationsId, projectsId" /> | Gets a DataScanJob resource. |
| <CopyableCode code="projects_locations_data_scans_jobs_list" /> | `SELECT` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Lists DataScanJobs under the given DataScan. |
| <CopyableCode code="projects_locations_lakes_tasks_jobs_get" /> | `SELECT` | <CopyableCode code="jobsId, lakesId, locationsId, projectsId, tasksId" /> | Get job resource. |
| <CopyableCode code="projects_locations_lakes_tasks_jobs_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId, tasksId" /> | Lists Jobs under the given task. |
| <CopyableCode code="projects_locations_data_scans_jobs_generate_data_quality_rules" /> | `EXEC` | <CopyableCode code="dataScansId, jobsId, locationsId, projectsId" /> | Generates recommended data quality rules based on the results of a data profiling scan.Use the recommendations to build rules for a data quality scan. |
| <CopyableCode code="projects_locations_lakes_tasks_jobs_cancel" /> | `EXEC` | <CopyableCode code="jobsId, lakesId, locationsId, projectsId, tasksId" /> | Cancel jobs running for the task resource. |

## `SELECT` examples

Lists DataScanJobs under the given DataScan.

```sql
SELECT
name,
endTime,
executionSpec,
labels,
message,
retryCount,
service,
serviceJob,
startTime,
state,
trigger,
uid
FROM google.dataplex.jobs
WHERE dataScansId = '{{ dataScansId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
