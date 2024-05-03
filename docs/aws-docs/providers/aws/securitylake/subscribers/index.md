---
title: subscribers
hide_title: false
hide_table_of_contents: false
keywords:
  - subscribers
  - securitylake
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

Used to retrieve a list of <code>subscribers</code> in a region or create a <code>subscribers</code> resource, use <code>subscriber</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscribers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SecurityLake::Subscriber</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securitylake.subscribers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="subscriber_arn" /></td><td><code>string</code></td><td></td></tr>
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
subscriber_arn
FROM aws.securitylake.subscribers
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>subscribers</code> resource, the following permissions are required:

### Create
```json
securitylake:CreateSubscriber,
securitylake:CreateCustomLogSource,
securitylake:CreateDataLake,
securitylake:TagResource,
securitylake:GetSubscriber,
securitylake:ListTagsForResource,
iam:GetRole,
iam:GetRolePolicy,
iam:PutRolePolicy,
iam:CreateRole,
iam:CreateServiceLinkedRole,
glue:GetDatabase,
glue:GetTable,
lakeformation:RegisterResource,
lakeformation:GrantPermissions,
lakeformation:RevokePermissions,
lakeformation:ListPermissions,
ram:GetResourceShareAssociations,
ram:CreateResourceShare,
ram:UpdateResourceShare,
ram:GetResourceShares
```

### List
```json
securitylake:ListSubscribers
```

