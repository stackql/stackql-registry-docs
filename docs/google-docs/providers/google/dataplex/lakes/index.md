---
title: lakes
hide_title: false
hide_table_of_contents: false
keywords:
  - lakes
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

Creates, updates, deletes, gets or lists a <code>lakes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lakes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.lakes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the lake, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the lake. |
| <CopyableCode code="assetStatus" /> | `object` | Aggregated status of the underlying assets of a lake or zone. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the lake was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the lake. |
| <CopyableCode code="metastore" /> | `object` | Settings to manage association of Dataproc Metastore with a lake. |
| <CopyableCode code="metastoreStatus" /> | `object` | Status of Lake and Dataproc Metastore service instance association. |
| <CopyableCode code="serviceAccount" /> | `string` | Output only. Service account associated with this lake. This service account must be authorized to access or operate on resources managed by the lake. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the lake. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the lake. This ID will be different if the lake is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the lake was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_get" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Retrieves a lake resource. |
| <CopyableCode code="projects_locations_lakes_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists lake resources in a project and location. |
| <CopyableCode code="projects_locations_lakes_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a lake resource. |
| <CopyableCode code="projects_locations_lakes_delete" /> | `DELETE` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Deletes a lake resource. All zones within the lake must be deleted before the lake can be deleted. |
| <CopyableCode code="projects_locations_lakes_patch" /> | `UPDATE` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Updates a lake resource. |

## `SELECT` examples

Lists lake resources in a project and location.

```sql
SELECT
name,
description,
assetStatus,
createTime,
displayName,
labels,
metastore,
metastoreStatus,
serviceAccount,
state,
uid,
updateTime
FROM google.dataplex.lakes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>lakes</code> resource.

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
INSERT INTO google.dataplex.lakes (
locationsId,
projectsId,
displayName,
labels,
description,
metastore
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ labels }}',
'{{ description }}',
'{{ metastore }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: '{{ displayName }}'
    - name: labels
      value: '{{ labels }}'
    - name: description
      value: '{{ description }}'
    - name: metastore
      value:
        - name: service
          value: '{{ service }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>lakes</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.lakes
SET 
displayName = '{{ displayName }}',
labels = '{{ labels }}',
description = '{{ description }}',
metastore = '{{ metastore }}'
WHERE 
lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>lakes</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.lakes
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
