---
title: drt_accesses
hide_title: false
hide_table_of_contents: false
keywords:
  - drt_accesses
  - shield
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


Used to retrieve a list of <code>drt_accesses</code> in a region or to create or delete a <code>drt_accesses</code> resource, use <code>drt_access</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>drt_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Config the role and list of Amazon S3 log buckets used by the Shield Response Team (SRT) to access your AWS account while assisting with attack mitigation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.drt_accesses" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
account_id
FROM aws.shield.drt_accesses
;
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.shield.drt_accesses (
 RoleArn,
 region
)
SELECT 
{{ .RoleArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "LogBucketList": [
  "{{ LogBucketList[0] }}"
 ],
 "RoleArn": "{{ RoleArn }}"
}
>>>
--all properties
INSERT INTO aws.shield.drt_accesses (
 LogBucketList,
 RoleArn,
 region
)
SELECT 
 {{ .LogBucketList }},
 {{ .RoleArn }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.shield.drt_accesses
WHERE data__Identifier = '<AccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>drt_accesses</code> resource, the following permissions are required:

### Create
```json
shield:DescribeDRTAccess,
shield:AssociateDRTLogBucket,
shield:AssociateDRTRole,
iam:PassRole,
iam:GetRole,
iam:ListAttachedRolePolicies,
s3:GetBucketPolicy,
s3:PutBucketPolicy
```

### Delete
```json
shield:DescribeDRTAccess,
shield:DisassociateDRTLogBucket,
shield:DisassociateDRTRole,
iam:PassRole,
iam:GetRole,
iam:ListAttachedRolePolicies,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
s3:DeleteBucketPolicy
```

