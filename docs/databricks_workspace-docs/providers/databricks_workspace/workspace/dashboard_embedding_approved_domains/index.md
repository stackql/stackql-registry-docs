---
title: dashboard_embedding_approved_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dashboard_embedding_approved_domains
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

Operations on a <code>dashboard_embedding_approved_domains</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard_embedding_approved_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.dashboard_embedding_approved_domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="aibi_dashboard_embedding_approved_domains" /> | `object` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="setting_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Retrieves the list of domains approved to host embedded AI/BI dashboards. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Delete the list of domains approved to host embedded AI/BI dashboards, reverting back to the default empty list. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates the list of domains approved to host embedded AI/BI dashboards. This update will fail if the current workspace access policy is not ALLOW_APPROVED_DOMAINS. |

## `SELECT` examples

```sql
SELECT
aibi_dashboard_embedding_approved_domains,
etag,
setting_name
FROM databricks_workspace.workspace.dashboard_embedding_approved_domains
WHERE deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>dashboard_embedding_approved_domains</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.workspace.dashboard_embedding_approved_domains
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>dashboard_embedding_approved_domains</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.workspace.dashboard_embedding_approved_domains
WHERE deployment_name = '{{ deployment_name }}';
```
