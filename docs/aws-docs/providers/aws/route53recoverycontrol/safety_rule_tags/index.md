---
title: safety_rule_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - safety_rule_tags
  - route53recoverycontrol
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

Expands all tag keys and values for <code>safety_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>safety_rule_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS Route53 Recovery Control basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoverycontrol.safety_rule_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="assertion_rule" /></td><td><code>object</code></td><td>An assertion rule enforces that, when a routing control state is changed, that the criteria set by the rule configuration is met. Otherwise, the change to the routing control is not accepted.</td></tr>
<tr><td><CopyableCode code="gating_rule" /></td><td><code>object</code></td><td>A gating rule verifies that a set of gating controls evaluates as true, based on a rule configuration that you specify. If the gating rule evaluates to true, Amazon Route 53 Application Recovery Controller allows a set of routing control state changes to run and complete against the set of target controls.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the safety rule.</td></tr>
<tr><td><CopyableCode code="safety_rule_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the safety rule.</td></tr>
<tr><td><CopyableCode code="control_panel_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the control panel.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><CopyableCode code="rule_config" /></td><td><code>object</code></td><td>The rule configuration for an assertion rule or gating rule. This is the criteria that you set for specific assertion controls (routing controls) or gating controls. This configuration specifies how many controls must be enabled after a transaction completes.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>safety_rules</code> in a region.
```sql
SELECT
region,
assertion_rule,
gating_rule,
name,
safety_rule_arn,
control_panel_arn,
status,
rule_config,
tag_key,
tag_value
FROM aws.route53recoverycontrol.safety_rule_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>safety_rule_tags</code> resource, see <a href="/providers/aws/route53recoverycontrol/safety_rules/#permissions"><code>safety_rules</code></a>

