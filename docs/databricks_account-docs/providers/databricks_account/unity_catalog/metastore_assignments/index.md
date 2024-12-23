---
title: metastore_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - metastore_assignments
  - unity_catalog
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>metastore_assignments</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metastore_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.unity_catalog.metastore_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="default_catalog_name" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="workspace_id" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, workspace_id" /> | Gets the metastore assignment, if any, for the workspace specified by ID. If the workspace is assigned a metastore, the mappig will be returned. If no metastore is assigned to the workspace, the assignment will not be found and a 404 returned. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id, metastore_id, workspace_id" /> | Creates an assignment to a metastore for a workspace |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, metastore_id, workspace_id" /> | Deletes a metastore assignment to a workspace, leaving the workspace with no metastore. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, metastore_id, workspace_id" /> | Updates an assignment to a metastore for a workspace. Currently, only the default catalog may be updated. |

## `SELECT` examples

```sql
SELECT
default_catalog_name,
metastore_id,
workspace_id
FROM databricks_account.unity_catalog.metastore_assignments
WHERE account_id = '{{ account_id }}' AND
workspace_id = '{{ workspace_id }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metastore_assignments</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'metastore_assignments', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.unity_catalog.metastore_assignments (
account_id,
metastore_id,
workspace_id,
data__metastore_assignment
)
SELECT 
'{{ account_id }}',
'{{ metastore_id }}',
'{{ workspace_id }}',
'{{ metastore_assignment }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: metastore_assignment
    value:
      metastore_id: string
      default_catalog_name: string

```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>metastore_assignments</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_account.unity_catalog.metastore_assignments
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE account_id = '{{ account_id }}' AND
metastore_id = '{{ metastore_id }}' AND
workspace_id = '{{ workspace_id }}';
```

## `DELETE` example

Deletes a <code>metastore_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.unity_catalog.metastore_assignments
WHERE account_id = '{{ account_id }}' AND
metastore_id = '{{ metastore_id }}' AND
workspace_id = '{{ workspace_id }}';
```
