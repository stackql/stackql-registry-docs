---
title: workspace_permission_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - workspace_permission_assignments
  - iam
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

Operations on a <code>workspace_permission_assignments</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_permission_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.workspace_permission_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="error" /> | `string` |
| <CopyableCode code="permissions" /> | `array` |
| <CopyableCode code="principal" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id, workspace_id" /> | Get the permission assignments for the specified Databricks account and Databricks workspace. |
| <CopyableCode code="createorupdate" /> | `INSERT` | <CopyableCode code="account_id, principal_id, workspace_id" /> | Creates or updates the workspace permissions assignment in a given account and workspace for the specified principal. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, principal_id, workspace_id" /> | Deletes the workspace permissions assignment in a given account and workspace for the specified principal. |

## `SELECT` examples

```sql
SELECT
error,
permissions,
principal
FROM databricks_account.iam.workspace_permission_assignments
WHERE account_id = '{{ account_id }}' AND
workspace_id = '{{ workspace_id }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_permission_assignments</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'workspace_permission_assignments', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.iam.workspace_permission_assignments (
account_id,
principal_id,
workspace_id,
data__permissions
)
SELECT 
'{{ account_id }}',
'{{ principal_id }}',
'{{ workspace_id }}',
'{{ permissions }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: permissions
    value:
    - ADMIN # can be ADMIN or USER

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>workspace_permission_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.iam.workspace_permission_assignments
WHERE account_id = '{{ account_id }}' AND
principal_id = '{{ principal_id }}' AND
workspace_id = '{{ workspace_id }}';
```
