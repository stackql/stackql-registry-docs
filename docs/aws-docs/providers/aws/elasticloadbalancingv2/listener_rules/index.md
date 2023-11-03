---
title: listener_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - listener_rules
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
Retrieves a list of <code>listener_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listener_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancingv2.listener_rules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ListenerArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RuleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Actions</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Priority</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>Conditions</code></td><td><code>array</code></td><td></td></tr><tr><td><code>IsDefault</code></td><td><code>boolean</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.elasticloadbalancingv2.listener_rules
WHERE region = 'us-east-1'
```
