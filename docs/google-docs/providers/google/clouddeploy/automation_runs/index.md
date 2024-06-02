---
title: automation_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - automation_runs
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
<tr><td><b>Name</b></td><td><code>automation_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="clouddeploy.automation_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the `AutomationRun`. Format is `projects/&#123;project&#125;/locations/&#123;location&#125;/deliveryPipelines/&#123;delivery_pipeline&#125;/automationRuns/&#123;automation_run&#125;`. |
| <CopyableCode code="advanceRolloutOperation" /> | `object` | Contains the information of an automated advance-rollout operation. |
| <CopyableCode code="automationId" /> | `string` | Output only. The ID of the automation that initiated the operation. |
| <CopyableCode code="automationSnapshot" /> | `object` | An `Automation` resource in the Cloud Deploy API. An `Automation` enables the automation of manually driven actions for a Delivery Pipeline, which includes Release promotion among Targets, Rollout repair and Rollout deployment strategy advancement. The intention of Automation is to reduce manual intervention in the continuous delivery process. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the `AutomationRun` was created. |
| <CopyableCode code="etag" /> | `string` | Output only. The weak etag of the `AutomationRun` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="expireTime" /> | `string` | Output only. Time the `AutomationRun` expires. An `AutomationRun` expires after 14 days from its creation date. |
| <CopyableCode code="promoteReleaseOperation" /> | `object` | Contains the information of an automated promote-release operation. |
| <CopyableCode code="repairRolloutOperation" /> | `object` | Contains the information for an automated `repair rollout` operation. |
| <CopyableCode code="ruleId" /> | `string` | Output only. The ID of the automation rule that initiated the operation. |
| <CopyableCode code="serviceAccount" /> | `string` | Output only. Email address of the user-managed IAM service account that performs the operations against Cloud Deploy resources. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the `AutomationRun`. |
| <CopyableCode code="stateDescription" /> | `string` | Output only. Explains the current state of the `AutomationRun`. Present only when an explanation is needed. |
| <CopyableCode code="targetId" /> | `string` | Output only. The ID of the target that represents the promotion stage that initiates the `AutomationRun`. The value of this field is the last segment of a target name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time at which the automationRun was updated. |
| <CopyableCode code="waitUntilTime" /> | `string` | Output only. Earliest time the `AutomationRun` will attempt to resume. Wait-time is configured by `wait` in automation rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationRunsId, deliveryPipelinesId, locationsId, projectsId" /> | Gets details of a single AutomationRun. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Lists AutomationRuns in a given project and location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Lists AutomationRuns in a given project and location. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="automationRunsId, deliveryPipelinesId, locationsId, projectsId" /> | Cancels an AutomationRun. The `state` of the `AutomationRun` after cancelling is `CANCELLED`. `CancelAutomationRun` can be called on AutomationRun in the state `IN_PROGRESS` and `PENDING`; AutomationRun in a different state returns an `FAILED_PRECONDITION` error. |
