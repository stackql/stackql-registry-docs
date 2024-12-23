---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - permissions
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

Operations on a <code>permissions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.permissions" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="request_object_id, request_object_type, deployment_name" /> | Gets the permissions of an object. Objects can inherit permissions from their parent objects or root object. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="request_object_id, request_object_type, deployment_name" /> | Updates the permissions on an object. Objects can inherit permissions from their parent objects or root object. |
| <CopyableCode code="set" /> | `REPLACE` | <CopyableCode code="request_object_id, request_object_type, deployment_name" /> | Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct permissions if none are specified. Objects can inherit permissions from their parent objects or root object. |

## `SELECT` examples

```sql
SELECT
access_control_list,
object_id,
object_type
FROM databricks_workspace.iam.permissions
WHERE request_object_id = '{{ request_object_id }}' AND
request_object_type = '{{ request_object_type }}' AND
deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>permissions</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.iam.permissions
SET { field = value }
WHERE request_object_id = '{{ request_object_id }}' AND
request_object_type = '{{ request_object_type }}' AND
deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>permissions</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.iam.permissions
SET { field = value }
WHERE request_object_id = '{{ request_object_id }}' AND
request_object_type = '{{ request_object_type }}' AND
deployment_name = '{{ deployment_name }}';
```
