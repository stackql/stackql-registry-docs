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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>rollouts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouddeploy.rollouts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. Name of the `Rollout`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. The `rollout` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?` |
| <CopyableCode code="description" /> | `string` | Description of the `Rollout` for user purposes. Max length is 255 characters. |
| <CopyableCode code="annotations" /> | `object` | User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| <CopyableCode code="approvalState" /> | `string` | Output only. Approval state of the `Rollout`. |
| <CopyableCode code="approveTime" /> | `string` | Output only. Time at which the `Rollout` was approved. |
| <CopyableCode code="controllerRollout" /> | `string` | Output only. Name of the `ControllerRollout`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the `Rollout` was created. |
| <CopyableCode code="deployEndTime" /> | `string` | Output only. Time at which the `Rollout` finished deploying. |
| <CopyableCode code="deployFailureCause" /> | `string` | Output only. The reason this rollout failed. This will always be unspecified while the rollout is in progress. |
| <CopyableCode code="deployStartTime" /> | `string` | Output only. Time at which the `Rollout` started deploying. |
| <CopyableCode code="deployingBuild" /> | `string` | Output only. The resource name of the Cloud Build `Build` object that is used to deploy the Rollout. Format is `projects/{project}/locations/{location}/builds/{build}`. |
| <CopyableCode code="enqueueTime" /> | `string` | Output only. Time at which the `Rollout` was enqueued. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="failureReason" /> | `string` | Output only. Additional information about the rollout failure, if available. |
| <CopyableCode code="labels" /> | `object` | Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes. |
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
| <CopyableCode code="advance" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Advances a Rollout in a given project and location. |
| <CopyableCode code="approve" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Approves a Rollout. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Cancels a Rollout in a given project and location. |
| <CopyableCode code="ignore_job" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Ignores the specified Job in a Rollout. |
| <CopyableCode code="retry_job" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId" /> | Retries the specified Job in a Rollout. |

## `SELECT` examples

Lists Rollouts in a given project and location.

```sql
SELECT
name,
description,
annotations,
approvalState,
approveTime,
controllerRollout,
createTime,
deployEndTime,
deployFailureCause,
deployStartTime,
deployingBuild,
enqueueTime,
etag,
failureReason,
labels,
metadata,
phases,
rollbackOfRollout,
rolledBackByRollouts,
state,
targetId,
uid
FROM google.clouddeploy.rollouts
WHERE deliveryPipelinesId = '{{ deliveryPipelinesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND releasesId = '{{ releasesId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rollouts</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.clouddeploy.rollouts (
deliveryPipelinesId,
locationsId,
projectsId,
releasesId,
name,
description,
annotations,
labels,
targetId,
etag
)
SELECT 
'{{ deliveryPipelinesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ releasesId }}',
'{{ name }}',
'{{ description }}',
'{{ annotations }}',
'{{ labels }}',
'{{ targetId }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: uid
      value: string
    - name: description
      value: string
    - name: annotations
      value: object
    - name: labels
      value: object
    - name: createTime
      value: string
    - name: approveTime
      value: string
    - name: enqueueTime
      value: string
    - name: deployStartTime
      value: string
    - name: deployEndTime
      value: string
    - name: targetId
      value: string
    - name: approvalState
      value: string
    - name: state
      value: string
    - name: failureReason
      value: string
    - name: deployingBuild
      value: string
    - name: etag
      value: string
    - name: deployFailureCause
      value: string
    - name: phases
      value:
        - - name: id
            value: string
          - name: state
            value: string
          - name: skipMessage
            value: string
          - name: deploymentJobs
            value:
              - name: deployJob
                value:
                  - name: id
                    value: string
                  - name: state
                    value: string
                  - name: skipMessage
                    value: string
                  - name: jobRun
                    value: string
                  - name: deployJob
                    value: []
                  - name: verifyJob
                    value: []
                  - name: predeployJob
                    value:
                      - name: actions
                        value:
                          - string
                  - name: postdeployJob
                    value:
                      - name: actions
                        value:
                          - string
                  - name: createChildRolloutJob
                    value: []
                  - name: advanceChildRolloutJob
                    value: []
          - name: childRolloutJobs
            value:
              - name: createRolloutJobs
                value:
                  - - name: id
                      value: string
                    - name: state
                      value: string
                    - name: skipMessage
                      value: string
                    - name: jobRun
                      value: string
              - name: advanceRolloutJobs
                value:
                  - - name: id
                      value: string
                    - name: state
                      value: string
                    - name: skipMessage
                      value: string
                    - name: jobRun
                      value: string
    - name: metadata
      value:
        - name: cloudRun
          value:
            - name: service
              value: string
            - name: serviceUrls
              value:
                - string
            - name: revision
              value: string
            - name: job
              value: string
        - name: automation
          value:
            - name: promoteAutomationRun
              value: string
            - name: advanceAutomationRuns
              value:
                - string
            - name: repairAutomationRuns
              value:
                - string
        - name: custom
          value:
            - name: values
              value: object
    - name: controllerRollout
      value: string
    - name: rollbackOfRollout
      value: string
    - name: rolledBackByRollouts
      value:
        - string

```
</TabItem>
</Tabs>
