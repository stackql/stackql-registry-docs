---
title: stages_execution_details
hide_title: false
hide_table_of_contents: false
keywords:
  - stages_execution_details
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

Creates, updates, deletes, gets or lists a <code>stages_execution_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stages_execution_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.stages_execution_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="workItems" /> | `array` | Work items processed by this worker, sorted by time. |
| <CopyableCode code="workerName" /> | `string` | Name of this worker |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_jobs_stages_get_execution_details" /> | `SELECT` | <CopyableCode code="jobId, location, projectId, stageId" /> | Request detailed information about the execution status of a stage of the job. EXPERIMENTAL. This API is subject to change or removal without notice. |

## `SELECT` examples

Request detailed information about the execution status of a stage of the job. EXPERIMENTAL. This API is subject to change or removal without notice.

```sql
SELECT
workItems,
workerName
FROM google.dataflow.stages_execution_details
WHERE jobId = '{{ jobId }}'
AND location = '{{ location }}'
AND projectId = '{{ projectId }}'
AND stageId = '{{ stageId }}';
```
