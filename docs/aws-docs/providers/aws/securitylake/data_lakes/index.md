---
title: data_lakes
hide_title: false
hide_table_of_contents: false
keywords:
  - data_lakes
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>data_lakes</code> in a region or to create or delete a <code>data_lakes</code> resource, use <code>data_lake</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_lakes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SecurityLake::DataLake</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securitylake.data_lakes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) created by you to provide to the subscriber.</td></tr>
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
arn
FROM aws.securitylake.data_lakes
WHERE region = 'us-east-1';
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
 "EncryptionConfiguration": {
  "KmsKeyId": "{{ KmsKeyId }}"
 },
 "LifecycleConfiguration": {
  "Expiration": {
   "Days": "{{ Days }}"
  },
  "Transitions": [
   {
    "Days": "{{ Days }}",
    "StorageClass": "{{ StorageClass }}"
   }
  ]
 },
 "ReplicationConfiguration": {
  "Regions": [
   "{{ Regions[0] }}"
  ],
  "RoleArn": "{{ RoleArn }}"
 },
 "MetaStoreManagerRoleArn": "{{ MetaStoreManagerRoleArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.securitylake.data_lakes (
 EncryptionConfiguration,
 LifecycleConfiguration,
 ReplicationConfiguration,
 MetaStoreManagerRoleArn,
 Tags,
 region
)
SELECT 
{{ .EncryptionConfiguration }},
 {{ .LifecycleConfiguration }},
 {{ .ReplicationConfiguration }},
 {{ .MetaStoreManagerRoleArn }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "EncryptionConfiguration": {
  "KmsKeyId": "{{ KmsKeyId }}"
 },
 "LifecycleConfiguration": {
  "Expiration": {
   "Days": "{{ Days }}"
  },
  "Transitions": [
   {
    "Days": "{{ Days }}",
    "StorageClass": "{{ StorageClass }}"
   }
  ]
 },
 "ReplicationConfiguration": {
  "Regions": [
   "{{ Regions[0] }}"
  ],
  "RoleArn": "{{ RoleArn }}"
 },
 "MetaStoreManagerRoleArn": "{{ MetaStoreManagerRoleArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.securitylake.data_lakes (
 EncryptionConfiguration,
 LifecycleConfiguration,
 ReplicationConfiguration,
 MetaStoreManagerRoleArn,
 Tags,
 region
)
SELECT 
 {{ .EncryptionConfiguration }},
 {{ .LifecycleConfiguration }},
 {{ .ReplicationConfiguration }},
 {{ .MetaStoreManagerRoleArn }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.securitylake.data_lakes
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_lakes</code> resource, the following permissions are required:

### Create
```json
events:*,
iam:CreateServiceLinkedRole,
iam:GetRole,
iam:ListAttachedRolePolicies,
iam:PutRolePolicy,
iam:PassRole,
glue:*,
organizations:*,
kms:DescribeKey,
kms:CreateGrant,
lakeformation:*,
lambda:*,
s3:*,
securitylake:CreateDataLake,
securitylake:TagResource,
securitylake:List*,
sqs:*
```

### Delete
```json
organizations:*,
securitylake:DeleteDataLake,
securitylake:List*
```

### List
```json
securitylake:List*
```

