---
title: studies
hide_title: false
hide_table_of_contents: false
keywords:
  - studies
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

Creates, updates, deletes, gets or lists a <code>studies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.studies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of a study. The study's globally unique identifier. Format: `projects/{project}/locations/{location}/studies/{study}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the study was created. |
| <CopyableCode code="displayName" /> | `string` | Required. Describes the Study, default value is empty string. |
| <CopyableCode code="inactiveReason" /> | `string` | Output only. A human readable reason why the Study is inactive. This should be empty if a study is ACTIVE or COMPLETED. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of a Study. |
| <CopyableCode code="studySpec" /> | `object` | Represents specification of a Study. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Gets a Study by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the studies in a region for an associated project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Study. A resource name will be generated after creation of the Study. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Deletes a Study. |
| <CopyableCode code="lookup" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Looks a study up using the user-defined display_name field instead of the fully qualified resource name. |

## `SELECT` examples

Lists all the studies in a region for an associated project.

```sql
SELECT
name,
createTime,
displayName,
inactiveReason,
state,
studySpec
FROM google.aiplatform.studies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>studies</code> resource.

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
INSERT INTO google.aiplatform.studies (
locationsId,
projectsId,
displayName,
studySpec
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ studySpec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: '{{ displayName }}'
    - name: studySpec
      value:
        - name: metrics
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: observationNoise
          value: '{{ observationNoise }}'
        - name: parameters
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: decayCurveStoppingSpec
          value:
            - name: useElapsedDuration
              value: '{{ useElapsedDuration }}'
        - name: convexAutomatedStoppingSpec
          value:
            - name: useElapsedDuration
              value: '{{ useElapsedDuration }}'
            - name: minStepCount
              value: '{{ minStepCount }}'
            - name: maxStepCount
              value: '{{ maxStepCount }}'
            - name: learningRateParameterName
              value: '{{ learningRateParameterName }}'
            - name: updateAllStoppedTrials
              value: '{{ updateAllStoppedTrials }}'
            - name: minMeasurementCount
              value: '{{ minMeasurementCount }}'
        - name: algorithm
          value: '{{ algorithm }}'
        - name: medianAutomatedStoppingSpec
          value:
            - name: useElapsedDuration
              value: '{{ useElapsedDuration }}'
        - name: measurementSelectionType
          value: '{{ measurementSelectionType }}'
        - name: studyStoppingConfig
          value:
            - name: minNumTrials
              value: '{{ minNumTrials }}'
            - name: shouldStopAsap
              value: '{{ shouldStopAsap }}'
            - name: maxNumTrialsNoProgress
              value: '{{ maxNumTrialsNoProgress }}'
            - name: maximumRuntimeConstraint
              value:
                - name: maxDuration
                  value: '{{ maxDuration }}'
                - name: endTime
                  value: '{{ endTime }}'
            - name: maxDurationNoProgress
              value: '{{ maxDurationNoProgress }}'
            - name: maxNumTrials
              value: '{{ maxNumTrials }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>studies</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.studies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND studiesId = '{{ studiesId }}';
```
