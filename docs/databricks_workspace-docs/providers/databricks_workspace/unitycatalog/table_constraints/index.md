---
title: table_constraints
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - table_constraints
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

Operations on a <code>table_constraints</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_constraints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.table_constraints" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new table constraint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cascade, constraint_name, full_name, deployment_name" /> | Deletes a table constraint. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>table_constraints</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'table_constraints', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.table_constraints (
deployment_name,
data__full_name_arg,
data__constraint
)
SELECT 
'{{ deployment_name }}',
'{{ full_name_arg }}',
'{{ constraint }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: full_name_arg
    value: string
  - name: constraint
    value:
      primary_key_constraint:
        name: string
        child_columns:
        - string
      foreign_key_constraint:
        name: string
        child_columns:
        - string
        parent_table: string
        parent_columns:
        - string
      named_table_constraint:
        name: string

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>table_constraints</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.table_constraints
WHERE cascade = '{{ cascade }}' AND
constraint_name = '{{ constraint_name }}' AND
full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```
