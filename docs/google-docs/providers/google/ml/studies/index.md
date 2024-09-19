---
title: studies
hide_title: false
hide_table_of_contents: false
keywords:
  - studies
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

Creates, updates, deletes, gets or lists a <code>studies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.studies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of a study. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the study was created. |
| <CopyableCode code="inactiveReason" /> | `string` | Output only. A human readable reason why the Study is inactive. This should be empty if a study is ACTIVE or COMPLETED. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of a study. |
| <CopyableCode code="studyConfig" /> | `object` | Represents configuration of a study. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_studies_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Gets a study. |
| <CopyableCode code="projects_locations_studies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the studies in a region for an associated project. |
| <CopyableCode code="projects_locations_studies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a study. |
| <CopyableCode code="projects_locations_studies_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Deletes a study. |

## `SELECT` examples

Lists all the studies in a region for an associated project.

```sql
SELECT
name,
createTime,
inactiveReason,
state,
studyConfig
FROM google.ml.studies
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
INSERT INTO google.ml.studies (
locationsId,
projectsId,
studyConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ studyConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
studyConfig:
  metrics:
    - goal: string
      metric: string
  parameters:
    - parameter: string
      type: string
      doubleValueSpec:
        minValue: number
        maxValue: number
      integerValueSpec:
        minValue: string
        maxValue: string
      categoricalValueSpec:
        values:
          - type: string
      discreteValueSpec:
        values:
          - type: string
            format: string
      scaleType: string
      parentDiscreteValues:
        values:
          - type: string
            format: string
      parentIntValues:
        values:
          - type: string
            format: string
      parentCategoricalValues:
        values:
          - type: string
      childParameterSpecs:
        - parameter: string
          type: string
          scaleType: string
          childParameterSpecs:
            - parameter: string
              type: string
              scaleType: string
              childParameterSpecs:
                - parameter: string
                  type: string
                  scaleType: string
                  childParameterSpecs:
                    - parameter: string
                      type: string
                      scaleType: string
                      childParameterSpecs:
                        - parameter: string
                          type: string
                          scaleType: string
                          childParameterSpecs:
                            - parameter: string
                              type: string
                              scaleType: string
                              childParameterSpecs:
                                - parameter: string
                                  type: string
                                  scaleType: string
                                  childParameterSpecs:
                                    - parameter: string
                                      type: string
                                      scaleType: string
                                      childParameterSpecs:
                                        - {}
  algorithm: string
  automatedStoppingConfig:
    decayCurveStoppingConfig:
      useElapsedTime: boolean
    medianAutomatedStoppingConfig:
      useElapsedTime: boolean
state: string
createTime: string
inactiveReason: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>studies</code> resource.

```sql
/*+ delete */
DELETE FROM google.ml.studies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND studiesId = '{{ studiesId }}';
```
