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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>group_membership</code> resource, use <code>group_memberships</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_membership</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS:IdentityStore::GroupMembership</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.identitystore.group_membership" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>The unique identifier for a group in the identity store.</td></tr>
<tr><td><CopyableCode code="identity_store_id" /></td><td><code>string</code></td><td>The globally unique identifier for the identity store.</td></tr>
<tr><td><CopyableCode code="member_id" /></td><td><code>object</code></td><td>An object containing the identifier of a group member.</td></tr>
<tr><td><CopyableCode code="membership_id" /></td><td><code>string</code></td><td>The identifier for a GroupMembership in the identity store.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
group_id,
identity_store_id,
member_id,
membership_id
FROM aws.identitystore.group_membership
WHERE region = 'us-east-1' AND data__Identifier = '<MembershipId>|<IdentityStoreId>';
```


## Permissions

To operate on the <code>group_membership</code> resource, the following permissions are required:

### Read
```json
identitystore:DescribeGroupMembership
```

