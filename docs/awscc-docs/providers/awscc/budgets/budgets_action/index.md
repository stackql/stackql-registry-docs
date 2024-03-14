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
Gets an individual <code>budgets_action</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>budgets_action</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>budgets_action</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.budgets.budgets_action</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>action_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>budget_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>notification_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>action_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>action_threshold</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>execution_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>approval_model</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subscribers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.budgets.budgets_action
WHERE data__Identifier = '<ActionId>|<BudgetName>';
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

### Delete
```json
budgets:DeleteBudgetAction
```

