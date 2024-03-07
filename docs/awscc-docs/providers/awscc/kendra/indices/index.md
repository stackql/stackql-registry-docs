---
title: indices
hide_title: false
hide_table_of_contents: false
keywords:
  - indices
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
Retrieves a list of <code>indices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>indices</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kendra.indices</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>indices</code> resource, the following permissions are required:

### Create
<pre>
kendra:CreateIndex,
kendra:DescribeIndex,
kendra:UpdateIndex,
kendra:ListTagsForResource,
iam:PassRole,
kendra:TagResource</pre>

### List
<pre>
kendra:ListIndices</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.kendra.indices
WHERE region = 'us-east-1'
```
