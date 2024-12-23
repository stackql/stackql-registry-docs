---
title: trials
hide_title: false
hide_table_of_contents: false
keywords:
  - trials
  - aiplatform
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

Creates, updates, deletes, gets or lists a <code>trials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.trials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. The identifier of the Trial assigned by the service. |
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the Trial assigned by the service. |
| <CopyableCode code="clientId" /> | `string` | Output only. The identifier of the client that originally requested this Trial. Each client is identified by a unique client_id. When a client asks for a suggestion, Vertex AI Vizier will assign it a Trial. The client should evaluate the Trial, complete it, and report back to Vertex AI Vizier. If suggestion is asked again by same client_id before the Trial is completed, the same Trial will be returned. Multiple clients with different client_ids can ask for suggestions simultaneously, each of them will get their own Trial. |
| <CopyableCode code="customJob" /> | `string` | Output only. The CustomJob name linked to the Trial. It's set for a HyperparameterTuningJob's Trial. |
| <CopyableCode code="endTime" /> | `string` | Output only. Time when the Trial's status changed to `SUCCEEDED` or `INFEASIBLE`. |
| <CopyableCode code="finalMeasurement" /> | `object` | A message representing a Measurement of a Trial. A Measurement contains the Metrics got by executing a Trial using suggested hyperparameter values. |
| <CopyableCode code="infeasibleReason" /> | `string` | Output only. A human readable string describing why the Trial is infeasible. This is set only if Trial state is `INFEASIBLE`. |
| <CopyableCode code="measurements" /> | `array` | Output only. A list of measurements that are strictly lexicographically ordered by their induced tuples (steps, elapsed_duration). These are used for early stopping computations. |
| <CopyableCode code="parameters" /> | `array` | Output only. The parameters of the Trial. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time when the Trial was started. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of the Trial. |
| <CopyableCode code="webAccessUris" /> | `object` | Output only. URIs for accessing [interactive shells](https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell) (one URI for each training node). Only available if this trial is part of a HyperparameterTuningJob and the job's trial_job_spec.enable_web_access field is `true`. The keys are names of each node used for the trial; for example, `workerpool0-0` for the primary node, `workerpool1-0` for the first node in the second worker pool, and `workerpool1-1` for the second node in the second worker pool. The values are the URIs for each node's interactive shell. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Gets a Trial. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Lists the Trials associated with a Study. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Adds a user provided Trial to a Study. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Deletes a Trial. |
| <CopyableCode code="check_trial_early_stopping_state" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Checks whether a Trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse. |
| <CopyableCode code="complete" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Marks a Trial as complete. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Stops a Trial. |
| <CopyableCode code="suggest" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Adds one or more Trials to a Study, with parameter values suggested by Vertex AI Vizier. Returns a long-running operation associated with the generation of Trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse. |

## `SELECT` examples

Lists the Trials associated with a Study.

```sql
SELECT
id,
name,
clientId,
customJob,
endTime,
finalMeasurement,
infeasibleReason,
measurements,
parameters,
startTime,
state,
webAccessUris
FROM google.aiplatform.trials
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND studiesId = '{{ studiesId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trials</code> resource.

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
INSERT INTO google.aiplatform.trials (
locationsId,
projectsId,
studiesId
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ studiesId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: clientId
      value: string
    - name: name
      value: string
    - name: customJob
      value: string
    - name: finalMeasurement
      value:
        - name: stepCount
          value: string
        - name: elapsedDuration
          value: string
        - name: metrics
          value:
            - - name: value
                value: number
              - name: metricId
                value: string
    - name: startTime
      value: string
    - name: measurements
      value:
        - - name: stepCount
            value: string
          - name: elapsedDuration
            value: string
          - name: metrics
            value:
              - - name: value
                  value: number
                - name: metricId
                  value: string
    - name: state
      value: string
    - name: endTime
      value: string
    - name: webAccessUris
      value: object
    - name: parameters
      value:
        - - name: value
            value: any
          - name: parameterId
            value: string
    - name: infeasibleReason
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>trials</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.trials
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND studiesId = '{{ studiesId }}'
AND trialsId = '{{ trialsId }}';
```
