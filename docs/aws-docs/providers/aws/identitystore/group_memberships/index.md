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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>group_membership</code> resource or lists <code>group_memberships</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS:IdentityStore::GroupMembership</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.identitystore.group_memberships" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>The unique identifier for a group in the identity store.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="IdentityStoreId, GroupId, MemberId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>group_memberships</code> in a region.
```sql
SELECT
region,
group_id,
identity_store_id,
member_id,
membership_id
FROM aws.identitystore.group_memberships
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>group_membership</code>.
```sql
SELECT
region,
group_id,
identity_store_id,
member_id,
membership_id
FROM aws.identitystore.group_memberships
WHERE region = 'us-east-1' AND data__Identifier = '<MembershipId>|<IdentityStoreId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>group_membership</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.identitystore.group_memberships (
 GroupId,
 IdentityStoreId,
 MemberId,
 region
)
SELECT 
'{{ GroupId }}',
 '{{ IdentityStoreId }}',
 '{{ MemberId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.identitystore.group_memberships (
 GroupId,
 IdentityStoreId,
 MemberId,
 region
)
SELECT 
 '{{ GroupId }}',
 '{{ IdentityStoreId }}',
 '{{ MemberId }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: group_membership
    props:
      - name: GroupId
        value: '{{ GroupId }}'
      - name: IdentityStoreId
        value: '{{ IdentityStoreId }}'
      - name: MemberId
        value:
          UserId: '{{ UserId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.identitystore.group_memberships
WHERE data__Identifier = '<MembershipId|IdentityStoreId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>group_memberships</code> resource, the following permissions are required:

### Create
```json
identitystore:CreateGroupMembership,
identitystore:DescribeGroupMembership
```

### Read
```json
identitystore:DescribeGroupMembership
```

### Delete
```json
identitystore:DeleteGroupMembership,
identitystore:DescribeGroupMembership
```

### List
```json
identitystore:ListGroupMemberships
```

