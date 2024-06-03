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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_jobs_stages_get_execution_details" /> | `SELECT` | <CopyableCode code="jobId, location, projectId, stageId" /> |
| <CopyableCode code="_projects_locations_jobs_stages_get_execution_details" /> | `EXEC` | <CopyableCode code="jobId, location, projectId, stageId" /> |
