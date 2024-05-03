---
title: group_memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - group_memberships
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

Used to retrieve a list of <code>group_memberships</code> in a region or create a <code>group_memberships</code> resource, use <code>group_membership</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS:IdentityStore::GroupMembership</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.identitystore.group_memberships" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="membership_id" /></td><td><code>string</code></td><td>The identifier for a GroupMembership in the identity store.</td></tr>
<tr><td><CopyableCode code="identity_store_id" /></td><td><code>string</code></td><td>The globally unique identifier for the identity store.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
membership_id,
identity_store_id
FROM aws.identitystore.group_memberships
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>group_memberships</code> resource, the following permissions are required:

### Create
```json
identitystore:CreateGroupMembership,
identitystore:DescribeGroupMembership
```

### List
```json
identitystore:ListGroupMemberships
```

