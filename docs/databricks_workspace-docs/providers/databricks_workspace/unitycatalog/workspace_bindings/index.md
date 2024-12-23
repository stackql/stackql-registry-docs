---
title: workspace_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - workspace_bindings
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

Operations on a <code>workspace_bindings</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.workspace_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="binding_type" /> | `string` |
| <CopyableCode code="workspace_id" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getbindings" /> | `SELECT` | <CopyableCode code="securable_name, securable_type, deployment_name" /> | Gets workspace bindings of the securable. The caller must be a metastore admin or an owner of the securable. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates workspace bindings of the catalog. The caller must be a metastore admin or an owner of the catalog. |
| <CopyableCode code="updatebindings" /> | `UPDATE` | <CopyableCode code="securable_name, securable_type, deployment_name" /> | Updates workspace bindings of the securable. The caller must be a metastore admin or an owner of the securable. |

## `SELECT` examples

```sql
SELECT
binding_type,
workspace_id
FROM databricks_workspace.unitycatalog.workspace_bindings
WHERE securable_name = '{{ securable_name }}' AND
securable_type = '{{ securable_type }}' AND
deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>workspace_bindings</code> resource.

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'updatebindings', value: 'updatebindings' }
    ]
}>
<TabItem value="update">

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.workspace_bindings
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
</TabItem>
<TabItem value="updatebindings">

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.workspace_bindings
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE securable_name = '{{ securable_name }}' AND
securable_type = '{{ securable_type }}' AND
deployment_name = '{{ deployment_name }}';
```
</TabItem>
</Tabs>
