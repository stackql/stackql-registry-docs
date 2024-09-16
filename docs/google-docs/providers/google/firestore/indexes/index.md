---
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
  - firestore
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

Creates, updates, deletes, gets or lists a <code>indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.firestore.indexes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. A server defined name for this index. The form of this name for composite indexes will be: `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{composite_index_id}` For single field indexes, this field will be empty. |
| <CopyableCode code="apiScope" /> | `string` | The API scope supported by this index. |
| <CopyableCode code="fields" /> | `array` | The fields supported by this index. For composite indexes, this requires a minimum of 2 and a maximum of 100 fields. The last field entry is always for the field path `__name__`. If, on creation, `__name__` was not specified as the last field, it will be added automatically with the same direction as that of the last field defined. If the final field in a composite index is not directional, the `__name__` will be ordered ASCENDING (unless explicitly specified). For single field indexes, this will always be exactly one entry with a field path equal to the field path of the associated field. |
| <CopyableCode code="queryScope" /> | `string` | Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the same collection ID. Indexes with a collection group query scope specified allow queries against all collections descended from a specific document, specified at query time, and that have the same collection ID as this index. |
| <CopyableCode code="state" /> | `string` | Output only. The serving state of the index. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="collectionGroupsId, databasesId, indexesId, projectsId" /> | Gets a composite index. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="collectionGroupsId, databasesId, projectsId" /> | Lists composite indexes. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="collectionGroupsId, databasesId, projectsId" /> | Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="collectionGroupsId, databasesId, indexesId, projectsId" /> | Deletes a composite index. |

## `SELECT` examples

Lists composite indexes.

```sql
SELECT
name,
apiScope,
fields,
queryScope,
state
FROM google.firestore.indexes
WHERE collectionGroupsId = '{{ collectionGroupsId }}'
AND databasesId = '{{ databasesId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>indexes</code> resource.

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
INSERT INTO google.firestore.indexes (
collectionGroupsId,
databasesId,
projectsId,
name,
queryScope,
apiScope,
fields,
state
)
SELECT 
'{{ collectionGroupsId }}',
'{{ databasesId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ queryScope }}',
'{{ apiScope }}',
'{{ fields }}',
'{{ state }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: queryScope
      value: '{{ queryScope }}'
    - name: apiScope
      value: '{{ apiScope }}'
    - name: fields
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: state
      value: '{{ state }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>indexes</code> resource.

```sql
/*+ delete */
DELETE FROM google.firestore.indexes
WHERE collectionGroupsId = '{{ collectionGroupsId }}'
AND databasesId = '{{ databasesId }}'
AND indexesId = '{{ indexesId }}'
AND projectsId = '{{ projectsId }}';
```
