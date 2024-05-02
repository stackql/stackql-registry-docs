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
<tr><td><b>Description</b></td><td>Resource Type definition for SSO PermissionSet</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sso.permission_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name you want to assign to this permission set.</td></tr>
<tr><td><code>permission_set_arn</code></td><td><code>string</code></td><td>The permission set that the policy will be attached to</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The permission set description.</td></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The sso instance arn that the permission set is owned.</td></tr>
<tr><td><code>session_duration</code></td><td><code>string</code></td><td>The length of time that a user can be signed in to an AWS account.</td></tr>
<tr><td><code>relay_state_type</code></td><td><code>string</code></td><td>The relay state URL that redirect links to any service in the AWS Management Console.</td></tr>
<tr><td><code>managed_policies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>inline_policy</code></td><td><code>object</code></td><td>The inline policy to put in permission set.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>customer_managed_policy_references</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>permissions_boundary</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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

