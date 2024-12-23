---
title: storage_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - storage_credentials
  - unitycatalog
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

Operations on a <code>storage_credentials</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.storage_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="aws_iam_role" /> | `object` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="full_name" /> | `string` |
| <CopyableCode code="isolation_mode" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="read_only" /> | `boolean` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |
| <CopyableCode code="used_for_managed_storage" /> | `boolean` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the storage credential, or have some permission on the storage credential. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets an array of storage credentials (as |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new storage credential. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes a storage credential from the metastore. The caller must be an owner of the storage credential. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates a storage credential on the metastore. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'storage_credentials (list)', value: 'list' },
        { label: 'storage_credentials (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
aws_iam_role,
comment,
created_at,
created_by,
full_name,
isolation_mode,
metastore_id,
owner,
read_only,
updated_at,
updated_by,
used_for_managed_storage
FROM databricks_workspace.unitycatalog.storage_credentials
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
aws_iam_role,
comment,
created_at,
created_by,
full_name,
isolation_mode,
metastore_id,
owner,
read_only,
updated_at,
updated_by,
used_for_managed_storage
FROM databricks_workspace.unitycatalog.storage_credentials
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_credentials</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'storage_credentials', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.storage_credentials (
deployment_name,
data__name,
data__comment,
data__read_only,
data__aws_iam_role,
data__skip_validation
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ comment }}',
'{{ read_only }}',
'{{ aws_iam_role }}',
'{{ skip_validation }}'
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
  - name: read_only
    value: true
  - name: aws_iam_role
    value:
      role_arn: string
  - name: skip_validation
    value: false

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>storage_credentials</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.unitycatalog.storage_credentials
SET { field = value }
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>storage_credentials</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.storage_credentials
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
