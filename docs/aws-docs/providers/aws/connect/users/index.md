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
<tr><td><b>Id</b></td><td><code>aws.connect.users</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>InstanceArn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><code>DirectoryUserId</code></td><td><code>string</code></td><td>The identifier of the user account in the directory used for identity management.</td></tr>
<tr><td><code>HierarchyGroupArn</code></td><td><code>string</code></td><td>The identifier of the hierarchy group for the user.</td></tr>
<tr><td><code>Username</code></td><td><code>string</code></td><td>The user name for the account.</td></tr>
<tr><td><code>Password</code></td><td><code>string</code></td><td>The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password.</td></tr>
<tr><td><code>RoutingProfileArn</code></td><td><code>string</code></td><td>The identifier of the routing profile for the user.</td></tr>
<tr><td><code>IdentityInfo</code></td><td><code>object</code></td><td>The information about the identity of the user.</td></tr>
<tr><td><code>PhoneConfig</code></td><td><code>object</code></td><td>The phone settings for the user.</td></tr>
<tr><td><code>SecurityProfileArns</code></td><td><code>array</code></td><td>One or more security profile arns for the user</td></tr>
<tr><td><code>UserArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the user.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.connect.users<br/>WHERE region = 'us-east-1'
</pre>
