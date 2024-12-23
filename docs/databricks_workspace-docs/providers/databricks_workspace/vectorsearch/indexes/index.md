---
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - indexes
  - vectorsearch
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>indexes</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.indexes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="creator" /> | `string` |
| <CopyableCode code="delta_sync_index_spec" /> | `object` |
| <CopyableCode code="endpoint_name" /> | `string` |
| <CopyableCode code="index_type" /> | `string` |
| <CopyableCode code="primary_key" /> | `string` |
| <CopyableCode code="status" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getindex" /> | `SELECT` | <CopyableCode code="index_name, deployment_name" /> | Get an index. |
| <CopyableCode code="listindexes" /> | `SELECT` | <CopyableCode code="endpoint_name, deployment_name" /> | List all indexes in the given endpoint. |
| <CopyableCode code="createindex" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create a new index. |
| <CopyableCode code="deleteindex" /> | `DELETE` | <CopyableCode code="index_name, deployment_name" /> | Delete an index. |
| <CopyableCode code="querynextpage" /> | `EXEC` | <CopyableCode code="index_name, deployment_name" /> | Use |
| <CopyableCode code="syncindex" /> | `EXEC` | <CopyableCode code="index_name, deployment_name" /> | Triggers a synchronization process for a specified vector index. |

## `SELECT` examples

<Tabs
    defaultValue="getindex"
    values={[
        { label: 'indexes (getindex)', value: 'getindex' },
        { label: 'indexes (listindexes)', value: 'listindexes' }
    ]
}>
<TabItem value="getindex">

```sql
SELECT
name,
creator,
delta_sync_index_spec,
endpoint_name,
index_type,
primary_key,
status
FROM databricks_workspace.vectorsearch.indexes
WHERE index_name = '{{ index_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="listindexes">

```sql
SELECT
name,
creator,
delta_sync_index_spec,
endpoint_name,
index_type,
primary_key,
status
FROM databricks_workspace.vectorsearch.indexes
WHERE endpoint_name = '{{ endpoint_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>indexes</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'indexes', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.vectorsearch.indexes (
deployment_name,
data__name,
data__primary_key,
data__index_type,
data__delta_sync_index_spec
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ primary_key }}',
'{{ index_type }}',
'{{ delta_sync_index_spec }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: main_catalog.docs.en_wiki_index
  - name: primary_key
    value: id
  - name: index_type
    value: DELTA_SYNC
  - name: delta_sync_index_spec
    value:
      source_table: main_catalog.docs.en_wiki
      pipeline_type: TRIGGERED
      embedding_source_columns:
      - name: text
        embedding_model_endpoint_name: e5-small-v2
      columns_to_sync:
      - id
      - text

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>indexes</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.vectorsearch.indexes
WHERE index_name = '{{ index_name }}' AND
deployment_name = '{{ deployment_name }}';
```
