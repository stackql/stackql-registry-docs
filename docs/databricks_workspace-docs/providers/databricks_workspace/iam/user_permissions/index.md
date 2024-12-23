---
title: user_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - user_permissions
  - iam
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

Operations on a <code>user_permissions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.user_permissions" /></td></tr>
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
| <CopyableCode code="getpermissions" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets the permissions of all passwords. Passwords can inherit permissions from their root object. |
| <CopyableCode code="updatepermissions" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates the permissions on all passwords. Passwords can inherit permissions from their root object. |
| <CopyableCode code="setpermissions" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct permissions if none are specified. Objects can inherit permissions from their root object. |

## `SELECT` examples

```sql
SELECT
access_control_list,
object_id,
object_type
FROM databricks_workspace.iam.user_permissions
WHERE deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>user_permissions</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.iam.user_permissions
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>user_permissions</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.iam.user_permissions
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```
