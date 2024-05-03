---
title: user_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pools
  - cognito
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

Used to retrieve a list of <code>user_pools</code> in a region or create a <code>user_pools</code> resource, use <code>user_pool</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPool</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pools" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
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
user_pool_id
FROM aws.cognito.user_pools
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>user_pools</code> resource, the following permissions are required:

### Create
```json
cognito-idp:CreateUserPool,
iam:PassRole,
cognito-idp:SetUserPoolMfaConfig,
cognito-idp:DescribeUserPool,
kms:CreateGrant,
iam:CreateServiceLinkedRole
```

### List
```json
cognito-idp:ListUserPools
```

