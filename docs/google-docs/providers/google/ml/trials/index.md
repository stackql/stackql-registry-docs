---
title: trials
hide_title: false
hide_table_of_contents: false
keywords:
  - trials
  - ml
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.trials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the trial assigned by the service. |
| <CopyableCode code="clientId" /> | `string` | Output only. The identifier of the client that originally requested this trial. |
| <CopyableCode code="endTime" /> | `string` | Output only. Time at which the trial's status changed to COMPLETED. |
| <CopyableCode code="finalMeasurement" /> | `object` | A message representing a measurement. |
| <CopyableCode code="infeasibleReason" /> | `string` | Output only. A human readable string describing why the trial is infeasible. This should only be set if trial_infeasible is true. |
| <CopyableCode code="measurements" /> | `array` | A list of measurements that are strictly lexicographically ordered by their induced tuples (steps, elapsed_time). These are used for early stopping computations. |
| <CopyableCode code="parameters" /> | `array` | The parameters of the trial. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time at which the trial was started. |
| <CopyableCode code="state" /> | `string` | The detailed state of a trial. |
| <CopyableCode code="trialInfeasible" /> | `boolean` | Output only. If true, the parameters in this trial are not attempted again. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_studies_trials_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Gets a trial. |
| <CopyableCode code="projects_locations_studies_trials_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Lists the trials associated with a study. |
| <CopyableCode code="projects_locations_studies_trials_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Adds a user provided trial to a study. |
| <CopyableCode code="projects_locations_studies_trials_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Deletes a trial. |
| <CopyableCode code="projects_locations_studies_trials_check_early_stopping_state" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Checks whether a trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse. |
| <CopyableCode code="projects_locations_studies_trials_complete" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Marks a trial as complete. |
| <CopyableCode code="projects_locations_studies_trials_stop" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Stops a trial. |
| <CopyableCode code="projects_locations_studies_trials_suggest" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Adds one or more trials to a study, with parameter values suggested by AI Platform Vizier. Returns a long-running operation associated with the generation of trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse. |

## `SELECT` examples

Lists the trials associated with a study.

```sql
SELECT
name,
clientId,
endTime,
finalMeasurement,
infeasibleReason,
measurements,
parameters,
startTime,
state,
trialInfeasible
FROM google.ml.trials
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
INSERT INTO google.ml.trials (
locationsId,
projectsId,
studiesId,
state,
parameters,
finalMeasurement,
measurements
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ studiesId }}',
'{{ state }}',
'{{ parameters }}',
'{{ finalMeasurement }}',
'{{ measurements }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: state
      value: '{{ state }}'
    - name: parameters
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: finalMeasurement
      value:
        - name: elapsedTime
          value: '{{ elapsedTime }}'
        - name: stepCount
          value: '{{ stepCount }}'
        - name: metrics
          value:
            - name: $ref
              value: '{{ $ref }}'
    - name: measurements
      value:
        - name: $ref
          value: '{{ $ref }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>trials</code> resource.

```sql
/*+ delete */
DELETE FROM google.ml.trials
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND studiesId = '{{ studiesId }}'
AND trialsId = '{{ trialsId }}';
```
