---
title: experiment_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - experiment_permissions
  - machinelearning
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

Operations on a <code>experiment_permissions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.experiment_permissions" /></td></tr>
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
| <CopyableCode code="getpermissions" /> | `SELECT` | <CopyableCode code="experiment_id, deployment_name" /> | Gets the permissions of an experiment. Experiments can inherit permissions from their root object. |
| <CopyableCode code="updatepermissions" /> | `UPDATE` | <CopyableCode code="experiment_id, deployment_name" /> | Updates the permissions on an experiment. Experiments can inherit permissions from their root object. |
| <CopyableCode code="setpermissions" /> | `REPLACE` | <CopyableCode code="experiment_id, deployment_name" /> | Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct permissions if none are specified. Objects can inherit permissions from their root object. |

## `SELECT` examples

```sql
SELECT
access_control_list,
object_id,
object_type
FROM databricks_workspace.machinelearning.experiment_permissions
WHERE experiment_id = '{{ experiment_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>experiment_permissions</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.machinelearning.experiment_permissions
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE experiment_id = '{{ experiment_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>experiment_permissions</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.machinelearning.experiment_permissions
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE experiment_id = '{{ experiment_id }}' AND
deployment_name = '{{ deployment_name }}';
```
