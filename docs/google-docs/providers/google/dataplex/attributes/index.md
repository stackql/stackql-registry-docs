---
title: attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - attributes
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

Creates, updates, deletes, gets or lists a <code>attributes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.attributes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the dataAttribute, of the form: projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the DataAttribute. |
| <CopyableCode code="attributeCount" /> | `integer` | Output only. The number of child attributes present for this attribute. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the DataAttribute was created. |
| <CopyableCode code="dataAccessSpec" /> | `object` | DataAccessSpec holds the access control configuration to be enforced on data stored within resources (eg: rows, columns in BigQuery Tables). When associated with data, the data is only accessible to principals explicitly granted access through the DataAccessSpec. Principals with access to the containing resource are not implicitly granted access. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the DataAttribute. |
| <CopyableCode code="parentId" /> | `string` | Optional. The ID of the parent DataAttribute resource, should belong to the same data taxonomy. Circular dependency in parent chain is not valid. Maximum depth of the hierarchy allowed is 4. a -> b -> c -> d -> e, depth = 4 |
| <CopyableCode code="resourceAccessSpec" /> | `object` | ResourceAccessSpec holds the access control configuration to be enforced on the resources, for example, Cloud Storage bucket, BigQuery dataset, BigQuery table. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the DataAttribute. This ID will be different if the DataAttribute is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the DataAttribute was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_data_taxonomies_attributes_get" /> | `SELECT` | <CopyableCode code="attributesId, dataTaxonomiesId, locationsId, projectsId" /> | Retrieves a Data Attribute resource. |
| <CopyableCode code="projects_locations_data_taxonomies_attributes_list" /> | `SELECT` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Lists Data Attribute resources in a DataTaxonomy. |
| <CopyableCode code="projects_locations_data_taxonomies_attributes_create" /> | `INSERT` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Create a DataAttribute resource. |
| <CopyableCode code="projects_locations_data_taxonomies_attributes_delete" /> | `DELETE` | <CopyableCode code="attributesId, dataTaxonomiesId, locationsId, projectsId" /> | Deletes a Data Attribute resource. |
| <CopyableCode code="projects_locations_data_taxonomies_attributes_patch" /> | `UPDATE` | <CopyableCode code="attributesId, dataTaxonomiesId, locationsId, projectsId" /> | Updates a DataAttribute resource. |

## `SELECT` examples

Lists Data Attribute resources in a DataTaxonomy.

```sql
SELECT
name,
description,
attributeCount,
createTime,
dataAccessSpec,
displayName,
etag,
labels,
parentId,
resourceAccessSpec,
uid,
updateTime
FROM google.dataplex.attributes
WHERE dataTaxonomiesId = '{{ dataTaxonomiesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>attributes</code> resource.

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
INSERT INTO google.dataplex.attributes (
dataTaxonomiesId,
locationsId,
projectsId,
name,
uid,
createTime,
updateTime,
description,
displayName,
labels,
parentId,
attributeCount,
etag,
resourceAccessSpec,
dataAccessSpec
)
SELECT 
'{{ dataTaxonomiesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ description }}',
'{{ displayName }}',
'{{ labels }}',
'{{ parentId }}',
'{{ attributeCount }}',
'{{ etag }}',
'{{ resourceAccessSpec }}',
'{{ dataAccessSpec }}'
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
      - name: uid
        value: '{{ uid }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: description
        value: '{{ description }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: labels
        value: '{{ labels }}'
      - name: parentId
        value: '{{ parentId }}'
      - name: attributeCount
        value: '{{ attributeCount }}'
      - name: etag
        value: '{{ etag }}'
      - name: resourceAccessSpec
        value: '{{ resourceAccessSpec }}'
      - name: dataAccessSpec
        value: '{{ dataAccessSpec }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>attributes</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.attributes
SET 
name = '{{ name }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
parentId = '{{ parentId }}',
attributeCount = '{{ attributeCount }}',
etag = '{{ etag }}',
resourceAccessSpec = '{{ resourceAccessSpec }}',
dataAccessSpec = '{{ dataAccessSpec }}'
WHERE 
attributesId = '{{ attributesId }}'
AND dataTaxonomiesId = '{{ dataTaxonomiesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>attributes</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.attributes
WHERE attributesId = '{{ attributesId }}'
AND dataTaxonomiesId = '{{ dataTaxonomiesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
