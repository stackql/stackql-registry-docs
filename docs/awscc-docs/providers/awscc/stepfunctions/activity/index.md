---
title: activity
hide_title: false
hide_table_of_contents: false
keywords:
  - activity
  - stepfunctions
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>activity</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>activity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>activity</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.stepfunctions.activity</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>activity</code> resource, the following permissions are required:

### Read
```json
states:DescribeActivity,
states:ListTagsForResource
```

### Update
```json
states:ListTagsForResource,
states:TagResource,
states:UntagResource
```

### Delete
```json
states:DeleteActivity
```


## Example
```sql
SELECT
region,
arn,
name,
tags
FROM awscc.stepfunctions.activity
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
