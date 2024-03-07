---
title: budgets_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - budgets_actions
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
Retrieves a list of <code>budgets_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>budgets_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>budgets_actions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.budgets.budgets_actions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>action_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>budget_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
action_id,
budget_name
FROM awscc.budgets.budgets_actions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>budgets_actions</code> resource, the following permissions are required:

### Create
```json
budgets:CreateBudgetAction,
iam:PassRole
```

### List
```json
budgets:DescribeBudgetActionsForAccount,
budgets:DescribeBudgetActionsForBudget
```

