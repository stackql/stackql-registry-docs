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
studySpec,
displayName
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ studySpec }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: inactiveReason
      value: string
    - name: state
      value: string
    - name: studySpec
      value:
        - name: parameters
          value:
            - - name: discreteValueSpec
                value:
                  - name: values
                    value:
                      - number
                  - name: defaultValue
                    value: number
              - name: categoricalValueSpec
                value:
                  - name: defaultValue
                    value: string
                  - name: values
                    value:
                      - string
              - name: conditionalParameterSpecs
                value:
                  - - name: parentCategoricalValues
                      value:
                        - name: values
                          value:
                            - string
                    - name: parentDiscreteValues
                      value:
                        - name: values
                          value:
                            - number
                    - name: parameterSpec
                      value:
                        - name: conditionalParameterSpecs
                          value:
                            - - name: parentIntValues
                                value:
                                  - name: values
                                    value:
                                      - string
                        - name: scaleType
                          value: string
                        - name: integerValueSpec
                          value:
                            - name: maxValue
                              value: string
                            - name: defaultValue
                              value: string
                            - name: minValue
                              value: string
                        - name: parameterId
                          value: string
                        - name: doubleValueSpec
                          value:
                            - name: defaultValue
                              value: number
                            - name: maxValue
                              value: number
                            - name: minValue
                              value: number
              - name: scaleType
                value: string
              - name: parameterId
                value: string
        - name: decayCurveStoppingSpec
          value:
            - name: useElapsedDuration
              value: boolean
        - name: observationNoise
          value: string
        - name: measurementSelectionType
          value: string
        - name: medianAutomatedStoppingSpec
          value:
            - name: useElapsedDuration
              value: boolean
        - name: convexAutomatedStoppingSpec
          value:
            - name: maxStepCount
              value: string
            - name: updateAllStoppedTrials
              value: boolean
            - name: minStepCount
              value: string
            - name: learningRateParameterName
              value: string
            - name: useElapsedDuration
              value: boolean
            - name: minMeasurementCount
              value: string
        - name: metrics
          value:
            - - name: goal
                value: string
              - name: metricId
                value: string
              - name: safetyConfig
                value:
                  - name: desiredMinSafeTrialsFraction
                    value: number
                  - name: safetyThreshold
                    value: number
        - name: studyStoppingConfig
          value:
            - name: maxNumTrials
              value: integer
            - name: maxNumTrialsNoProgress
              value: integer
            - name: shouldStopAsap
              value: boolean
            - name: maximumRuntimeConstraint
              value:
                - name: maxDuration
                  value: string
                - name: endTime
                  value: string
            - name: minNumTrials
              value: integer
            - name: maxDurationNoProgress
              value: string
        - name: algorithm
          value: string
    - name: displayName
      value: string
    - name: createTime
      value: string

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
