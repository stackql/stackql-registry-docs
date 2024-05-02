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
<tr><td><b>Description</b></td><td>Specifies a listener rule. The listener must be associated with an Application Load Balancer. Each rule consists of a priority, one or more actions, and one or more conditions.&lt;br&#x2F;&gt; For more information, see &#91;Quotas for your Application Load Balancers&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;elasticloadbalancing&#x2F;latest&#x2F;application&#x2F;load-balancer-limits.html) in the *User Guide for Application Load Balancers*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancingv2.listener_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>listener_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the listener.</td></tr>
<tr><td><code>rule_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>actions</code></td><td><code>array</code></td><td>The actions.&lt;br&#x2F;&gt; The rule must include exactly one of the following types of actions: ``forward``, ``fixed-response``, or ``redirect``, and it must be the last action to be performed. If the rule is for an HTTPS listener, it can also optionally include an authentication action.</td></tr>
<tr><td><code>priority</code></td><td><code>integer</code></td><td>The rule priority. A listener can't have multiple rules with the same priority.&lt;br&#x2F;&gt; If you try to reorder rules by updating their priorities, do not specify a new priority if an existing rule already uses this priority, as this can cause an error. If you need to reuse a priority with a different rule, you must remove it as a priority first, and then specify it in a subsequent update.</td></tr>
<tr><td><code>conditions</code></td><td><code>array</code></td><td>The conditions.&lt;br&#x2F;&gt; The rule can optionally include up to one of each of the following conditions: ``http-request-method``, ``host-header``, ``path-pattern``, and ``source-ip``. A rule can also optionally include one or more of each of the following conditions: ``http-header`` and ``query-string``.</td></tr>
<tr><td><code>is_default</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
listener_arn,
rule_arn,
actions,
priority,
conditions,
is_default
FROM aws.elasticloadbalancingv2.listener_rule
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

