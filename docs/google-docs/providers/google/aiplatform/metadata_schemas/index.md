---
title: metadata_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_schemas
  - aiplatform
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

Creates, updates, deletes, gets or lists a <code>metadata_schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metadata_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.metadata_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the MetadataSchema. |
| <CopyableCode code="description" /> | `string` | Description of the Metadata Schema |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this MetadataSchema was created. |
| <CopyableCode code="schema" /> | `string` | Required. The raw YAML string representation of the MetadataSchema. The combination of [MetadataSchema.version] and the schema name given by `title` in [MetadataSchema.schema] must be unique within a MetadataStore. The schema is defined as an OpenAPI 3.0.2 [MetadataSchema Object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#schemaObject) |
| <CopyableCode code="schemaType" /> | `string` | The type of the MetadataSchema. This is a property that identifies which metadata types will use the MetadataSchema. |
| <CopyableCode code="schemaVersion" /> | `string` | The version of the MetadataSchema. The version's format must match the following regular expression: `^[0-9]+.+.+$`, which would allow to order/compare different versions. Example: 1.0.0, 1.0.1, etc. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, metadataSchemasId, metadataStoresId, projectsId" /> | Retrieves a specific MetadataSchema. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Lists MetadataSchemas. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Creates a MetadataSchema. |

## `SELECT` examples

Lists MetadataSchemas.

```sql
SELECT
name,
description,
createTime,
schema,
schemaType,
schemaVersion
FROM google.aiplatform.metadata_schemas
WHERE locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metadata_schemas</code> resource.

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
INSERT INTO google.aiplatform.metadata_schemas (
locationsId,
metadataStoresId,
projectsId,
schemaType,
schema,
description,
schemaVersion,
name,
createTime
)
SELECT 
'{{ locationsId }}',
'{{ metadataStoresId }}',
'{{ projectsId }}',
'{{ schemaType }}',
'{{ schema }}',
'{{ description }}',
'{{ schemaVersion }}',
'{{ name }}',
'{{ createTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: schemaType
        value: '{{ schemaType }}'
      - name: schema
        value: '{{ schema }}'
      - name: description
        value: '{{ description }}'
      - name: schemaVersion
        value: '{{ schemaVersion }}'
      - name: name
        value: '{{ name }}'
      - name: createTime
        value: '{{ createTime }}'

```
</TabItem>
</Tabs>
