---
title: permission_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - permission_levels
  - apps
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

Operations on a <code>permission_levels</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.permission_levels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="permission_level" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getpermissionlevels" /> | `SELECT` | <CopyableCode code="app_name, deployment_name" /> | Gets the permission levels that a user can have on an object. |

## `SELECT` examples

```sql
SELECT
description,
permission_level
FROM databricks_workspace.apps.permission_levels
WHERE app_name = '{{ app_name }}' AND
deployment_name = '{{ deployment_name }}';
```
