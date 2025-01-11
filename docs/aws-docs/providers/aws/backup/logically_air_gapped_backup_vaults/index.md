---
title: logically_air_gapped_backup_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - logically_air_gapped_backup_vaults
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

Creates, updates, deletes or gets a <code>logically_air_gapped_backup_vault</code> resource or lists <code>logically_air_gapped_backup_vaults</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logically_air_gapped_backup_vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Backup::LogicallyAirGappedBackupVault</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.logically_air_gapped_backup_vaults" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_vault_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="min_retention_days" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="max_retention_days" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_vault_tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="notifications" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_vault_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vault_state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vault_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-logicallyairgappedbackupvault.html"><code>AWS::Backup::LogicallyAirGappedBackupVault</code></a>.

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
    <td><CopyableCode code="BackupVaultName, MinRetentionDays, MaxRetentionDays, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>logically_air_gapped_backup_vaults</code> in a region.
```sql
SELECT
region,
access_policy,
backup_vault_name,
min_retention_days,
max_retention_days,
backup_vault_tags,
notifications,
encryption_key_arn,
backup_vault_arn,
vault_state,
vault_type
FROM aws.backup.logically_air_gapped_backup_vaults
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>logically_air_gapped_backup_vault</code>.
```sql
SELECT
region,
access_policy,
backup_vault_name,
min_retention_days,
max_retention_days,
backup_vault_tags,
notifications,
encryption_key_arn,
backup_vault_arn,
vault_state,
vault_type
FROM aws.backup.logically_air_gapped_backup_vaults
WHERE region = 'us-east-1' AND data__Identifier = '<BackupVaultName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>logically_air_gapped_backup_vault</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.backup.logically_air_gapped_backup_vaults (
 BackupVaultName,
 MinRetentionDays,
 MaxRetentionDays,
 region
)
SELECT 
'{{ BackupVaultName }}',
 '{{ MinRetentionDays }}',
 '{{ MaxRetentionDays }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.backup.logically_air_gapped_backup_vaults (
 AccessPolicy,
 BackupVaultName,
 MinRetentionDays,
 MaxRetentionDays,
 BackupVaultTags,
 Notifications,
 region
)
SELECT 
 '{{ AccessPolicy }}',
 '{{ BackupVaultName }}',
 '{{ MinRetentionDays }}',
 '{{ MaxRetentionDays }}',
 '{{ BackupVaultTags }}',
 '{{ Notifications }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: logically_air_gapped_backup_vault
    props:
      - name: AccessPolicy
        value: {}
      - name: BackupVaultName
        value: '{{ BackupVaultName }}'
      - name: MinRetentionDays
        value: '{{ MinRetentionDays }}'
      - name: MaxRetentionDays
        value: '{{ MaxRetentionDays }}'
      - name: BackupVaultTags
        value: {}
      - name: Notifications
        value:
          BackupVaultEvents:
            - '{{ BackupVaultEvents[0] }}'
          SNSTopicArn: '{{ SNSTopicArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.backup.logically_air_gapped_backup_vaults
WHERE data__Identifier = '<BackupVaultName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>logically_air_gapped_backup_vaults</code> resource, the following permissions are required:

### Create
```json
backup:TagResource,
backup:CreateLogicallyAirGappedBackupVault,
backup:PutBackupVaultAccessPolicy,
backup:PutBackupVaultNotifications,
backup-storage:Mount,
backup-storage:MountCapsule,
backup:DescribeBackupVault
```

### Read
```json
backup:DescribeBackupVault,
backup:GetBackupVaultNotifications,
backup:GetBackupVaultAccessPolicy,
backup:ListTags
```

### Update
```json
backup:DescribeBackupVault,
backup:DeleteBackupVaultAccessPolicy,
backup:DeleteBackupVaultNotifications,
backup:DeleteBackupVaultLockConfiguration,
backup:GetBackupVaultAccessPolicy,
backup:ListTags,
backup:TagResource,
backup:UntagResource,
backup:PutBackupVaultAccessPolicy,
backup:PutBackupVaultNotifications,
backup:PutBackupVaultLockConfiguration
```

### Delete
```json
backup:DeleteBackupVault
```

### List
```json
backup:ListBackupVaults
```
