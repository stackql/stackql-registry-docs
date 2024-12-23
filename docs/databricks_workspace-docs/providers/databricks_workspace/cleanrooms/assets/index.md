---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - assets
  - cleanrooms
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

Operations on a <code>assets</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.assets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="added_at" /> | `integer` |
| <CopyableCode code="asset_type" /> | `string` |
| <CopyableCode code="foreign_table" /> | `object` |
| <CopyableCode code="foreign_table_local_details" /> | `object` |
| <CopyableCode code="notebook" /> | `object` |
| <CopyableCode code="owner_collaborator_alias" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="table" /> | `object` |
| <CopyableCode code="table_local_details" /> | `object` |
| <CopyableCode code="view" /> | `object` |
| <CopyableCode code="view_local_details" /> | `object` |
| <CopyableCode code="volume_local_details" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clean_room_name, deployment_name" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clean_room_name, deployment_name" /> | Create a clean room asset —share an asset like a notebook or table into the clean room. For each UC asset that is added through this method, the clean room owner must also have enough privilege on the asset to consume it. The privilege must be maintained indefinitely for the clean room to be able to access the asset. Typically, you should use a group as the clean room owner. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="asset_full_name, asset_type, clean_room_name, deployment_name" /> | Delete a clean room asset - unshare/remove the asset from the clean room |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="asset_type, clean_room_name, name, deployment_name" /> | Update a clean room asset. For example, updating the content of a notebook; changing the shared partitions of a table; etc. |

## `SELECT` examples

```sql
SELECT
name,
added_at,
asset_type,
foreign_table,
foreign_table_local_details,
notebook,
owner_collaborator_alias,
status,
table,
table_local_details,
view,
view_local_details,
volume_local_details
FROM databricks_workspace.cleanrooms.assets
WHERE clean_room_name = '{{ clean_room_name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assets</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'assets', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.cleanrooms.assets (
clean_room_name,
deployment_name,
data__name,
data__asset_type,
data__table_local_details,
data__volume_local_details,
data__view_local_details,
data__foreign_table_local_details,
data__table,
data__notebook,
data__view,
data__foreign_table
)
SELECT 
'{{ clean_room_name }}',
'{{ deployment_name }}',
'{{ name }}',
'{{ asset_type }}',
'{{ table_local_details }}',
'{{ volume_local_details }}',
'{{ view_local_details }}',
'{{ foreign_table_local_details }}',
'{{ table }}',
'{{ notebook }}',
'{{ view }}',
'{{ foreign_table }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: creator.sales.products
  - name: asset_type
    value: TABLE
  - name: table_local_details
    value:
      local_name: demo.sales.products
      partitions:
      - values:
        - name: string
          value: string
          recipient_property_key: string
          op: EQUAL
  - name: volume_local_details
    value:
      local_name: demo.sales.products
  - name: view_local_details
    value:
      local_name: demo.sales.products
  - name: foreign_table_local_details
    value:
      local_name: demo.sales.products
  - name: table
    value:
      columns:
      - name: string
        type_text: string
        type_name: BOOLEAN
        position: 0
        type_precision: 0
        type_scale: 0
        type_interval_type: string
        type_json: string
        comment: string
        nullable: true
        partition_index: 0
        mask:
          function_name: string
          using_column_names:
          - string
  - name: notebook
    value:
      notebook_content: string
      etag: string
  - name: view
    value:
      columns:
      - name: string
        type_text: string
        type_name: BOOLEAN
        position: 0
        type_precision: 0
        type_scale: 0
        type_interval_type: string
        type_json: string
        comment: string
        nullable: true
        partition_index: 0
        mask:
          function_name: string
          using_column_names:
          - string
  - name: foreign_table
    value:
      columns:
      - name: string
        type_text: string
        type_name: BOOLEAN
        position: 0
        type_precision: 0
        type_scale: 0
        type_interval_type: string
        type_json: string
        comment: string
        nullable: true
        partition_index: 0
        mask:
          function_name: string
          using_column_names:
          - string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>assets</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.cleanrooms.assets
SET { field = value }
WHERE asset_type = '{{ asset_type }}' AND
clean_room_name = '{{ clean_room_name }}' AND
name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>assets</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.cleanrooms.assets
WHERE asset_full_name = '{{ asset_full_name }}' AND
asset_type = '{{ asset_type }}' AND
clean_room_name = '{{ clean_room_name }}' AND
deployment_name = '{{ deployment_name }}';
```
