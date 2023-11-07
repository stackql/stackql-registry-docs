---
title: permission_set
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_set
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
Gets an individual <code>permission_set</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>permission_set</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sso.permission_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name you want to assign to this permission set.</td></tr>
<tr><td><code>PermissionSetArn</code></td><td><code>string</code></td><td>The permission set that the policy will be attached to</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The permission set description.</td></tr>
<tr><td><code>InstanceArn</code></td><td><code>string</code></td><td>The sso instance arn that the permission set is owned.</td></tr>
<tr><td><code>SessionDuration</code></td><td><code>string</code></td><td>The length of time that a user can be signed in to an AWS account.</td></tr>
<tr><td><code>RelayStateType</code></td><td><code>string</code></td><td>The relay state URL that redirect links to any service in the AWS Management Console.</td></tr>
<tr><td><code>ManagedPolicies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>InlinePolicy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>CustomerManagedPolicyReferences</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>PermissionsBoundary</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.sso.permission_set<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;InstanceArn&gt;'<br/>AND data__Identifier = '&lt;PermissionSetArn&gt;'
</pre>
