---
title: backup_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults
  - backup
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


Used to retrieve a list of <code>backup_vaults</code> in a region or to create or delete a <code>backup_vaults</code> resource, use <code>backup_vault</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Backup::BackupVault</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.backup_vaults" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="backup_vault_name" /></td><td><code>undefined</code></td><td></td></tr>
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
backup_vault_name
FROM aws.backup.backup_vaults
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
 "BackupVaultName": "{{ BackupVaultName }}"
}
>>>
--required properties only
INSERT INTO aws.backup.backup_vaults (
 BackupVaultName,
 region
)
SELECT 
{{ .BackupVaultName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AccessPolicy": {},
 "BackupVaultName": "{{ BackupVaultName }}",
 "BackupVaultTags": {},
 "EncryptionKeyArn": "{{ EncryptionKeyArn }}",
 "Notifications": {
  "BackupVaultEvents": [
   "{{ BackupVaultEvents[0] }}"
  ],
  "SNSTopicArn": "{{ SNSTopicArn }}"
 },
 "LockConfiguration": {
  "MinRetentionDays": "{{ MinRetentionDays }}",
  "MaxRetentionDays": "{{ MaxRetentionDays }}",
  "ChangeableForDays": "{{ ChangeableForDays }}"
 }
}
>>>
--all properties
INSERT INTO aws.backup.backup_vaults (
 AccessPolicy,
 BackupVaultName,
 BackupVaultTags,
 EncryptionKeyArn,
 Notifications,
 LockConfiguration,
 region
)
SELECT 
 {{ .AccessPolicy }},
 {{ .BackupVaultName }},
 {{ .BackupVaultTags }},
 {{ .EncryptionKeyArn }},
 {{ .Notifications }},
 {{ .LockConfiguration }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.backup.backup_vaults
WHERE data__Identifier = '<BackupVaultName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>backup_vaults</code> resource, the following permissions are required:

### Create
```json
backup:TagResource,
backup:CreateBackupVault,
backup:PutBackupVaultAccessPolicy,
backup:PutBackupVaultNotifications,
backup:PutBackupVaultLockConfiguration,
backup-storage:Mount,
backup-storage:MountCapsule,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt,
kms:RetireGrant,
kms:DescribeKey
```

### Delete
```json
backup:DeleteBackupVault
```

### List
```json
backup:ListBackupVaults
```

