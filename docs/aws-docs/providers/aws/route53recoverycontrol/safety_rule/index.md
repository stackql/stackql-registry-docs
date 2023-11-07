---
title: safety_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - safety_rule
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
Gets an individual <code>safety_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>safety_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>safety_rule</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53recoverycontrol.safety_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AssertionRule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>GatingRule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SafetyRuleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the safety rule.</td></tr>
<tr><td><code>ControlPanelArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the control panel.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><code>RuleConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.route53recoverycontrol.safety_rule<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;SafetyRuleArn&gt;'
</pre>
