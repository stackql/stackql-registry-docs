---
title: listener_rules_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - listener_rules_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>listener_rules</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/listener_rules/"><code>listener_rules</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listener_rules_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a listener rule. The listener must be associated with an Application Load Balancer. Each rule consists of a priority, one or more actions, and one or more conditions.<br />For more information, see &#91;Quotas for your Application Load Balancers&#93;(https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html) in the *User Guide for Application Load Balancers*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.listener_rules_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="listener_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the listener.</td></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td>The actions.<br />The rule must include exactly one of the following types of actions: <code>forward</code>, <code>fixed-response</code>, or <code>redirect</code>, and it must be the last action to be performed. If the rule is for an HTTPS listener, it can also optionally include an authentication action.</td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td>The rule priority. A listener can't have multiple rules with the same priority.<br />If you try to reorder rules by updating their priorities, do not specify a new priority if an existing rule already uses this priority, as this can cause an error. If you need to reuse a priority with a different rule, you must remove it as a priority first, and then specify it in a subsequent update.</td></tr>
<tr><td><CopyableCode code="conditions" /></td><td><code>array</code></td><td>The conditions.<br />The rule can optionally include up to one of each of the following conditions: <code>http-request-method</code>, <code>host-header</code>, <code>path-pattern</code>, and <code>source-ip</code>. A rule can also optionally include one or more of each of the following conditions: <code>http-header</code> and <code>query-string</code>.</td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>listener_rules</code> in a region.
```sql
SELECT
region,
rule_arn
FROM aws.elasticloadbalancingv2.listener_rules_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>listener_rules_list_only</code> resource, see <a href="/providers/aws/elasticloadbalancingv2/listener_rules/#permissions"><code>listener_rules</code></a>


