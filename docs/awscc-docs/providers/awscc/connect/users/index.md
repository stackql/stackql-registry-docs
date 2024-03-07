---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
Retrieves a list of <code>users</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>users</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.users</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>user_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the user.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>users</code> resource, the following permissions are required:

### Create
```json
connect:CreateUser,
connect:TagResource,
connect:AssociateUserProficiencies
```

### List
```json
connect:ListUsers
```


## Example
```sql
SELECT
region,
user_arn
FROM awscc.connect.users
WHERE region = 'us-east-1'
```
