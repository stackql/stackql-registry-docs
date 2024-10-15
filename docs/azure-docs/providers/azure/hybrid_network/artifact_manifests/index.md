---
title: artifact_manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_manifests
  - hybrid_network
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

Creates, updates, deletes, gets or lists a <code>artifact_manifests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifact_manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.artifact_manifests" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_artifact_manifests', value: 'view', },
        { label: 'artifact_manifests', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="artifactManifestName" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifactStoreName" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifact_manifest_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifacts" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Artifact manifest properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifactManifestName, artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about a artifact manifest resource. |
| <CopyableCode code="list_by_artifact_store" /> | `SELECT` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about the artifact manifest. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="artifactManifestName, artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a artifact manifest. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="artifactManifestName, artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Deletes the specified artifact manifest. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="artifactManifestName, artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Updates a artifact manifest resource. |

## `SELECT` examples

Gets information about the artifact manifest.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_artifact_manifests', value: 'view', },
        { label: 'artifact_manifests', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
artifactManifestName,
artifactStoreName,
artifact_manifest_state,
artifacts,
location,
provisioning_state,
publisherName,
resourceGroupName,
subscriptionId,
tags
FROM azure.hybrid_network.vw_artifact_manifests
WHERE artifactStoreName = '{{ artifactStoreName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.hybrid_network.artifact_manifests
WHERE artifactStoreName = '{{ artifactStoreName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>artifact_manifests</code> resource.

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
INSERT INTO azure.hybrid_network.artifact_manifests (
artifactManifestName,
artifactStoreName,
publisherName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ artifactManifestName }}',
'{{ artifactStoreName }}',
'{{ publisherName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: artifactManifestState
          value: []
        - name: artifacts
          value:
            - - name: artifactName
                value: string
              - name: artifactType
                value: []
              - name: artifactVersion
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>artifact_manifests</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_network.artifact_manifests
SET 
tags = '{{ tags }}'
WHERE 
artifactManifestName = '{{ artifactManifestName }}'
AND artifactStoreName = '{{ artifactStoreName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>artifact_manifests</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_network.artifact_manifests
WHERE artifactManifestName = '{{ artifactManifestName }}'
AND artifactStoreName = '{{ artifactStoreName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
