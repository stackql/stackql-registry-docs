---
title: quick_connect
hide_title: false
hide_table_of_contents: false
keywords:
  - quick_connect
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
Gets an individual <code>quick_connect</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quick_connect</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>quick_connect</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.quick_connect</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the quick connect.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the quick connect.</td></tr>
<tr><td><code>quick_connect_config</code></td><td><code>object</code></td><td>Configuration settings for the quick connect.</td></tr>
<tr><td><code>quick_connect_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the quick connect.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><code>quick_connect_type</code></td><td><code>string</code></td><td>The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>quick_connect</code> resource, the following permissions are required:

### Read
<pre>
connect:DescribeQuickConnect</pre>

### Delete
<pre>
connect:DeleteQuickConnect,
connect:UntagResource</pre>

### Update
<pre>
connect:UpdateQuickConnectName,
connect:UpdateQuickConnectConfig,
connect:TagResource,
connect:UntagResource</pre>


## Example
```sql
SELECT
region,
instance_arn,
name,
description,
quick_connect_config,
quick_connect_arn,
tags,
quick_connect_type
FROM awscc.connect.quick_connect
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;QuickConnectArn&gt;'
```
