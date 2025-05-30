---
title: fields
hide_title: false
hide_table_of_contents: false
keywords:
  - fields
  - datacatalog
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

Creates, updates, deletes, gets or lists a <code>fields</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fields</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datacatalog.fields" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_tag_templates_fields_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, tagTemplatesId" /> | Creates a field in a tag template. You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| <CopyableCode code="projects_locations_tag_templates_fields_delete" /> | `DELETE` | <CopyableCode code="fieldsId, locationsId, projectsId, tagTemplatesId" /> | Deletes a field in a tag template and all uses of this field from the tags based on this template. You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| <CopyableCode code="projects_locations_tag_templates_fields_patch" /> | `UPDATE` | <CopyableCode code="fieldsId, locationsId, projectsId, tagTemplatesId" /> | Updates a field in a tag template. You can't update the field type with this method. You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| <CopyableCode code="projects_locations_tag_templates_fields_rename" /> | `EXEC` | <CopyableCode code="fieldsId, locationsId, projectsId, tagTemplatesId" /> | Renames a field in a tag template. You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project] (https://cloud.google.com/data-catalog/docs/concepts/resource-project). |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>fields</code> resource.

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
INSERT INTO google.datacatalog.fields (
locationsId,
projectsId,
tagTemplatesId,
name,
displayName,
type,
isRequired,
description,
order
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ tagTemplatesId }}',
'{{ name }}',
'{{ displayName }}',
'{{ type }}',
{{ isRequired }},
'{{ description }}',
'{{ order }}'
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
    - name: type
      value:
        - name: primitiveType
          value: string
        - name: enumType
          value:
            - name: allowedValues
              value:
                - - name: displayName
                    value: string
    - name: isRequired
      value: boolean
    - name: description
      value: string
    - name: order
      value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>fields</code> resource.

```sql
/*+ update */
UPDATE google.datacatalog.fields
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
type = '{{ type }}',
isRequired = true|false,
description = '{{ description }}',
order = '{{ order }}'
WHERE 
fieldsId = '{{ fieldsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tagTemplatesId = '{{ tagTemplatesId }}';
```

## `DELETE` example

Deletes the specified <code>fields</code> resource.

```sql
/*+ delete */
DELETE FROM google.datacatalog.fields
WHERE fieldsId = '{{ fieldsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tagTemplatesId = '{{ tagTemplatesId }}';
```
