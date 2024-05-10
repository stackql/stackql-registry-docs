---
title: assignment
hide_title: false
hide_table_of_contents: false
keywords:
  - assignment
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>assignment</code> resource, use <code>assignments</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for SSO assignmet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.assignment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The sso instance that the permission set is owned.</td></tr>
<tr><td><CopyableCode code="target_id" /></td><td><code>string</code></td><td>The account id to be provisioned.</td></tr>
<tr><td><CopyableCode code="target_type" /></td><td><code>string</code></td><td>The type of resource to be provsioned to, only aws account now</td></tr>
<tr><td><CopyableCode code="permission_set_arn" /></td><td><code>string</code></td><td>The permission set that the assignemt will be assigned</td></tr>
<tr><td><CopyableCode code="principal_type" /></td><td><code>string</code></td><td>The assignee's type, user&#x2F;group</td></tr>
<tr><td><CopyableCode code="principal_id" /></td><td><code>string</code></td><td>The assignee's identifier, user id&#x2F;group id</td></tr>
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
instance_arn,
target_id,
target_type,
permission_set_arn,
principal_type,
principal_id
FROM aws.sso.assignment
WHERE region = 'us-east-1' AND data__Identifier = '<InstanceArn>|<TargetId>|<TargetType>|<PermissionSetArn>|<PrincipalType>|<PrincipalId>';
```


## Permissions

To operate on the <code>assignment</code> resource, the following permissions are required:

### Read
```json
sso:ListAccountAssignments,
iam:GetSAMLProvider,
iam:ListRolePolicies
```

