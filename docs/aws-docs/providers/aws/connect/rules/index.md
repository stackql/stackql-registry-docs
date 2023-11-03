---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.rules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the rule.</td></tr><tr><td><code>RuleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the rule.</td></tr><tr><td><code>InstanceArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the instance.</td></tr><tr><td><code>TriggerEventSource</code></td><td><code>undefined</code></td><td>The event source that triggers the rule.</td></tr><tr><td><code>Function</code></td><td><code>string</code></td><td>The conditions of a rule.</td></tr><tr><td><code>Actions</code></td><td><code>undefined</code></td><td>The list of actions that will be executed when a rule is triggered.</td></tr><tr><td><code>PublishStatus</code></td><td><code>string</code></td><td>The publish status of a rule, either draft or published.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.connect.rules
WHERE region = 'us-east-1'
```
