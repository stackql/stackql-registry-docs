---
title: jobs_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_metrics
  - dataflow
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

Creates, updates, deletes, gets or lists a <code>jobs_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.jobs_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="metricTime" /> | `string` | Timestamp as of which metric values are current. |
| <CopyableCode code="metrics" /> | `array` | All metrics for this job. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_jobs_get_metrics" /> | `SELECT` | <CopyableCode code="jobId, projectId" /> | Request the job status. To request the status of a job, we recommend using `projects.locations.jobs.getMetrics` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.getMetrics` is not recommended, as you can only request the status of jobs that are running in `us-central1`. |
| <CopyableCode code="projects_locations_jobs_get_metrics" /> | `SELECT` | <CopyableCode code="jobId, location, projectId" /> | Request the job status. To request the status of a job, we recommend using `projects.locations.jobs.getMetrics` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.getMetrics` is not recommended, as you can only request the status of jobs that are running in `us-central1`. |

## `SELECT` examples

Request the job status. To request the status of a job, we recommend using `projects.locations.jobs.getMetrics` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.getMetrics` is not recommended, as you can only request the status of jobs that are running in `us-central1`.

```sql
SELECT
metricTime,
metrics
FROM google.dataflow.jobs_metrics
WHERE jobId = '{{ jobId }}'
AND projectId = '{{ projectId }}';
```
