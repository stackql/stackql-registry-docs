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
<tr><td><b>Id</b></td><td><code>aws.backup.backup_vault</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AccessPolicy</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BackupVaultName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>BackupVaultTags</code></td><td><code>object</code></td><td></td></tr><tr><td><code>EncryptionKeyArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Notifications</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>LockConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>BackupVaultArn</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.backup.backup_vault
WHERE region = 'us-east-1' AND data__Identifier = '{BackupVaultName}'
```
