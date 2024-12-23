---
title: object_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - object_permissions
  - workspace
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

Operations on a <code>object_permissions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.object_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="access_control_list" /> | `array` |
| <CopyableCode code="object_id" /> | `string` |
| <CopyableCode code="object_type" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getpermissions" /> | `SELECT` | <CopyableCode code="workspace_object_id, workspace_object_type, deployment_name" /> | Gets the permissions of a workspace object. Workspace objects can inherit permissions from their parent objects or root object. |
| <CopyableCode code="updatepermissions" /> | `UPDATE` | <CopyableCode code="workspace_object_id, workspace_object_type, deployment_name" /> | Updates the permissions on a workspace object. Workspace objects can inherit permissions from their parent objects or root object. |
| <CopyableCode code="setpermissions" /> | `REPLACE` | <CopyableCode code="workspace_object_id, workspace_object_type, deployment_name" /> | Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct permissions if none are specified. Objects can inherit permissions from their parent objects or root object. |

## `SELECT` examples

```sql
SELECT
access_control_list,
object_id,
object_type
FROM databricks_workspace.workspace.object_permissions
WHERE workspace_object_id = '{{ workspace_object_id }}' AND
workspace_object_type = '{{ workspace_object_type }}' AND
deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>object_permissions</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.workspace.object_permissions
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE workspace_object_id = '{{ workspace_object_id }}' AND
workspace_object_type = '{{ workspace_object_type }}' AND
deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>object_permissions</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.workspace.object_permissions
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE workspace_object_id = '{{ workspace_object_id }}' AND
workspace_object_type = '{{ workspace_object_type }}' AND
deployment_name = '{{ deployment_name }}';
```
