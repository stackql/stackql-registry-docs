---
title: contentitems
hide_title: false
hide_table_of_contents: false
keywords:
  - contentitems
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

Creates, updates, deletes, gets or lists a <code>contentitems</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contentitems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.contentitems" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the content, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/content/{content_id} |
| <CopyableCode code="description" /> | `string` | Optional. Description of the content. |
| <CopyableCode code="createTime" /> | `string` | Output only. Content creation time. |
| <CopyableCode code="dataText" /> | `string` | Required. Content data in string format. |
| <CopyableCode code="labels" /> | `object` | Optional. User defined labels for the content. |
| <CopyableCode code="notebook" /> | `object` | Configuration for Notebook content. |
| <CopyableCode code="path" /> | `string` | Required. The path for the Content file, represented as directory structure. Unique within a lake. Limited to alphanumerics, hyphens, underscores, dots and slashes. |
| <CopyableCode code="sqlScript" /> | `object` | Configuration for the Sql Script content. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the content. This ID will be different if the content is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the content was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_contentitems_get" /> | `SELECT` | <CopyableCode code="contentitemsId, lakesId, locationsId, projectsId" /> | Get a content resource. |
| <CopyableCode code="projects_locations_lakes_contentitems_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | List content. |
| <CopyableCode code="projects_locations_lakes_contentitems_create" /> | `INSERT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Create a content. |
| <CopyableCode code="projects_locations_lakes_contentitems_delete" /> | `DELETE` | <CopyableCode code="contentitemsId, lakesId, locationsId, projectsId" /> | Delete a content. |
| <CopyableCode code="projects_locations_lakes_contentitems_patch" /> | `UPDATE` | <CopyableCode code="contentitemsId, lakesId, locationsId, projectsId" /> | Update a content. Only supports full resource update. |

## `SELECT` examples

List content.

```sql
SELECT
name,
description,
createTime,
dataText,
labels,
notebook,
path,
sqlScript,
uid,
updateTime
FROM google.dataplex.contentitems
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contentitems</code> resource.

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
INSERT INTO google.dataplex.contentitems (
lakesId,
locationsId,
projectsId,
path,
labels,
description,
dataText,
sqlScript,
notebook
)
SELECT 
'{{ lakesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ path }}',
'{{ labels }}',
'{{ description }}',
'{{ dataText }}',
'{{ sqlScript }}',
'{{ notebook }}'
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
    - name: path
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: description
      value: string
    - name: dataText
      value: string
    - name: sqlScript
      value:
        - name: engine
          value: string
    - name: notebook
      value:
        - name: kernelType
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>contentitems</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.contentitems
SET 
path = '{{ path }}',
labels = '{{ labels }}',
description = '{{ description }}',
dataText = '{{ dataText }}',
sqlScript = '{{ sqlScript }}',
notebook = '{{ notebook }}'
WHERE 
contentitemsId = '{{ contentitemsId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>contentitems</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.contentitems
WHERE contentitemsId = '{{ contentitemsId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
