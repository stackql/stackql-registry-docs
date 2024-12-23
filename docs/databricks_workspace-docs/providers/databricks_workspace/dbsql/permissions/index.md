---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - permissions
  - dbsql
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

Operations on a <code>permissions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.permissions" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="objectId, objectType, deployment_name" /> | Gets a JSON representation of the access control list (ACL) for a specified object. |
| <CopyableCode code="set" /> | `REPLACE` | <CopyableCode code="objectId, objectType, deployment_name" /> | Sets the access control list (ACL) for a specified object. This operation will complete rewrite the ACL. |
| <CopyableCode code="transferownership" /> | `EXEC` | <CopyableCode code="objectType, deployment_name" /> | Transfer ownership of a single object. |

## `SELECT` examples

```sql
SELECT
access_control_list,
object_id,
object_type
FROM databricks_workspace.dbsql.permissions
WHERE objectId = '{{ objectId }}' AND
objectType = '{{ objectType }}' AND
deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>permissions</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.dbsql.permissions
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE objectId = '{{ objectId }}' AND
objectType = '{{ objectType }}' AND
deployment_name = '{{ deployment_name }}';
```
