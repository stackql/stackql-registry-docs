---
title: document_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - document_schemas
  - contentwarehouse
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

Creates, updates, deletes or gets an <code>document_schema</code> resource or lists <code>document_schemas</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>document_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contentwarehouse.document_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the document schema. Format: projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}. The name is ignored when creating a document schema. |
| <CopyableCode code="description" /> | `string` | Schema description. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the document schema is created. |
| <CopyableCode code="displayName" /> | `string` | Required. Name of the schema given by the user. Must be unique per project. |
| <CopyableCode code="documentIsFolder" /> | `boolean` | Document Type, true refers the document is a folder, otherwise it is a typical document. |
| <CopyableCode code="propertyDefinitions" /> | `array` | Document details. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the document schema is last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="documentSchemasId, locationsId, projectsId" /> | Gets a document schema. Returns NOT_FOUND if the document schema does not exist. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists document schemas. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a document schema. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="documentSchemasId, locationsId, projectsId" /> | Deletes a document schema. Returns NOT_FOUND if the document schema does not exist. Returns BAD_REQUEST if the document schema has documents depending on it. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="documentSchemasId, locationsId, projectsId" /> | Updates a Document Schema. Returns INVALID_ARGUMENT if the name of the Document Schema is non-empty and does not equal the existing name. Supports only appending new properties, adding new ENUM possible values, and updating the EnumTypeOptions.validation_check_disabled flag for ENUM possible values. Updating existing properties will result into INVALID_ARGUMENT. |

## `SELECT` examples

Lists document schemas.

```sql
SELECT
name,
description,
createTime,
displayName,
documentIsFolder,
propertyDefinitions,
updateTime
FROM google.contentwarehouse.document_schemas
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>document_schemas</code> resource.

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
INSERT INTO google.contentwarehouse.document_schemas (
locationsId,
projectsId,
name,
updateTime,
description,
createTime,
propertyDefinitions,
displayName,
documentIsFolder
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ updateTime }}',
'{{ description }}',
'{{ createTime }}',
'{{ propertyDefinitions }}',
'{{ displayName }}',
true|false
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
      - name: updateTime
        value: '{{ updateTime }}'
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: propertyDefinitions
        value: '{{ propertyDefinitions }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: documentIsFolder
        value: '{{ documentIsFolder }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a document_schema only if the necessary resources are available.

```sql
UPDATE google.contentwarehouse.document_schemas
SET 
documentSchema = '{{ documentSchema }}'
WHERE 
documentSchemasId = '{{ documentSchemasId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified document_schema resource.

```sql
DELETE FROM google.contentwarehouse.document_schemas
WHERE documentSchemasId = '{{ documentSchemasId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
