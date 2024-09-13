---
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
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

Creates, updates, deletes or gets an <code>zone</code> resource or lists <code>zones</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the zone, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the zone. |
| <CopyableCode code="assetStatus" /> | `object` | Aggregated status of the underlying assets of a lake or zone. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the zone was created. |
| <CopyableCode code="discoverySpec" /> | `object` | Settings to manage the metadata discovery and publishing in a zone. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="labels" /> | `object` | Optional. User defined labels for the zone. |
| <CopyableCode code="resourceSpec" /> | `object` | Settings for resources attached as assets within a zone. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the zone. |
| <CopyableCode code="type" /> | `string` | Required. Immutable. The type of the zone. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the zone. This ID will be different if the zone is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the zone was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_zones_get" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | Retrieves a zone resource. |
| <CopyableCode code="projects_locations_lakes_zones_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Lists zone resources in a lake. |
| <CopyableCode code="projects_locations_lakes_zones_create" /> | `INSERT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Creates a zone resource within a lake. |
| <CopyableCode code="projects_locations_lakes_zones_delete" /> | `DELETE` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | Deletes a zone resource. All assets within a zone must be deleted before the zone can be deleted. |
| <CopyableCode code="projects_locations_lakes_zones_patch" /> | `UPDATE` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | Updates a zone resource. |

## `SELECT` examples

Lists zone resources in a lake.

```sql
SELECT
name,
description,
assetStatus,
createTime,
discoverySpec,
displayName,
labels,
resourceSpec,
state,
type,
uid,
updateTime
FROM google.dataplex.zones
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>zones</code> resource.

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
INSERT INTO google.dataplex.zones (
lakesId,
locationsId,
projectsId,
name,
displayName,
uid,
createTime,
updateTime,
labels,
description,
state,
type,
discoverySpec,
resourceSpec,
assetStatus
)
SELECT 
'{{ lakesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ state }}',
'{{ type }}',
'{{ discoverySpec }}',
'{{ resourceSpec }}',
'{{ assetStatus }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
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
      - name: type
        value: '{{ type }}'
      - name: discoverySpec
        value: '{{ discoverySpec }}'
      - name: resourceSpec
        value: '{{ resourceSpec }}'
      - name: assetStatus
        value: '{{ assetStatus }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a zone only if the necessary resources are available.

```sql
UPDATE google.dataplex.zones
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
state = '{{ state }}',
type = '{{ type }}',
discoverySpec = '{{ discoverySpec }}',
resourceSpec = '{{ resourceSpec }}',
assetStatus = '{{ assetStatus }}'
WHERE 
lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}';
```

## `DELETE` example

Deletes the specified zone resource.

```sql
DELETE FROM google.dataplex.zones
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}';
```
