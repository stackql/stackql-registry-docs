---
title: listener_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - listener_rule
  - elasticloadbalancingv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>listener_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listener_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>listener_rule</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticloadbalancingv2.listener_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>listener_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rule_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>actions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>conditions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>is_default</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
listener_arn,
rule_arn,
actions,
priority,
conditions,
is_default
FROM awscc.elasticloadbalancingv2.listener_rule
WHERE data__Identifier = '<RuleArn>';
```

## Permissions

To operate on the <code>listener_rule</code> resource, the following permissions are required:

### Delete
```json
elasticloadbalancing:DeleteRule,
elasticloadbalancing:DescribeRules
```

### Read
```json
elasticloadbalancing:DescribeRules
```

### Update
```json
elasticloadbalancing:ModifyRule,
elasticloadbalancing:SetRulePriorities,
elasticloadbalancing:DescribeRules
```

