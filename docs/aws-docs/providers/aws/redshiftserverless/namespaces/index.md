---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - redshiftserverless
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


Used to retrieve a list of <code>namespaces</code> in a region or to create or delete a <code>namespaces</code> resource, use <code>namespace</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RedshiftServerless::Namespace Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshiftserverless.namespaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="namespace_name" /></td><td><code>string</code></td><td>A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.</td></tr>
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
namespace_name
FROM aws.redshiftserverless.namespaces
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
 "NamespaceName": "{{ NamespaceName }}"
}
>>>
--required properties only
INSERT INTO aws.redshiftserverless.namespaces (
 NamespaceName,
 region
)
SELECT 
{{ NamespaceName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AdminPasswordSecretKmsKeyId": "{{ AdminPasswordSecretKmsKeyId }}",
 "AdminUserPassword": "{{ AdminUserPassword }}",
 "AdminUsername": "{{ AdminUsername }}",
 "DbName": "{{ DbName }}",
 "DefaultIamRoleArn": "{{ DefaultIamRoleArn }}",
 "IamRoles": [
  "{{ IamRoles[0] }}"
 ],
 "KmsKeyId": "{{ KmsKeyId }}",
 "LogExports": [
  "{{ LogExports[0] }}"
 ],
 "ManageAdminPassword": "{{ ManageAdminPassword }}",
 "NamespaceName": "{{ NamespaceName }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "FinalSnapshotName": "{{ FinalSnapshotName }}",
 "FinalSnapshotRetentionPeriod": "{{ FinalSnapshotRetentionPeriod }}",
 "NamespaceResourcePolicy": {},
 "RedshiftIdcApplicationArn": "{{ RedshiftIdcApplicationArn }}",
 "SnapshotCopyConfigurations": [
  {
   "DestinationRegion": "{{ DestinationRegion }}",
   "DestinationKmsKeyId": "{{ DestinationKmsKeyId }}",
   "SnapshotRetentionPeriod": "{{ SnapshotRetentionPeriod }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.redshiftserverless.namespaces (
 AdminPasswordSecretKmsKeyId,
 AdminUserPassword,
 AdminUsername,
 DbName,
 DefaultIamRoleArn,
 IamRoles,
 KmsKeyId,
 LogExports,
 ManageAdminPassword,
 NamespaceName,
 Tags,
 FinalSnapshotName,
 FinalSnapshotRetentionPeriod,
 NamespaceResourcePolicy,
 RedshiftIdcApplicationArn,
 SnapshotCopyConfigurations,
 region
)
SELECT 
 {{ AdminPasswordSecretKmsKeyId }},
 {{ AdminUserPassword }},
 {{ AdminUsername }},
 {{ DbName }},
 {{ DefaultIamRoleArn }},
 {{ IamRoles }},
 {{ KmsKeyId }},
 {{ LogExports }},
 {{ ManageAdminPassword }},
 {{ NamespaceName }},
 {{ Tags }},
 {{ FinalSnapshotName }},
 {{ FinalSnapshotRetentionPeriod }},
 {{ NamespaceResourcePolicy }},
 {{ RedshiftIdcApplicationArn }},
 {{ SnapshotCopyConfigurations }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.redshiftserverless.namespaces
WHERE data__Identifier = '<NamespaceName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>namespaces</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
kms:TagResource,
kms:UntagResource,
kms:ScheduleKeyDeletion,
kms:CancelKeyDeletion,
kms:Encrypt,
kms:Decrypt,
kms:DescribeKey,
kms:GenerateDataKeyPair,
kms:GenerateDataKey,
kms:CreateGrant,
kms:ListGrants,
kms:RevokeGrant,
kms:RetireGrant,
redshift-serverless:CreateNamespace,
redshift-serverless:GetNamespace,
redshift-serverless:ListSnapshotCopyConfigurations,
redshift-serverless:CreateSnapshotCopyConfiguration,
redshift:GetResourcePolicy,
redshift:PutResourcePolicy,
secretsmanager:CreateSecret,
secretsmanager:TagResource,
secretsmanager:RotateSecret,
secretsmanager:DescribeSecret
```

### Delete
```json
iam:PassRole,
redshift-serverless:DeleteNamespace,
redshift-serverless:GetNamespace,
kms:RetireGrant,
secretsmanager:DescribeSecret,
secretsmanager:DeleteSecret,
redshift:DeleteResourcePolicy
```

### List
```json
iam:PassRole,
redshift-serverless:ListNamespaces
```

