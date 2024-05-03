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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>permission_set</code> resource, use <code>permission_sets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for SSO PermissionSet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.permission_set" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this permission set.</td></tr>
<tr><td><CopyableCode code="permission_set_arn" /></td><td><code>string</code></td><td>The permission set that the policy will be attached to</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The permission set description.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The sso instance arn that the permission set is owned.</td></tr>
<tr><td><CopyableCode code="session_duration" /></td><td><code>string</code></td><td>The length of time that a user can be signed in to an AWS account.</td></tr>
<tr><td><CopyableCode code="relay_state_type" /></td><td><code>string</code></td><td>The relay state URL that redirect links to any service in the AWS Management Console.</td></tr>
<tr><td><CopyableCode code="managed_policies" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="inline_policy" /></td><td><code>object</code></td><td>The inline policy to put in permission set.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_policy_references" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions_boundary" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
name,
permission_set_arn,
description,
instance_arn,
session_duration,
relay_state_type,
managed_policies,
inline_policy,
tags,
customer_managed_policy_references,
permissions_boundary
FROM aws.sso.permission_set
WHERE data__Identifier = '<InstanceArn>|<PermissionSetArn>';
```

## Permissions

To operate on the <code>permission_set</code> resource, the following permissions are required:

### Read
```json
sso:DescribePermissionSet,
sso:ListTagsForResource,
sso:ListManagedPoliciesInPermissionSet,
sso:ListCustomerManagedPolicyReferencesInPermissionSet,
sso:GetInlinePolicyForPermissionSet,
sso:GetPermissionsBoundaryForPermissionSet
```

### Update
```json
sso:UpdatePermissionSet,
sso:TagResource,
sso:UntagResource,
sso:ListTagsForResource,
sso:AttachManagedPolicyToPermissionSet,
sso:AttachCustomerManagedPolicyReferenceToPermissionSet,
sso:DetachManagedPolicyFromPermissionSet,
sso:DetachCustomerManagedPolicyReferenceFromPermissionSet,
sso:ListManagedPoliciesInPermissionSet,
sso:ListCustomerManagedPolicyReferencesInPermissionSet,
sso:PutInlinePolicyToPermissionSet,
sso:GetPermissionsBoundaryForPermissionSet,
sso:DeletePermissionsBoundaryFromPermissionSet,
sso:PutPermissionsBoundaryToPermissionSet,
sso:DeleteInlinePolicyFromPermissionSet,
sso:ProvisionPermissionSet,
sso:DescribePermissionSet,
sso:GetInlinePolicyForPermissionSet,
sso:DescribePermissionSetProvisioningStatus
```

### Delete
```json
sso:DeletePermissionSet
```

