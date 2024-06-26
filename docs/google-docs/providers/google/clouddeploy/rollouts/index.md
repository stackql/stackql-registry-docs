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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouddeploy.rollouts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. Name of the `Rollout`. Format is `projects/&#123;project&#125;/locations/&#123;location&#125;/deliveryPipelines/&#123;deliveryPipeline&#125;/releases/&#123;release&#125;/rollouts/&#123;rollout&#125;`. The `rollout` component must match `[a-z]([a-z0-9-]&#123;0,61&#125;[a-z0-9])?` |
| <CopyableCode code="description" /> | `string` | Description of the `Rollout` for user purposes. Max length is 255 characters. |
| <CopyableCode code="annotations" /> | `object` | User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| <CopyableCode code="approvalState" /> | `string` | Output only. Approval state of the `Rollout`. |
| <CopyableCode code="approveTime" /> | `string` | Output only. Time at which the `Rollout` was approved. |
| <CopyableCode code="controllerRollout" /> | `string` | Output only. Name of the `ControllerRollout`. Format is `projects/&#123;project&#125;/locations/&#123;location&#125;/deliveryPipelines/&#123;deliveryPipeline&#125;/releases/&#123;release&#125;/rollouts/&#123;rollout&#125;`. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the `Rollout` was created. |
| <CopyableCode code="deployEndTime" /> | `string` | Output only. Time at which the `Rollout` finished deploying. |
| <CopyableCode code="deployFailureCause" /> | `string` | Output only. The reason this rollout failed. This will always be unspecified while the rollout is in progress. |
| <CopyableCode code="deployStartTime" /> | `string` | Output only. Time at which the `Rollout` started deploying. |
| <CopyableCode code="deployingBuild" /> | `string` | Output only. The resource name of the Cloud Build `Build` object that is used to deploy the Rollout. Format is `projects/&#123;project&#125;/locations/&#123;location&#125;/builds/&#123;build&#125;`. |
| <CopyableCode code="enqueueTime" /> | `string` | Output only. Time at which the `Rollout` was enqueued. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="failureReason" /> | `string` | Output only. Additional information about the rollout failure, if available. |
| <CopyableCode code="labels" /> | `object` | Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;= 128 bytes. |
| <CopyableCode code="metadata" /> | `object` | Metadata includes information associated with a `Rollout`. |
| <CopyableCode code="phases" /> | `array` | Output only. The phases that represent the workflows of this `Rollout`. |
| <CopyableCode code="rollbackOfRollout" /> | `string` | Output only. Name of the `Rollout` that is rolled back by this `Rollout`. Empty if this `Rollout` wasn't created as a rollback. |
| <CopyableCode code="rolledBackByRollouts" /> | `array` | Output only. Names of `Rollouts` that rolled back this `Rollout`. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the `Rollout`. |
| <CopyableCode code="targetId" /> | `string` | Required. The ID of Target to which this `Rollout` is deploying. |
| <CopyableCode code="uid" /> | `string` | Output only. Unique identifier of the `Rollout`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Gets details of a single Rollout. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId" /> | Lists Rollouts in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId" /> | Creates a new Rollout in a given project and location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId" /> | Lists Rollouts in a given project and location. |
| <CopyableCode code="advance" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Advances a Rollout in a given project and location. |
| <CopyableCode code="approve" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Approves a Rollout. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Cancels a Rollout in a given project and location. |
| <CopyableCode code="ignore_job" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Ignores the specified Job in a Rollout. |
| <CopyableCode code="retry_job" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Retries the specified Job in a Rollout. |
