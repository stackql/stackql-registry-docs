---
title: permission_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_sets
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>permission_sets</code> in a region or create a <code>permission_sets</code> resource, use <code>permission_set</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for SSO PermissionSet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.permission_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The sso instance arn that the permission set is owned.</td></tr>
<tr><td><CopyableCode code="permission_set_arn" /></td><td><code>string</code></td><td>The permission set that the policy will be attached to</td></tr>
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
instance_arn,
permission_set_arn
FROM aws.sso.permission_sets
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>permission_sets</code> resource, the following permissions are required:

### Create
```json
sso:CreatePermissionSet,
sso:PutInlinePolicyToPermissionSet,
sso:AttachManagedPolicyToPermissionSet,
sso:AttachCustomerManagedPolicyReferenceToPermissionSet,
sso:PutPermissionsBoundaryToPermissionSet,
sso:TagResource,
sso:DescribePermissionSet,
sso:ListTagsForResource,
sso:ListManagedPoliciesInPermissionSet,
sso:ListCustomerManagedPolicyReferencesInPermissionSet,
sso:GetInlinePolicyForPermissionSet,
sso:GetPermissionsBoundaryForPermissionSet
```

### List
```json
sso:DescribePermissionSet
```

