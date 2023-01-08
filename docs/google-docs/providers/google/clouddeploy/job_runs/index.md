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
| `deployJobRun` | `object` | DeployJobRun contains information specific to a deploy `JobRun`. |
| `state` | `string` | Output only. The current state of the `JobRun`. |
| `endTime` | `string` | Output only. Time at which the `JobRun` ended. |
| `startTime` | `string` | Output only. Time at which the `JobRun` was started. |
| `verifyJobRun` | `object` | VerifyJobRun contains information specific to a verify `JobRun`. |
| `createTime` | `string` | Output only. Time at which the `JobRun` was created. |
| `etag` | `string` | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `phaseId` | `string` | Output only. ID of the `Rollout` phase this `JobRun` belongs in. |
| `jobId` | `string` | Output only. ID of the `Rollout` job this `JobRun` corresponds to. |
| `uid` | `string` | Output only. Unique identifier of the `JobRun`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_deliveryPipelines_releases_rollouts_jobRuns_get` | `SELECT` | `deliveryPipelinesId, jobRunsId, locationsId, projectsId, releasesId, rolloutsId` | Gets details of a single JobRun. |
| `projects_locations_deliveryPipelines_releases_rollouts_jobRuns_list` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Lists JobRuns in a given project and location. |
