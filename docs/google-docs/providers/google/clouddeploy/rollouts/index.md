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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | Optional. Name of the `Rollout`. Format is projects/&#123;project&#125;/ locations/&#123;location&#125;/deliveryPipelines/&#123;deliveryPipeline&#125;/ releases/&#123;release&#125;/rollouts/a-z&#123;0,62&#125;. |
| `description` | `string` | Description of the `Rollout` for user purposes. Max length is 255 characters. |
| `failureReason` | `string` | Output only. Additional information about the rollout failure, if available. |
| `uid` | `string` | Output only. Unique identifier of the `Rollout`. |
| `approveTime` | `string` | Output only. Time at which the `Rollout` was approved. |
| `metadata` | `object` | Metadata includes information associated with a `Rollout`. |
| `deployStartTime` | `string` | Output only. Time at which the `Rollout` started deploying. |
| `enqueueTime` | `string` | Output only. Time at which the `Rollout` was enqueued. |
| `labels` | `object` | Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;= 128 bytes. |
| `state` | `string` | Output only. Current state of the `Rollout`. |
| `phases` | `array` | Output only. The phases that represent the workflows of this `Rollout`. |
| `annotations` | `object` | User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| `deployFailureCause` | `string` | Output only. The reason this rollout failed. This will always be unspecified while the rollout is in progress. |
| `controllerRollout` | `string` | Output only. Name of the `ControllerRollout`. Format is projects/&#123;project&#125;/ locations/&#123;location&#125;/deliveryPipelines/&#123;deliveryPipeline&#125;/ releases/&#123;release&#125;/rollouts/a-z&#123;0,62&#125;. |
| `targetId` | `string` | Required. The ID of Target to which this `Rollout` is deploying. |
| `approvalState` | `string` | Output only. Approval state of the `Rollout`. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `deployingBuild` | `string` | Output only. The resource name of the Cloud Build `Build` object that is used to deploy the Rollout. Format is `projects/&#123;project&#125;/locations/&#123;location&#125;/builds/&#123;build&#125;`. |
| `createTime` | `string` | Output only. Time at which the `Rollout` was created. |
| `deployEndTime` | `string` | Output only. Time at which the `Rollout` finished deploying. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Gets details of a single Rollout. |
| `list` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Lists Rollouts in a given project and location. |
| `create` | `INSERT` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Creates a new Rollout in a given project and location. |
| `_list` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Lists Rollouts in a given project and location. |
| `advance` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Advances a Rollout in a given project and location. |
| `approve` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Approves a Rollout. |
| `cancel` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Cancels a Rollout in a given project and location. |
| `ignore_job` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Ignores the specified Job in a Rollout. |
| `retry_job` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Retries the specified Job in a Rollout. |
