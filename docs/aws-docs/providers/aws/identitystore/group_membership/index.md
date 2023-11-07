---
title: group_membership
hide_title: false
hide_table_of_contents: false
keywords:
  - group_membership
  - identitystore
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>group_membership</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_membership</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>group_membership</td></tr>
<tr><td><b>Id</b></td><td><code>aws.identitystore.group_membership</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>GroupId</code></td><td><code>string</code></td><td>The unique identifier for a group in the identity store.</td></tr>
<tr><td><code>IdentityStoreId</code></td><td><code>string</code></td><td>The globally unique identifier for the identity store.</td></tr>
<tr><td><code>MemberId</code></td><td><code>object</code></td><td>An object containing the identifier of a group member.</td></tr>
<tr><td><code>MembershipId</code></td><td><code>string</code></td><td>The identifier for a GroupMembership in the identity store.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.identitystore.group_membership<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;MembershipId&gt;'<br/>AND data__Identifier = '&lt;IdentityStoreId&gt;'
</pre>
