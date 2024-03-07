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
Gets an individual <code>backup_vault</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_vault</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>backup_vault</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.backup.backup_vault</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>backup_vault_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>backup_vault_tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>encryption_key_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>notifications</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>lock_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>backup_vault_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>backup_vault</code> resource, the following permissions are required:

### Read
<pre>
backup:DescribeBackupVault,
backup:GetBackupVaultNotifications,
backup:GetBackupVaultAccessPolicy,
backup:ListTags</pre>

### Update
<pre>
backup:DescribeBackupVault,
backup:DeleteBackupVaultAccessPolicy,
backup:DeleteBackupVaultNotifications,
backup:DeleteBackupVaultLockConfiguration,
backup:ListTags,
backup:TagResource,
backup:UntagResource,
backup:PutBackupVaultAccessPolicy,
backup:PutBackupVaultNotifications,
backup:PutBackupVaultLockConfiguration</pre>

### Delete
<pre>
backup:DeleteBackupVault</pre>


## Example
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
FROM awscc.backup.backup_vault
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;BackupVaultName&gt;'
```
