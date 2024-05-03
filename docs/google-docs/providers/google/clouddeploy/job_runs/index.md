---
title: job_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - job_runs
  - clouddeploy
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
<tr><td><b>Name</b></td><td><code>job_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouddeploy.job_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. Name of the `JobRun`. Format is projects/&#123;project&#125;/locations/&#123;location&#125;/ deliveryPipelines/&#123;deliveryPipeline&#125;/releases/&#123;releases&#125;/rollouts/ &#123;rollouts&#125;/jobRuns/&#123;uuid&#125;. |
| <CopyableCode code="advanceChildRolloutJobRun" /> | `object` | AdvanceChildRolloutJobRun contains information specific to a advanceChildRollout `JobRun`. |
| <CopyableCode code="createChildRolloutJobRun" /> | `object` | CreateChildRolloutJobRun contains information specific to a createChildRollout `JobRun`. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the `JobRun` was created. |
| <CopyableCode code="deployJobRun" /> | `object` | DeployJobRun contains information specific to a deploy `JobRun`. |
| <CopyableCode code="endTime" /> | `string` | Output only. Time at which the `JobRun` ended. |
| <CopyableCode code="etag" /> | `string` | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="jobId" /> | `string` | Output only. ID of the `Rollout` job this `JobRun` corresponds to. |
| <CopyableCode code="phaseId" /> | `string` | Output only. ID of the `Rollout` phase this `JobRun` belongs in. |
| <CopyableCode code="postdeployJobRun" /> | `object` | PostdeployJobRun contains information specific to a postdeploy `JobRun`. |
| <CopyableCode code="predeployJobRun" /> | `object` | PredeployJobRun contains information specific to a predeploy `JobRun`. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time at which the `JobRun` was started. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the `JobRun`. |
| <CopyableCode code="uid" /> | `string` | Output only. Unique identifier of the `JobRun`. |
| <CopyableCode code="verifyJobRun" /> | `object` | VerifyJobRun contains information specific to a verify `JobRun`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deliveryPipelinesId, jobRunsId, locationsId, projectsId, releasesId, rolloutsId" /> | Gets details of a single JobRun. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Lists JobRuns in a given project and location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Lists JobRuns in a given project and location. |
| <CopyableCode code="terminate" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, jobRunsId, locationsId, projectsId, releasesId, rolloutsId" /> | Terminates a Job Run in a given project and location. |
