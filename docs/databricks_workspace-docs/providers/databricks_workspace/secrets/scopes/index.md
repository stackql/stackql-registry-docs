---
title: scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - scopes
  - secrets
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

Operations on a <code>scopes</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.secrets.scopes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="backend_type" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listscopes" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Lists all secret scopes available in the workspace. |
| <CopyableCode code="createscope" /> | `INSERT` | <CopyableCode code="deployment_name" /> | The scope name must consist of alphanumeric characters, dashes, underscores, and periods,  and may not exceed 128 characters. |
| <CopyableCode code="deletescope" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Deletes a secret scope. |

## `SELECT` examples

```sql
SELECT
name,
backend_type
FROM databricks_workspace.secrets.scopes
WHERE deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scopes</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'scopes', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.secrets.scopes (
deployment_name,
data__scope,
data__initial_manage_principal,
data__scope_backend_type
)
SELECT 
'{{ deployment_name }}',
'{{ scope }}',
'{{ initial_manage_principal }}',
'{{ scope_backend_type }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: scope
    value: string
  - name: initial_manage_principal
    value: string
  - name: scope_backend_type
    value: DATABRICKS

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>scopes</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.secrets.scopes
WHERE deployment_name = '{{ deployment_name }}';
```
