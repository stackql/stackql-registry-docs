---
title: delivery_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_pipelines
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

Creates, updates, deletes, gets or lists a <code>delivery_pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouddeploy.delivery_pipelines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. Name of the `DeliveryPipeline`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}`. The `deliveryPipeline` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?` |
| <CopyableCode code="description" /> | `string` | Description of the `DeliveryPipeline`. Max length is 255 characters. |
| <CopyableCode code="annotations" /> | `object` | User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. |
| <CopyableCode code="condition" /> | `object` | PipelineCondition contains all conditions relevant to a Delivery Pipeline. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the pipeline was created. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes. |
| <CopyableCode code="serialPipeline" /> | `object` | SerialPipeline defines a sequential set of stages for a `DeliveryPipeline`. |
| <CopyableCode code="suspended" /> | `boolean` | When suspended, no new releases or rollouts can be created, but in-progress ones will complete. |
| <CopyableCode code="uid" /> | `string` | Output only. Unique identifier of the `DeliveryPipeline`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Most recent time at which the pipeline was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Gets details of a single DeliveryPipeline. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DeliveryPipelines in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new DeliveryPipeline in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Deletes a single DeliveryPipeline. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Updates the parameters of a single DeliveryPipeline. |
| <CopyableCode code="rollback_target" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Creates a `Rollout` to roll back the specified target. |

## `SELECT` examples

Lists DeliveryPipelines in a given project and location.

```sql
SELECT
name,
description,
annotations,
condition,
createTime,
etag,
labels,
serialPipeline,
suspended,
uid,
updateTime
FROM google.clouddeploy.delivery_pipelines
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>delivery_pipelines</code> resource.

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
INSERT INTO google.clouddeploy.delivery_pipelines (
locationsId,
projectsId,
name,
description,
annotations,
labels,
serialPipeline,
etag,
suspended
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ annotations }}',
'{{ labels }}',
'{{ serialPipeline }}',
'{{ etag }}',
{{ suspended }}
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
    - name: updateTime
      value: string
    - name: serialPipeline
      value:
        - name: stages
          value:
            - - name: targetId
                value: string
              - name: profiles
                value:
                  - string
              - name: strategy
                value:
                  - name: standard
                    value:
                      - name: verify
                        value: boolean
                      - name: predeploy
                        value:
                          - name: actions
                            value:
                              - string
                      - name: postdeploy
                        value:
                          - name: actions
                            value:
                              - string
                  - name: canary
                    value:
                      - name: runtimeConfig
                        value:
                          - name: kubernetes
                            value:
                              - name: gatewayServiceMesh
                                value:
                                  - name: httpRoute
                                    value: string
                                  - name: service
                                    value: string
                                  - name: deployment
                                    value: string
                                  - name: routeUpdateWaitTime
                                    value: string
                                  - name: stableCutbackDuration
                                    value: string
                                  - name: podSelectorLabel
                                    value: string
                              - name: serviceNetworking
                                value:
                                  - name: service
                                    value: string
                                  - name: deployment
                                    value: string
                                  - name: disablePodOverprovisioning
                                    value: boolean
                                  - name: podSelectorLabel
                                    value: string
                          - name: cloudRun
                            value:
                              - name: automaticTrafficControl
                                value: boolean
                              - name: canaryRevisionTags
                                value:
                                  - string
                              - name: priorRevisionTags
                                value:
                                  - string
                              - name: stableRevisionTags
                                value:
                                  - string
                      - name: canaryDeployment
                        value:
                          - name: percentages
                            value:
                              - integer
                          - name: verify
                            value: boolean
                      - name: customCanaryDeployment
                        value:
                          - name: phaseConfigs
                            value:
                              - - name: phaseId
                                  value: string
                                - name: percentage
                                  value: integer
                                - name: profiles
                                  value:
                                    - string
                                - name: verify
                                  value: boolean
              - name: deployParameters
                value:
                  - - name: values
                      value: object
                    - name: matchTargetLabels
                      value: object
    - name: condition
      value:
        - name: pipelineReadyCondition
          value:
            - name: status
              value: boolean
            - name: updateTime
              value: string
        - name: targetsPresentCondition
          value:
            - name: status
              value: boolean
            - name: missingTargets
              value:
                - string
            - name: updateTime
              value: string
        - name: targetsTypeCondition
          value:
            - name: status
              value: boolean
            - name: errorDetails
              value: string
    - name: etag
      value: string
    - name: suspended
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>delivery_pipelines</code> resource.

```sql
/*+ update */
UPDATE google.clouddeploy.delivery_pipelines
SET 
name = '{{ name }}',
description = '{{ description }}',
annotations = '{{ annotations }}',
labels = '{{ labels }}',
serialPipeline = '{{ serialPipeline }}',
etag = '{{ etag }}',
suspended = true|false
WHERE 
deliveryPipelinesId = '{{ deliveryPipelinesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>delivery_pipelines</code> resource.

```sql
/*+ delete */
DELETE FROM google.clouddeploy.delivery_pipelines
WHERE deliveryPipelinesId = '{{ deliveryPipelinesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
