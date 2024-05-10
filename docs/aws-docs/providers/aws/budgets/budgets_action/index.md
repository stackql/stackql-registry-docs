---
title: budgets_action
hide_title: false
hide_table_of_contents: false
keywords:
  - budgets_action
  - budgets
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>budgets_action</code> resource, use <code>budgets_actions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>budgets_action</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.budgets.budgets_action" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="action_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="budget_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="notification_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="action_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="action_threshold" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="approval_model" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subscribers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
action_id,
budget_name,
notification_type,
action_type,
action_threshold,
execution_role_arn,
approval_model,
subscribers,
definition
FROM aws.budgets.budgets_action
WHERE region = 'us-east-1' AND data__Identifier = '<ActionId>|<BudgetName>';
```


## Permissions

To operate on the <code>budgets_action</code> resource, the following permissions are required:

### Read
```json
budgets:DescribeBudgetAction
```

### Update
```json
budgets:UpdateBudgetAction,
iam:PassRole
```

