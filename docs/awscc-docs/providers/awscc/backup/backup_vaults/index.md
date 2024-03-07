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
Retrieves a list of <code>backup_vaults</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>backup_vaults</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.backup.backup_vaults</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>backup_vault_name</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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

### List
```json
backup:ListBackupVaults
```


## Example
```sql
SELECT
region,
backup_vault_name
FROM awscc.backup.backup_vaults
WHERE region = 'us-east-1'
```
