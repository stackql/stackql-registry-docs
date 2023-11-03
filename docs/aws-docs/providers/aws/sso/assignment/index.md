---
title: assignment
hide_title: false
hide_table_of_contents: false
keywords:
  - assignment
  - sso
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>assignment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.sso.assignment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>InstanceArn</code></td><td><code>string</code></td><td>The sso instance that the permission set is owned.</td></tr><tr><td><code>TargetId</code></td><td><code>string</code></td><td>The account id to be provisioned.</td></tr><tr><td><code>TargetType</code></td><td><code>string</code></td><td>The type of resource to be provsioned to, only aws account now</td></tr><tr><td><code>PermissionSetArn</code></td><td><code>string</code></td><td>The permission set that the assignemt will be assigned</td></tr><tr><td><code>PrincipalType</code></td><td><code>string</code></td><td>The assignee's type, user/group</td></tr><tr><td><code>PrincipalId</code></td><td><code>string</code></td><td>The assignee's identifier, user id/group id</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sso.assignment
WHERE region = 'us-east-1' AND data__Identifier = '<InstanceArn>' AND data__Identifier = '<TargetId>' AND data__Identifier = '<TargetType>' AND data__Identifier = '<PermissionSetArn>' AND data__Identifier = '<PrincipalType>' AND data__Identifier = '<PrincipalId>'
</pre>
