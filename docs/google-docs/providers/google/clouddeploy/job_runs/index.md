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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddeploy.job_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. Name of the `JobRun`. Format is projects/&#123;project&#125;/locations/&#123;location&#125;/ deliveryPipelines/&#123;deliveryPipeline&#125;/releases/&#123;releases&#125;/rollouts/ &#123;rollouts&#125;/jobRuns/&#123;uuid&#125;. |
| `createChildRolloutJobRun` | `object` | CreateChildRolloutJobRun contains information specific to a createChildRollout `JobRun`. |
| `startTime` | `string` | Output only. Time at which the `JobRun` was started. |
| `predeployJobRun` | `object` | PredeployJobRun contains information specific to a predeploy `JobRun`. |
| `verifyJobRun` | `object` | VerifyJobRun contains information specific to a verify `JobRun`. |
| `state` | `string` | Output only. The current state of the `JobRun`. |
| `jobId` | `string` | Output only. ID of the `Rollout` job this `JobRun` corresponds to. |
| `uid` | `string` | Output only. Unique identifier of the `JobRun`. |
| `postdeployJobRun` | `object` | PostdeployJobRun contains information specific to a postdeploy `JobRun`. |
| `createTime` | `string` | Output only. Time at which the `JobRun` was created. |
| `deployJobRun` | `object` | DeployJobRun contains information specific to a deploy `JobRun`. |
| `endTime` | `string` | Output only. Time at which the `JobRun` ended. |
| `advanceChildRolloutJobRun` | `object` | AdvanceChildRolloutJobRun contains information specific to a advanceChildRollout `JobRun`. |
| `phaseId` | `string` | Output only. ID of the `Rollout` phase this `JobRun` belongs in. |
| `etag` | `string` | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deliveryPipelinesId, jobRunsId, locationsId, projectsId, releasesId, rolloutsId` | Gets details of a single JobRun. |
| `list` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Lists JobRuns in a given project and location. |
| `_list` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Lists JobRuns in a given project and location. |
| `terminate` | `EXEC` | `deliveryPipelinesId, jobRunsId, locationsId, projectsId, releasesId, rolloutsId` | Terminates a Job Run in a given project and location. |
