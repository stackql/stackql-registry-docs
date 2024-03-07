---
title: template
hide_title: false
hide_table_of_contents: false
keywords:
  - template
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>template</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.quicksight.template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>permissions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>source_entity</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>template_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>validation_strategy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>version_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>template</code> resource, the following permissions are required:

### Read
<pre>
quicksight:DescribeTemplate,
quicksight:DescribeTemplatePermissions,
quicksight:ListTagsForResource</pre>

### Update
<pre>
quicksight:DescribeTemplate,
quicksight:DescribeTemplatePermissions,
quicksight:UpdateTemplate,
quicksight:UpdateTemplatePermissions,
quicksight:PassDataSet,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource</pre>

### Delete
<pre>
quicksight:DescribeTemplate,
quicksight:DeleteTemplate</pre>


## Example
```sql
SELECT
region,
arn,
aws_account_id,
created_time,
definition,
last_updated_time,
name,
permissions,
source_entity,
tags,
template_id,
validation_strategy,
version,
version_description
FROM awscc.quicksight.template
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AwsAccountId&gt;'
AND data__Identifier = '&lt;TemplateId&gt;'
```
