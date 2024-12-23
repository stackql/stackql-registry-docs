---
title: dashboard_embedding_access_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dashboard_embedding_access_policy
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

Operations on a <code>dashboard_embedding_access_policy</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard_embedding_access_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.dashboard_embedding_access_policy" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="aibi_dashboard_embedding_access_policy" /> | `object` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="setting_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Retrieves the AI/BI dashboard embedding access policy. The default setting is ALLOW_APPROVED_DOMAINS, permitting AI/BI dashboards to be embedded on approved domains. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Delete the AI/BI dashboard embedding access policy, reverting back to the default. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates the AI/BI dashboard embedding access policy at the workspace level. |

## `SELECT` examples

```sql
SELECT
aibi_dashboard_embedding_access_policy,
etag,
setting_name
FROM databricks_workspace.workspace.dashboard_embedding_access_policy
WHERE deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>dashboard_embedding_access_policy</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.workspace.dashboard_embedding_access_policy
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>dashboard_embedding_access_policy</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.workspace.dashboard_embedding_access_policy
WHERE deployment_name = '{{ deployment_name }}';
```
