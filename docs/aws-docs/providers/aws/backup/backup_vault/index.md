---
title: backup_vault
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vault
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


Gets or updates an individual <code>backup_vault</code> resource, use <code>backup_vaults</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_vault</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Backup::BackupVault</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.backup_vault" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_vault_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_vault_tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="notifications" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="lock_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_vault_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
access_policy,
backup_vault_name,
backup_vault_tags,
encryption_key_arn,
notifications,
lock_configuration,
backup_vault_arn
FROM aws.backup.backup_vault
WHERE region = 'us-east-1' AND data__Identifier = '<BackupVaultName>';
```


## Permissions

To operate on the <code>backup_vault</code> resource, the following permissions are required:

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
backup:ListTags,
backup:TagResource,
backup:UntagResource,
backup:PutBackupVaultAccessPolicy,
backup:PutBackupVaultNotifications,
backup:PutBackupVaultLockConfiguration
```

