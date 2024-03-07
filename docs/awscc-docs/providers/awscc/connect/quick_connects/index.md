---
title: quick_connects
hide_title: false
hide_table_of_contents: false
keywords:
  - quick_connects
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
Retrieves a list of <code>quick_connects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quick_connects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>quick_connects</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.quick_connects</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>quick_connect_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the quick connect.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>quick_connects</code> resource, the following permissions are required:

### Create
<pre>
connect:CreateQuickConnect,
connect:TagResource</pre>

### List
<pre>
connect:ListQuickConnects</pre>


## Example
```sql
SELECT
region,
quick_connect_arn
FROM awscc.connect.quick_connects
WHERE region = 'us-east-1'
```
