---
title: usage_dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - usage_dashboards
  - billing
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

Operations on a <code>usage_dashboards</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.usage_dashboards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="dashboard_id" /> | `string` |
| <CopyableCode code="dashboard_url" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id" /> | Get a usage dashboard specified by workspaceId, accountId, and dashboard type. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Create a usage dashboard specified by workspaceId, accountId, and dashboard type. |

## `SELECT` examples

```sql
SELECT
dashboard_id,
dashboard_url
FROM databricks_account.billing.usage_dashboards
WHERE account_id = '{{ account_id }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>usage_dashboards</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'usage_dashboards', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.billing.usage_dashboards (
account_id,
data__workspace_id,
data__dashboard_type
)
SELECT 
'{{ account_id }}',
'{{ workspace_id }}',
'{{ dashboard_type }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: workspace_id
    value: 0
  - name: dashboard_type
    value: USAGE_DASHBOARD_TYPE_WORKSPACE

```

</TabItem>
</Tabs>
