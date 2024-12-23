---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - permissions
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

Operations on a <code>permissions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="namespace" /> | `object` |
| <CopyableCode code="setting_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets the default namespace setting. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Deletes the default namespace setting for the workspace. A fresh etag needs to be provided in |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates the default namespace setting for the workspace. A fresh etag needs to be provided in |

## `SELECT` examples

```sql
SELECT
etag,
namespace,
setting_name
FROM databricks_workspace.workspace.permissions
WHERE deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>permissions</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.workspace.permissions
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>permissions</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.workspace.permissions
WHERE deployment_name = '{{ deployment_name }}';
```
