---
title: automatic_cluster_update
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - automatic_cluster_update
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

Operations on a <code>automatic_cluster_update</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>automatic_cluster_update</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.automatic_cluster_update" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="automatic_cluster_update_workspace" /> | `object` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="setting_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets the automatic cluster update setting. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates the automatic cluster update setting for the workspace. A fresh etag needs to be provided in |

## `SELECT` examples

```sql
SELECT
automatic_cluster_update_workspace,
etag,
setting_name
FROM databricks_workspace.workspace.automatic_cluster_update
WHERE deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>automatic_cluster_update</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.workspace.automatic_cluster_update
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```
