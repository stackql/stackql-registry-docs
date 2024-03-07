---
title: resource_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policy
  - organizations
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resource_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.organizations.resource_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique identifier (ID) associated with this resource policy.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the resource policy.</td></tr>
<tr><td><code>content</code></td><td><code>object</code></td><td>The policy document. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags that you want to attach to the resource policy</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resource_policy</code> resource, the following permissions are required:

### Read
```json
organizations:DescribeResourcePolicy,
organizations:ListTagsForResource
```

### Update
```json
organizations:DescribeResourcePolicy,
organizations:PutResourcePolicy,
organizations:ListTagsForResource,
organizations:TagResource,
organizations:UntagResource
```

### Delete
```json
organizations:DeleteResourcePolicy
```


## Example
```sql
SELECT
region,
id,
arn,
content,
tags
FROM awscc.organizations.resource_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
