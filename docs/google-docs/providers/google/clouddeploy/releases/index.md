---
title: releases
hide_title: false
hide_table_of_contents: false
keywords:
  - releases
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

Creates, updates, deletes, gets or lists a <code>releases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouddeploy.releases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. Name of the `Release`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}`. The `release` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?` |
| <CopyableCode code="description" /> | `string` | Description of the `Release`. Max length is 255 characters. |
| <CopyableCode code="abandoned" /> | `boolean` | Output only. Indicates whether this is an abandoned release. |
| <CopyableCode code="annotations" /> | `object` | User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| <CopyableCode code="buildArtifacts" /> | `array` | List of artifacts to pass through to Skaffold command. |
| <CopyableCode code="condition" /> | `object` | ReleaseCondition contains all conditions relevant to a Release. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the `Release` was created. |
| <CopyableCode code="customTargetTypeSnapshots" /> | `array` | Output only. Snapshot of the custom target types referenced by the targets taken at release creation time. |
| <CopyableCode code="deliveryPipelineSnapshot" /> | `object` | A `DeliveryPipeline` resource in the Cloud Deploy API. A `DeliveryPipeline` defines a pipeline through which a Skaffold configuration can progress. |
| <CopyableCode code="deployParameters" /> | `object` | Optional. The deploy parameters to use for all targets in this release. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes. |
| <CopyableCode code="renderEndTime" /> | `string` | Output only. Time at which the render completed. |
| <CopyableCode code="renderStartTime" /> | `string` | Output only. Time at which the render began. |
| <CopyableCode code="renderState" /> | `string` | Output only. Current state of the render operation. |
| <CopyableCode code="skaffoldConfigPath" /> | `string` | Filepath of the Skaffold config inside of the config URI. |
| <CopyableCode code="skaffoldConfigUri" /> | `string` | Cloud Storage URI of tar.gz archive containing Skaffold configuration. |
| <CopyableCode code="skaffoldVersion" /> | `string` | The Skaffold version to use when operating on this release, such as "1.20.0". Not all versions are valid; Cloud Deploy supports a specific set of versions. If unset, the most recent supported Skaffold version will be used. |
| <CopyableCode code="targetArtifacts" /> | `object` | Output only. Map from target ID to the target artifacts created during the render operation. |
| <CopyableCode code="targetRenders" /> | `object` | Output only. Map from target ID to details of the render operation for that target. |
| <CopyableCode code="targetSnapshots" /> | `array` | Output only. Snapshot of the targets taken at release creation time. |
| <CopyableCode code="uid" /> | `string` | Output only. Unique identifier of the `Release`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId" /> | Gets details of a single Release. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Lists Releases in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Creates a new Release in a given project and location. |
| <CopyableCode code="abandon" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId, releasesId" /> | Abandons a Release in the Delivery Pipeline. |

## `SELECT` examples

Lists Releases in a given project and location.

```sql
SELECT
name,
description,
abandoned,
annotations,
buildArtifacts,
condition,
createTime,
customTargetTypeSnapshots,
deliveryPipelineSnapshot,
deployParameters,
etag,
labels,
renderEndTime,
renderStartTime,
renderState,
skaffoldConfigPath,
skaffoldConfigUri,
skaffoldVersion,
targetArtifacts,
targetRenders,
targetSnapshots,
uid
FROM google.clouddeploy.releases
WHERE deliveryPipelinesId = '{{ deliveryPipelinesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>releases</code> resource.

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
INSERT INTO google.clouddeploy.releases (
deliveryPipelinesId,
locationsId,
projectsId,
name,
description,
annotations,
labels,
skaffoldConfigUri,
skaffoldConfigPath,
buildArtifacts,
etag,
skaffoldVersion,
deployParameters
)
SELECT 
'{{ deliveryPipelinesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ annotations }}',
'{{ labels }}',
'{{ skaffoldConfigUri }}',
'{{ skaffoldConfigPath }}',
'{{ buildArtifacts }}',
'{{ etag }}',
'{{ skaffoldVersion }}',
'{{ deployParameters }}'
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
    - name: abandoned
      value: boolean
    - name: createTime
      value: string
    - name: renderStartTime
      value: string
    - name: renderEndTime
      value: string
    - name: skaffoldConfigUri
      value: string
    - name: skaffoldConfigPath
      value: string
    - name: buildArtifacts
      value:
        - - name: image
            value: string
          - name: tag
            value: string
    - name: deliveryPipelineSnapshot
      value:
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
    - name: targetSnapshots
      value:
        - - name: name
            value: string
          - name: targetId
            value: string
          - name: uid
            value: string
          - name: description
            value: string
          - name: annotations
            value: object
          - name: labels
            value: object
          - name: requireApproval
            value: boolean
          - name: createTime
            value: string
          - name: updateTime
            value: string
          - name: gke
            value:
              - name: cluster
                value: string
              - name: internalIp
                value: boolean
              - name: proxyUrl
                value: string
          - name: anthosCluster
            value:
              - name: membership
                value: string
          - name: run
            value:
              - name: location
                value: string
          - name: multiTarget
            value:
              - name: targetIds
                value:
                  - string
          - name: customTarget
            value:
              - name: customTargetType
                value: string
          - name: etag
            value: string
          - name: executionConfigs
            value:
              - - name: usages
                  value:
                    - string
                - name: defaultPool
                  value:
                    - name: serviceAccount
                      value: string
                    - name: artifactStorage
                      value: string
                - name: privatePool
                  value:
                    - name: workerPool
                      value: string
                    - name: serviceAccount
                      value: string
                    - name: artifactStorage
                      value: string
                - name: workerPool
                  value: string
                - name: serviceAccount
                  value: string
                - name: artifactStorage
                  value: string
                - name: executionTimeout
                  value: string
                - name: verbose
                  value: boolean
          - name: deployParameters
            value: object
    - name: customTargetTypeSnapshots
      value:
        - - name: name
            value: string
          - name: customTargetTypeId
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
          - name: etag
            value: string
          - name: customActions
            value:
              - name: renderAction
                value: string
              - name: deployAction
                value: string
              - name: includeSkaffoldModules
                value:
                  - - name: configs
                      value:
                        - string
                    - name: git
                      value:
                        - name: repo
                          value: string
                        - name: path
                          value: string
                        - name: ref
                          value: string
                    - name: googleCloudStorage
                      value:
                        - name: source
                          value: string
                        - name: path
                          value: string
                    - name: googleCloudBuildRepo
                      value:
                        - name: repository
                          value: string
                        - name: path
                          value: string
                        - name: ref
                          value: string
    - name: renderState
      value: string
    - name: etag
      value: string
    - name: skaffoldVersion
      value: string
    - name: targetArtifacts
      value: object
    - name: targetRenders
      value: object
    - name: condition
      value:
        - name: releaseReadyCondition
          value:
            - name: status
              value: boolean
        - name: skaffoldSupportedCondition
          value:
            - name: status
              value: boolean
            - name: skaffoldSupportState
              value: string
            - name: maintenanceModeTime
              value: string
            - name: supportExpirationTime
              value: string
    - name: deployParameters
      value: object

```
</TabItem>
</Tabs>
