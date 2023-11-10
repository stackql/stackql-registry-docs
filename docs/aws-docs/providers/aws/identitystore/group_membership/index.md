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
<tr><td><code>group_id</code></td><td><code>string</code></td><td>The unique identifier for a group in the identity store.</td></tr>
<tr><td><code>identity_store_id</code></td><td><code>string</code></td><td>The globally unique identifier for the identity store.</td></tr>
<tr><td><code>member_id</code></td><td><code>object</code></td><td>An object containing the identifier of a group member.</td></tr>
<tr><td><code>membership_id</code></td><td><code>string</code></td><td>The identifier for a GroupMembership in the identity store.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
group_id,
identity_store_id,
member_id,
membership_id
FROM aws.identitystore.group_membership
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;MembershipId&gt;'
AND data__Identifier = '&lt;IdentityStoreId&gt;'
```
