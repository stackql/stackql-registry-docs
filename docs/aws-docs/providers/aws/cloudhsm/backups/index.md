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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudhsm.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="BackupId" /> | `string` | The identifier (ID) of the backup. |
| <CopyableCode code="BackupState" /> | `string` | The state of the backup. |
| <CopyableCode code="ClusterId" /> | `string` | The identifier (ID) of the cluster that was backed up. |
| <CopyableCode code="CopyTimestamp" /> | `string` | The date and time when the backup was copied from a source backup. |
| <CopyableCode code="CreateTimestamp" /> | `string` | The date and time when the backup was created. |
| <CopyableCode code="DeleteTimestamp" /> | `string` | The date and time when the backup will be permanently deleted. |
| <CopyableCode code="NeverExpires" /> | `boolean` | Specifies whether the service should exempt a backup from the retention policy for the cluster. &lt;code&gt;True&lt;/code&gt; exempts a backup from the retention policy. &lt;code&gt;False&lt;/code&gt; means the service applies the backup retention policy defined at the cluster. |
| <CopyableCode code="SourceBackup" /> | `string` | The identifier (ID) of the source backup from which the new backup was copied. |
| <CopyableCode code="SourceCluster" /> | `string` | The identifier (ID) of the cluster containing the source backup from which the new backup was copied. |
| <CopyableCode code="SourceRegion" /> | `string` | The AWS Region that contains the source backup from which the new backup was copied. |
| <CopyableCode code="TagList" /> | `array` | The list of tags for the backup. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="describe_backups" /> | `SELECT` | <CopyableCode code="region" /> | &lt;p&gt;Gets information about backups of AWS CloudHSM clusters.&lt;/p&gt; &lt;p&gt;This is a paginated operation, which means that each response might contain only a subset of all the backups. When the response contains only a subset of backups, it includes a &lt;code&gt;NextToken&lt;/code&gt; value. Use this value in a subsequent &lt;code&gt;DescribeBackups&lt;/code&gt; request to get more backups. When you receive a response with no &lt;code&gt;NextToken&lt;/code&gt; (or an empty or null value), that means there are no more backups to get.&lt;/p&gt; |
| <CopyableCode code="delete_backup" /> | `DELETE` | <CopyableCode code="X-Amz-Target, data__BackupId, region" /> | Deletes a specified AWS CloudHSM backup. A backup can be restored up to 7 days after the DeleteBackup request is made. For more information on restoring a backup, see &lt;a&gt;RestoreBackup&lt;/a&gt;. |
| <CopyableCode code="copy_backup_to_region" /> | `EXEC` | <CopyableCode code="X-Amz-Target, data__BackupId, data__DestinationRegion, region" /> | Copy an AWS CloudHSM cluster backup to a different region. |
| <CopyableCode code="modify_backup_attributes" /> | `EXEC` | <CopyableCode code="X-Amz-Target, data__BackupId, data__NeverExpires, region" /> | Modifies attributes for AWS CloudHSM backup. |
| <CopyableCode code="restore_backup" /> | `EXEC` | <CopyableCode code="X-Amz-Target, data__BackupId, region" /> | Restores a specified AWS CloudHSM backup that is in the &lt;code&gt;PENDING_DELETION&lt;/code&gt; state. For mor information on deleting a backup, see &lt;a&gt;DeleteBackup&lt;/a&gt;. |
