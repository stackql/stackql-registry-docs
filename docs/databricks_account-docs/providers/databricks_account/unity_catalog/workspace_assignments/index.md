---
title: workspace_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - workspace_assignments
  - unity_catalog
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>workspace_assignments</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.unity_catalog.workspace_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="workspace_ids" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id, metastore_id" /> | Gets a list of all Databricks workspace IDs that have been assigned to given metastore. |

## `SELECT` examples

```sql
SELECT
workspace_ids
FROM databricks_account.unity_catalog.workspace_assignments
WHERE account_id = '{{ account_id }}' AND
metastore_id = '{{ metastore_id }}';
```
