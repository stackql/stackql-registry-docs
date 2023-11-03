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
<tr><td><b>Id</b></td><td><code>aws.budgets.budgets_action</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ActionId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BudgetName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NotificationType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ActionType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ActionThreshold</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ExecutionRoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApprovalModel</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Subscribers</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Definition</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.budgets.budgets_action
WHERE region = 'us-east-1' AND data__Identifier = '{ActionId}' AND data__Identifier = '{BudgetName}'
</pre>
