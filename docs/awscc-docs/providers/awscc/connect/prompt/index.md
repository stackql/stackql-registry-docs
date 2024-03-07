---
title: prompt
hide_title: false
hide_table_of_contents: false
keywords:
  - prompt
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
Gets an individual <code>prompt</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prompt</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>prompt</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.prompt</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the prompt.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the prompt.</td></tr>
<tr><td><code>s3_uri</code></td><td><code>string</code></td><td>S3 URI of the customer's audio file for creating prompts resource..</td></tr>
<tr><td><code>prompt_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the prompt.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>prompt</code> resource, the following permissions are required:

### Read
<pre>
connect:DescribePrompt</pre>

### Update
<pre>
connect:UpdatePrompt,
connect:TagResource,
connect:UntagResource</pre>

### Delete
<pre>
connect:DeletePrompt</pre>


## Example
```sql
SELECT
region,
instance_arn,
name,
description,
s3_uri,
prompt_arn,
tags
FROM awscc.connect.prompt
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;PromptArn&gt;'
```
