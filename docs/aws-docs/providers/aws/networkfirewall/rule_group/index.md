---
title: rule_group
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_group
  - networkfirewall
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>rule_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rule_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkfirewall.rule_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RuleGroupName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RuleGroupArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RuleGroupId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RuleGroup</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.networkfirewall.rule_group<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;RuleGroupArn&gt;'
</pre>
