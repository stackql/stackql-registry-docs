---
title: restrict_admins
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - restrict_admins
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

Operations on a <code>restrict_admins</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restrict_admins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.restrict_admins" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="restrict_workspace_admins" /> | `object` |
| <CopyableCode code="setting_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets the restrict workspace admins setting. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Reverts the restrict workspace admins setting status for the workspace. A fresh etag needs to be provided in |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates the restrict workspace admins setting for the workspace. A fresh etag needs to be provided in |

## `SELECT` examples

```sql
SELECT
etag,
restrict_workspace_admins,
setting_name
FROM databricks_workspace.workspace.restrict_admins
WHERE deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>restrict_admins</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.workspace.restrict_admins
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>restrict_admins</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.workspace.restrict_admins
WHERE deployment_name = '{{ deployment_name }}';
```
