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

Creates, updates, deletes, gets or lists a <code>zones</code> resource.

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
displayName,
labels,
description,
type,
discoverySpec,
resourceSpec
)
SELECT 
'{{ lakesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ labels }}',
'{{ description }}',
'{{ type }}',
'{{ discoverySpec }}',
'{{ resourceSpec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: uid
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: description
      value: string
    - name: state
      value: string
    - name: type
      value: string
    - name: discoverySpec
      value:
        - name: enabled
          value: boolean
        - name: includePatterns
          value:
            - string
        - name: excludePatterns
          value:
            - string
        - name: csvOptions
          value:
            - name: headerRows
              value: integer
            - name: delimiter
              value: string
            - name: encoding
              value: string
            - name: disableTypeInference
              value: boolean
        - name: jsonOptions
          value:
            - name: encoding
              value: string
            - name: disableTypeInference
              value: boolean
        - name: schedule
          value: string
    - name: resourceSpec
      value:
        - name: locationType
          value: string
    - name: assetStatus
      value:
        - name: updateTime
          value: string
        - name: activeAssets
          value: integer
        - name: securityPolicyApplyingAssets
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>zones</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.zones
SET 
displayName = '{{ displayName }}',
labels = '{{ labels }}',
description = '{{ description }}',
type = '{{ type }}',
discoverySpec = '{{ discoverySpec }}',
resourceSpec = '{{ resourceSpec }}'
WHERE 
lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}';
```

## `DELETE` example

Deletes the specified <code>zones</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.zones
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}';
```
