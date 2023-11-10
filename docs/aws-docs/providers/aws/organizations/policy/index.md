---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
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
Gets an individual <code>policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>policy</td></tr>
<tr><td><b>Id</b></td><td><code>aws.organizations.policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the Policy</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of policy to create. You can specify one of the following values: AISERVICES_OPT_OUT_POLICY, BACKUP_POLICY, SERVICE_CONTROL_POLICY, TAG_POLICY</td></tr>
<tr><td><code>content</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Human readable description of the policy</td></tr>
<tr><td><code>target_ids</code></td><td><code>array</code></td><td>List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id of the Policy</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>ARN of the Policy</td></tr>
<tr><td><code>aws_managed</code></td><td><code>boolean</code></td><td>A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
type,
content,
description,
target_ids,
tags,
id,
arn,
aws_managed
FROM aws.organizations.policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
