---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - events
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
<tr><td><b>Description</b></td><td>rules</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.events.rules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the rule, such as arn:aws:events:us-east-2:123456789012:rule&#x2F;example.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>rules</code> resource, the following permissions are required:

### Create
<pre>
iam:PassRole,
events:DescribeRule,
events:PutRule,
events:PutTargets</pre>

### List
<pre>
events:ListRules</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.events.rules
WHERE region = 'us-east-1'
```
