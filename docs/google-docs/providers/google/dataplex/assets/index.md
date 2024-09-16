---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - dataplex
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

Creates, updates, deletes, gets or lists a <code>assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.assets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the asset, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the asset. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the asset was created. |
| <CopyableCode code="discoverySpec" /> | `object` | Settings to manage the metadata discovery and publishing for an asset. |
| <CopyableCode code="discoveryStatus" /> | `object` | Status of discovery for an asset. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="labels" /> | `object` | Optional. User defined labels for the asset. |
| <CopyableCode code="resourceSpec" /> | `object` | Identifies the cloud resource that is referenced by this asset. |
| <CopyableCode code="resourceStatus" /> | `object` | Status of the resource referenced by an asset. |
| <CopyableCode code="securityStatus" /> | `object` | Security policy status of the asset. Data security policy, i.e., readers, writers & owners, should be specified in the lake/zone/asset IAM policy. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the asset. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the asset was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_zones_assets_get" /> | `SELECT` | <CopyableCode code="assetsId, lakesId, locationsId, projectsId, zonesId" /> | Retrieves an asset resource. |
| <CopyableCode code="projects_locations_lakes_zones_assets_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | Lists asset resources in a zone. |
| <CopyableCode code="projects_locations_lakes_zones_assets_create" /> | `INSERT` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | Creates an asset resource. |
| <CopyableCode code="projects_locations_lakes_zones_assets_delete" /> | `DELETE` | <CopyableCode code="assetsId, lakesId, locationsId, projectsId, zonesId" /> | Deletes an asset resource. The referenced storage resource is detached (default) or deleted based on the associated Lifecycle policy. |
| <CopyableCode code="projects_locations_lakes_zones_assets_patch" /> | `UPDATE` | <CopyableCode code="assetsId, lakesId, locationsId, projectsId, zonesId" /> | Updates an asset resource. |

## `SELECT` examples

Lists asset resources in a zone.

```sql
SELECT
name,
description,
createTime,
discoverySpec,
discoveryStatus,
displayName,
labels,
resourceSpec,
resourceStatus,
securityStatus,
state,
uid,
updateTime
FROM google.dataplex.assets
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assets</code> resource.

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
INSERT INTO google.dataplex.assets (
lakesId,
locationsId,
projectsId,
zonesId,
name,
displayName,
uid,
createTime,
updateTime,
labels,
description,
state,
resourceSpec,
resourceStatus,
securityStatus,
discoverySpec,
discoveryStatus
)
SELECT 
'{{ lakesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ zonesId }}',
'{{ name }}',
'{{ displayName }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ state }}',
'{{ resourceSpec }}',
'{{ resourceStatus }}',
'{{ securityStatus }}',
'{{ discoverySpec }}',
'{{ discoveryStatus }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: uid
      value: '{{ uid }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: description
      value: '{{ description }}'
    - name: state
      value: '{{ state }}'
    - name: resourceSpec
      value: '{{ resourceSpec }}'
    - name: resourceStatus
      value: '{{ resourceStatus }}'
    - name: securityStatus
      value: '{{ securityStatus }}'
    - name: discoverySpec
      value: '{{ discoverySpec }}'
    - name: discoveryStatus
      value: '{{ discoveryStatus }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>assets</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.assets
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
state = '{{ state }}',
resourceSpec = '{{ resourceSpec }}',
resourceStatus = '{{ resourceStatus }}',
securityStatus = '{{ securityStatus }}',
discoverySpec = '{{ discoverySpec }}',
discoveryStatus = '{{ discoveryStatus }}'
WHERE 
assetsId = '{{ assetsId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}';
```

## `DELETE` example

Deletes the specified <code>assets</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.assets
WHERE assetsId = '{{ assetsId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}';
```
