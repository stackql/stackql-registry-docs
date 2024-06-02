---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - batch
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="batch.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Job name. For example: "projects/123456/locations/us-central1/jobs/job01". |
| <CopyableCode code="allocationPolicy" /> | `object` | A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job. |
| <CopyableCode code="createTime" /> | `string` | Output only. When the Job was created. |
| <CopyableCode code="labels" /> | `object` | Labels for the Job. Labels could be user provided or system generated. For example, "labels": &#123; "department": "finance", "environment": "test" &#125; You can assign up to 64 labels. [Google Compute Engine label restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) apply. Label names that start with "goog-" or "google-" are reserved. |
| <CopyableCode code="logsPolicy" /> | `object` | LogsPolicy describes how outputs from a Job's Tasks (stdout/stderr) will be preserved. |
| <CopyableCode code="notifications" /> | `array` | Notification configurations. |
| <CopyableCode code="priority" /> | `string` | Priority of the Job. The valid value range is [0, 100). Default value is 0. Higher value indicates higher priority. A job with higher priority value is more likely to run earlier if all other requirements are satisfied. |
| <CopyableCode code="status" /> | `object` | Job status. |
| <CopyableCode code="taskGroups" /> | `array` | Required. TaskGroups in the Job. Only one TaskGroup is supported now. |
| <CopyableCode code="uid" /> | `string` | Output only. A system generated unique ID for the Job. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last time the Job was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Get a Job specified by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List all Jobs for a project within a region. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a Job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Delete a Job. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List all Jobs for a project within a region. |
