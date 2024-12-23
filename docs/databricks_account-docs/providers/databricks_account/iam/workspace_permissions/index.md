---
title: workspace_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - workspace_permissions
  - iam
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

Operations on a <code>workspace_permissions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.workspace_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="permission_level" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, workspace_id" /> | Get an array of workspace permissions for the specified account and workspace. |

## `SELECT` examples

```sql
SELECT
description,
permission_level
FROM databricks_account.iam.workspace_permissions
WHERE account_id = '{{ account_id }}' AND
workspace_id = '{{ workspace_id }}';
```
