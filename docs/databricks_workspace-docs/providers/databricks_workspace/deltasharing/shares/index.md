---
title: shares
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - shares
  - deltasharing
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

Operations on a <code>shares</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltasharing.shares" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="objects" /> | `array` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="storage_location" /> | `string` |
| <CopyableCode code="storage_root" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets a data object share from the metastore. The caller must be a metastore admin or the owner of the share. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets an array of data object shares from the metastore. The caller must be a metastore admin or the owner of the share. There is no guarantee of a specific ordering of the elements in the array. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new share for data objects. Data objects can be added after creation with |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes a data object share from the metastore. The caller must be an owner of the share. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates the share with the changes and data objects in the request. The caller must be the owner of the share or a metastore admin. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'shares (list)', value: 'list' },
        { label: 'shares (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
comment,
created_at,
created_by,
objects,
owner,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.deltasharing.shares
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
comment,
created_at,
created_by,
objects,
owner,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.deltasharing.shares
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>shares</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'shares', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.deltasharing.shares (
deployment_name,
data__name,
data__comment,
data__storage_root
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ comment }}',
'{{ storage_root }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: comment
    value: string
  - name: storage_root
    value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>shares</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.deltasharing.shares
SET { field = value }
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>shares</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.deltasharing.shares
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
