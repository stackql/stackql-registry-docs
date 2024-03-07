---
title: index
hide_title: false
hide_table_of_contents: false
keywords:
  - index
  - kendra
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>index</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>index</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>index</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kendra.index</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description for the index</td></tr>
<tr><td><code>server_side_encryption_configuration</code></td><td><code>object</code></td><td>Server side encryption configuration</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags for labeling the index</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>edition</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>document_metadata_configurations</code></td><td><code>array</code></td><td>Document metadata configurations</td></tr>
<tr><td><code>capacity_units</code></td><td><code>object</code></td><td>Capacity units</td></tr>
<tr><td><code>user_context_policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_token_configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>index</code> resource, the following permissions are required:

### Read
<pre>
kendra:DescribeIndex,
kendra:ListTagsForResource</pre>

### Update
<pre>
kendra:DescribeIndex,
kendra:UpdateIndex,
kendra:ListTagsForResource,
kendra:TagResource,
kendra:UntagResource,
iam:PassRole</pre>

### Delete
<pre>
kendra:DescribeIndex,
kendra:DeleteIndex</pre>


## Example
```sql
SELECT
region,
id,
arn,
description,
server_side_encryption_configuration,
tags,
name,
role_arn,
edition,
document_metadata_configurations,
capacity_units,
user_context_policy,
user_token_configurations
FROM awscc.kendra.index
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
