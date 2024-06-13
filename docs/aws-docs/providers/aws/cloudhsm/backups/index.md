---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - cloudhsm
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

Contains information about a backup of an AWS CloudHSM cluster. All backup objects contain the <code>BackupId</code>, <code>BackupState</code>, <code>ClusterId</code>, and <code>CreateTimestamp</code> parameters. Backups that were copied into a destination region additionally contain the <code>CopyTimestamp</code>, <code>SourceBackup</code>, <code>SourceCluster</code>, and <code>SourceRegion</code> parameters. A backup that is pending deletion will include the <code>DeleteTimestamp</code> parameter.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains information about a backup of an AWS CloudHSM cluster. All backup objects contain the <code>BackupId</code>, <code>BackupState</code>, <code>ClusterId</code>, and <code>CreateTimestamp</code> parameters. Backups that were copied into a destination region additionally contain the <code>CopyTimestamp</code>, <code>SourceBackup</code>, <code>SourceCluster</code>, and <code>SourceRegion</code> parameters. A backup that is pending deletion will include the <code>DeleteTimestamp</code> parameter.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudhsm.backups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="backup_id" /></td><td><code>string</code></td><td>The identifier (ID) of the backup.</td></tr>
<tr><td><CopyableCode code="backup_state" /></td><td><code>string</code></td><td>The state of the backup.</td></tr>
<tr><td><CopyableCode code="cluster_id" /></td><td><code>string</code></td><td>The identifier (ID) of the cluster that was backed up.</td></tr>
<tr><td><CopyableCode code="create_timestamp" /></td><td><code>string</code></td><td>The date and time when the backup was created.</td></tr>
<tr><td><CopyableCode code="copy_timestamp" /></td><td><code>string</code></td><td>The date and time when the backup was copied from a source backup.</td></tr>
<tr><td><CopyableCode code="never_expires" /></td><td><code>boolean</code></td><td>Specifies whether the service should exempt a backup from the retention policy for the cluster. <code>True</code> exempts a backup from the retention policy. <code>False</code> means the service applies the backup retention policy defined at the cluster.</td></tr>
<tr><td><CopyableCode code="source_region" /></td><td><code>string</code></td><td>The AWS Region that contains the source backup from which the new backup was copied.</td></tr>
<tr><td><CopyableCode code="source_backup" /></td><td><code>string</code></td><td>The identifier (ID) of the source backup from which the new backup was copied.</td></tr>
<tr><td><CopyableCode code="source_cluster" /></td><td><code>string</code></td><td>The identifier (ID) of the cluster containing the source backup from which the new backup was copied.</td></tr>
<tr><td><CopyableCode code="delete_timestamp" /></td><td><code>string</code></td><td>The date and time when the backup will be permanently deleted.</td></tr>
<tr><td><CopyableCode code="tag_list" /></td><td><code>array</code></td><td>The list of tags for the backup.</td></tr>
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
    <td><CopyableCode code="describe_backups" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_backup" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="X-Amz-Target, data__BackupId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="copy_backup_to_region" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="X-Amz-Target, data__BackupId, data__DestinationRegion, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="modify_backup_attributes" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="X-Amz-Target, data__BackupId, data__NeverExpires, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="restore_backup" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="X-Amz-Target, data__BackupId, region" /></td>
  </tr>
</tbody></table>








