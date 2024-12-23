---
title: metastore_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - metastore_assignments
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

Operations on a <code>metastore_assignments</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metastore_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.metastore_assignments" /></td></tr>
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
| <CopyableCode code="current" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets the metastore assignment for the workspace being accessed. |
| <CopyableCode code="assign" /> | `INSERT` | <CopyableCode code="workspace_id, deployment_name" /> | Creates a new metastore assignment. If an assignment for the same |
| <CopyableCode code="unassign" /> | `DELETE` | <CopyableCode code="metastore_id, workspace_id, deployment_name" /> | Deletes a metastore assignment. The caller must be an account administrator. |
| <CopyableCode code="updateassignment" /> | `UPDATE` | <CopyableCode code="workspace_id, deployment_name" /> | Updates a metastore assignment. This operation can be used to update |

## `SELECT` examples

```sql
SELECT
default_catalog_name,
metastore_id,
workspace_id
FROM databricks_workspace.unitycatalog.metastore_assignments
WHERE deployment_name = '{{ deployment_name }}';
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
INSERT INTO databricks_workspace.unitycatalog.metastore_assignments (
workspace_id,
deployment_name,
data__metastore_id,
data__default_catalog_name
)
SELECT 
'{{ workspace_id }}',
'{{ deployment_name }}',
'{{ metastore_id }}',
'{{ default_catalog_name }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: metastore_id
    value: string
  - name: default_catalog_name
    value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>metastore_assignments</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.unitycatalog.metastore_assignments
SET { field = value }
WHERE workspace_id = '{{ workspace_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>metastore_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.metastore_assignments
WHERE metastore_id = '{{ metastore_id }}' AND
workspace_id = '{{ workspace_id }}' AND
deployment_name = '{{ deployment_name }}';
```
