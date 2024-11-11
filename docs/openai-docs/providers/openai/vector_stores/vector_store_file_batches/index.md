---
title: vector_store_file_batches
hide_title: false
hide_table_of_contents: false
keywords:
  - vector_store_file_batches
  - vector_stores
  - openai
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage openai resources using SQL
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>vector_store_file_batches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vector_store_file_batches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.vector_stores.vector_store_file_batches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the vector store files batch was created. |
| <CopyableCode code="file_counts" /> | `object` |  |
| <CopyableCode code="object" /> | `string` | The object type, which is always `vector_store.file_batch`. |
| <CopyableCode code="status" /> | `string` | The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`. |
| <CopyableCode code="vector_store_id" /> | `string` | The ID of the [vector store](/docs/api-reference/vector-stores/object) that the [File](/docs/api-reference/files) is attached to. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_vector_store_file_batch" /> | `SELECT` | <CopyableCode code="batch_id, vector_store_id" /> |  |
| <CopyableCode code="create_vector_store_file_batch" /> | `INSERT` | <CopyableCode code="vector_store_id, data__file_ids" /> |  |
| <CopyableCode code="cancel_vector_store_file_batch" /> | `EXEC` | <CopyableCode code="batch_id, vector_store_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
created_at,
file_counts,
object,
status,
vector_store_id
FROM openai.vector_stores.vector_store_file_batches
WHERE batch_id = '{{ batch_id }}'
AND vector_store_id = '{{ vector_store_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vector_store_file_batches</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO openai.vector_stores.vector_store_file_batches (
data__file_ids,
data__chunking_strategy,
vector_store_id
)
SELECT 
'{{ file_ids }}',
'{{ chunking_strategy }}',
'{{ vector_store_id }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO openai.vector_stores.vector_store_file_batches (
data__file_ids,
vector_store_id
)
SELECT 
'{{ file_ids }}',
'{{ vector_store_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: vector_store_file_batches
  props:
    - name: vector_store_id
      value: string
    - name: data__file_ids
      value: string
    - name: file_ids
      value: array
    - name: chunking_strategy
      props:
        - name: type
          value: string

```
</TabItem>
</Tabs>
