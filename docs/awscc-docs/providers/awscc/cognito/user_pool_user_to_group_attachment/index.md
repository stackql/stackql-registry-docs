---
title: user_pool_user_to_group_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_user_to_group_attachment
  - cognito
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>user_pool_user_to_group_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_user_to_group_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_pool_user_to_group_attachment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cognito.user_pool_user_to_group_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>username</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>user_pool_user_to_group_attachment</code> resource, the following permissions are required:

### Delete
<pre>
cognito-idp:AdminRemoveUserFromGroup,
cognito-idp:AdminListGroupsForUser</pre>

### Read
<pre>
cognito-idp:AdminListGroupsForUser</pre>


## Example
```sql
SELECT
region,
user_pool_id,
username,
group_name
FROM awscc.cognito.user_pool_user_to_group_attachment
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;UserPoolId&gt;'
AND data__Identifier = '&lt;GroupName&gt;'
AND data__Identifier = '&lt;Username&gt;'
```
