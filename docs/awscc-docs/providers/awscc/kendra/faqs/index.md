---
title: faqs
hide_title: false
hide_table_of_contents: false
keywords:
  - faqs
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
Retrieves a list of <code>faqs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>faqs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>faqs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kendra.faqs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>index_id</code></td><td><code>undefined</code></td><td>Index ID</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>faqs</code> resource, the following permissions are required:

### Create
<pre>
kendra:CreateFaq,
kendra:DescribeFaq,
iam:PassRole,
kendra:ListTagsForResource,
kendra:TagResource</pre>

### List
<pre>
kendra:ListFaqs</pre>


## Example
```sql
SELECT
region,
id,
index_id
FROM awscc.kendra.faqs
WHERE region = 'us-east-1'
```
