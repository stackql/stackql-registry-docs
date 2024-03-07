---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
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
Gets an individual <code>account</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>account</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.organizations.account</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_name</code></td><td><code>string</code></td><td>The friendly name of the member account.</td></tr>
<tr><td><code>email</code></td><td><code>string</code></td><td>The email address of the owner to assign to the new member account.</td></tr>
<tr><td><code>role_name</code></td><td><code>string</code></td><td>The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.</td></tr>
<tr><td><code>parent_ids</code></td><td><code>array</code></td><td>List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value.</td></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>If the account was created successfully, the unique identifier (ID) of the new account.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the account.</td></tr>
<tr><td><code>joined_method</code></td><td><code>string</code></td><td>The method by which the account joined the organization.</td></tr>
<tr><td><code>joined_timestamp</code></td><td><code>string</code></td><td>The date the account became a part of the organization.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the account in the organization.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>account</code> resource, the following permissions are required:

### Read
<pre>
organizations:DescribeAccount,
organizations:ListParents,
organizations:ListTagsForResource</pre>

### Update
<pre>
organizations:MoveAccount,
organizations:TagResource,
organizations:UntagResource,
organizations:ListRoots,
organizations:DescribeAccount,
organizations:ListParents,
organizations:ListTagsForResource</pre>

### Delete
<pre>
organizations:CloseAccount</pre>


## Example
```sql
SELECT
region,
account_name,
email,
role_name,
parent_ids,
tags,
account_id,
arn,
joined_method,
joined_timestamp,
status
FROM awscc.organizations.account
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AccountId&gt;'
```
