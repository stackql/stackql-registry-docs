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
uid,
description,
annotations,
labels,
abandoned,
createTime,
renderStartTime,
renderEndTime,
skaffoldConfigUri,
skaffoldConfigPath,
buildArtifacts,
deliveryPipelineSnapshot,
targetSnapshots,
customTargetTypeSnapshots,
renderState,
etag,
skaffoldVersion,
targetArtifacts,
targetRenders,
condition,
deployParameters
)
SELECT 
'{{ deliveryPipelinesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ uid }}',
'{{ description }}',
'{{ annotations }}',
'{{ labels }}',
true|false,
'{{ createTime }}',
'{{ renderStartTime }}',
'{{ renderEndTime }}',
'{{ skaffoldConfigUri }}',
'{{ skaffoldConfigPath }}',
'{{ buildArtifacts }}',
'{{ deliveryPipelineSnapshot }}',
'{{ targetSnapshots }}',
'{{ customTargetTypeSnapshots }}',
'{{ renderState }}',
'{{ etag }}',
'{{ skaffoldVersion }}',
'{{ targetArtifacts }}',
'{{ targetRenders }}',
'{{ condition }}',
'{{ deployParameters }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: uid
      value: '{{ uid }}'
    - name: description
      value: '{{ description }}'
    - name: annotations
      value: '{{ annotations }}'
    - name: labels
      value: '{{ labels }}'
    - name: abandoned
      value: '{{ abandoned }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: renderStartTime
      value: '{{ renderStartTime }}'
    - name: renderEndTime
      value: '{{ renderEndTime }}'
    - name: skaffoldConfigUri
      value: '{{ skaffoldConfigUri }}'
    - name: skaffoldConfigPath
      value: '{{ skaffoldConfigPath }}'
    - name: buildArtifacts
      value: '{{ buildArtifacts }}'
    - name: deliveryPipelineSnapshot
      value: '{{ deliveryPipelineSnapshot }}'
    - name: targetSnapshots
      value: '{{ targetSnapshots }}'
    - name: customTargetTypeSnapshots
      value: '{{ customTargetTypeSnapshots }}'
    - name: renderState
      value: '{{ renderState }}'
    - name: etag
      value: '{{ etag }}'
    - name: skaffoldVersion
      value: '{{ skaffoldVersion }}'
    - name: targetArtifacts
      value: '{{ targetArtifacts }}'
    - name: targetRenders
      value: '{{ targetRenders }}'
    - name: condition
      value: '{{ condition }}'
    - name: deployParameters
      value: '{{ deployParameters }}'

```
</TabItem>
</Tabs>
