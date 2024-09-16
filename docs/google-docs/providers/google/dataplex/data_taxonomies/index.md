---
title: data_taxonomies
hide_title: false
hide_table_of_contents: false
keywords:
  - data_taxonomies
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

Creates, updates, deletes, gets or lists a <code>data_taxonomies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_taxonomies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.data_taxonomies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the DataTaxonomy, of the form: projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the DataTaxonomy. |
| <CopyableCode code="attributeCount" /> | `integer` | Output only. The number of attributes in the DataTaxonomy. |
| <CopyableCode code="classCount" /> | `integer` | Output only. The number of classes in the DataTaxonomy. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the DataTaxonomy was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the DataTaxonomy. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the dataTaxonomy. This ID will be different if the DataTaxonomy is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the DataTaxonomy was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_data_taxonomies_get" /> | `SELECT` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Retrieves a DataTaxonomy resource. |
| <CopyableCode code="projects_locations_data_taxonomies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DataTaxonomy resources in a project and location. |
| <CopyableCode code="projects_locations_data_taxonomies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a DataTaxonomy resource. |
| <CopyableCode code="projects_locations_data_taxonomies_delete" /> | `DELETE` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Deletes a DataTaxonomy resource. All attributes within the DataTaxonomy must be deleted before the DataTaxonomy can be deleted. |
| <CopyableCode code="projects_locations_data_taxonomies_patch" /> | `UPDATE` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Updates a DataTaxonomy resource. |

## `SELECT` examples

Lists DataTaxonomy resources in a project and location.

```sql
SELECT
name,
description,
attributeCount,
classCount,
createTime,
displayName,
etag,
labels,
uid,
updateTime
FROM google.dataplex.data_taxonomies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_taxonomies</code> resource.

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
INSERT INTO google.dataplex.data_taxonomies (
locationsId,
projectsId,
description,
displayName,
labels,
etag
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ displayName }}',
'{{ labels }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: description
      value: '{{ description }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: labels
      value: '{{ labels }}'
    - name: etag
      value: '{{ etag }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>data_taxonomies</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.data_taxonomies
SET 
description = '{{ description }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
etag = '{{ etag }}'
WHERE 
dataTaxonomiesId = '{{ dataTaxonomiesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>data_taxonomies</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.data_taxonomies
WHERE dataTaxonomiesId = '{{ dataTaxonomiesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
