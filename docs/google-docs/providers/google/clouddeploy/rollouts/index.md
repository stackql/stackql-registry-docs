---
title: rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - rollouts
  - clouddeploy
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddeploy.rollouts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. Name of the `Rollout`. Format is projects/{project}/ locations/{location}/deliveryPipelines/{deliveryPipeline}/ releases/{release}/rollouts/a-z{0,62}. |
| `description` | `string` | Description of the `Rollout` for user purposes. Max length is 255 characters. |
| `annotations` | `object` | User annotations. These attributes can only be set and used by the user, and not by Google Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| `labels` | `object` | Labels are attributes that can be set and used by both the user and by Google Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;= 128 bytes. |
| `enqueueTime` | `string` | Output only. Time at which the `Rollout` was enqueued. |
| `failureReason` | `string` | Output only. Reason the build failed. Empty if the build succeeded. |
| `deployStartTime` | `string` | Output only. Time at which the `Rollout` started deploying. |
| `deployEndTime` | `string` | Output only. Time at which the `Rollout` finished deploying. |
| `deployFailureCause` | `string` | Output only. The reason this deploy failed. This will always be unspecified while the deploy in progress. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `createTime` | `string` | Output only. Time at which the `Rollout` was created. |
| `deployingBuild` | `string` | Output only. The resource name of the Cloud Build `Build` object that is used to deploy the Rollout. Format is `projects/{project}/locations/{location}/builds/{build}`. |
| `state` | `string` | Output only. Current state of the `Rollout`. |
| `uid` | `string` | Output only. Unique identifier of the `Rollout`. |
| `approvalState` | `string` | Output only. Approval state of the `Rollout`. |
| `targetId` | `string` | Required. The ID of Target to which this `Rollout` is deploying. |
| `approveTime` | `string` | Output only. Time at which the `Rollout` was approved. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_deliveryPipelines_releases_rollouts_get` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Gets details of a single Rollout. |
| `projects_locations_deliveryPipelines_releases_rollouts_list` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Lists Rollouts in a given project and location. |
| `projects_locations_deliveryPipelines_releases_rollouts_create` | `INSERT` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Creates a new Rollout in a given project and location. |
| `projects_locations_deliveryPipelines_releases_rollouts_approve` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Approves a Rollout. |
