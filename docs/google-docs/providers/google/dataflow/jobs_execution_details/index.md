---
title: jobs_execution_details
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_execution_details
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs_execution_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.jobs_execution_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endTime" /> | `string` | End time of this stage. If the work item is completed, this is the actual end time of the stage. Otherwise, it is the predicted end time. |
| <CopyableCode code="metrics" /> | `array` | Metrics for this stage. |
| <CopyableCode code="progress" /> | `object` | Information about the progress of some component of job execution. |
| <CopyableCode code="stageId" /> | `string` | ID of this stage |
| <CopyableCode code="startTime" /> | `string` | Start time of this stage. |
| <CopyableCode code="state" /> | `string` | State of this stage. |
| <CopyableCode code="stragglerSummary" /> | `object` | Summarized straggler identification details. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_jobs_get_execution_details" /> | `SELECT` | <CopyableCode code="jobId, location, projectId" /> |
| <CopyableCode code="_projects_locations_jobs_get_execution_details" /> | `EXEC` | <CopyableCode code="jobId, location, projectId" /> |
