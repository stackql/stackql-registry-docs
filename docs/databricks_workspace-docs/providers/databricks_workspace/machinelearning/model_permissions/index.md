---
title: model_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - model_permissions
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

Operations on a <code>model_permissions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_permissions" /></td></tr>
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
| <CopyableCode code="getpermissions" /> | `SELECT` | <CopyableCode code="registered_model_id, deployment_name" /> | Gets the permissions of a registered model. Registered models can inherit permissions from their root object. |
| <CopyableCode code="updatepermissions" /> | `UPDATE` | <CopyableCode code="registered_model_id, deployment_name" /> | Updates the permissions on a registered model. Registered models can inherit permissions from their root object. |
| <CopyableCode code="setpermissions" /> | `REPLACE` | <CopyableCode code="registered_model_id, deployment_name" /> | Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct permissions if none are specified. Objects can inherit permissions from their root object. |

## `SELECT` examples

```sql
SELECT
access_control_list,
object_id,
object_type
FROM databricks_workspace.machinelearning.model_permissions
WHERE registered_model_id = '{{ registered_model_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>model_permissions</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.machinelearning.model_permissions
SET { field = value }
WHERE registered_model_id = '{{ registered_model_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>model_permissions</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.machinelearning.model_permissions
SET { field = value }
WHERE registered_model_id = '{{ registered_model_id }}' AND
deployment_name = '{{ deployment_name }}';
```
