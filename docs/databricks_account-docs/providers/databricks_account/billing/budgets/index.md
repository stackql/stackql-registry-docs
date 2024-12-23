---
title: budgets
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - budgets
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

Operations on a <code>budgets</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>budgets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.budgets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="alert_configurations" /> | `array` |
| <CopyableCode code="budget_configuration_id" /> | `string` |
| <CopyableCode code="create_time" /> | `integer` |
| <CopyableCode code="display_name" /> | `string` |
| <CopyableCode code="filter" /> | `object` |
| <CopyableCode code="update_time" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, budget_id" /> | Gets a budget configuration for an account. Both account and budget configuration are specified by ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets all budgets associated with this account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Create a new budget configuration for an account. For full details, see |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, budget_id" /> | Deletes a budget configuration for an account. Both account and budget configuration are specified by ID. This cannot be undone. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, budget_id" /> | Updates a budget configuration for an account. Both account and budget configuration are specified by ID. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'budgets (list)', value: 'list' },
        { label: 'budgets (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
account_id,
alert_configurations,
budget_configuration_id,
create_time,
display_name,
filter,
update_time
FROM databricks_account.billing.budgets
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
account_id,
alert_configurations,
budget_configuration_id,
create_time,
display_name,
filter,
update_time
FROM databricks_account.billing.budgets
WHERE account_id = '{{ account_id }}' AND
budget_id = '{{ budget_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>budgets</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'budgets', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.billing.budgets (
account_id,
data__budget
)
SELECT 
'{{ account_id }}',
'{{ budget }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: budget
    value:
      account_id: 449e7a5c-69d3-4b8a-aaaf-5c9b713ebc65
      alert_configurations:
      - time_period: MONTH
        trigger_type: CUMULATIVE_SPENDING_EXCEEDED
        quantity_type: LIST_PRICE_DOLLARS_USD
        quantity_threshold: string
        action_configurations:
        - action_type: EMAIL_NOTIFICATION
          target: string
      filter:
        workspace_id:
          operator: IN
          values:
          - 0
        tags:
        - key: string
          value:
            operator: IN
            values:
            - string
      display_name: string

```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>budgets</code> resource.

```sql
/*+ update */
REPLACE databricks_account.billing.budgets
SET { field = value }
WHERE account_id = '{{ account_id }}' AND
budget_id = '{{ budget_id }}';
```

## `DELETE` example

Deletes a <code>budgets</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.billing.budgets
WHERE account_id = '{{ account_id }}' AND
budget_id = '{{ budget_id }}';
```
