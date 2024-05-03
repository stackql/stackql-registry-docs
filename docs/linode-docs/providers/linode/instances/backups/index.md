---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - instances
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.instances.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="automatic" /> | `array` |
| <CopyableCode code="snapshot" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getBackup" /> | `SELECT` | <CopyableCode code="backupId, linodeId" /> | Returns information about a Backup.<br /> |
| <CopyableCode code="getBackups" /> | `SELECT` | <CopyableCode code="linodeId" /> | Returns information about this Linode's available backups.<br /> |
| <CopyableCode code="createSnapshot" /> | `INSERT` | <CopyableCode code="linodeId, data__label" /> | Creates a snapshot Backup of a Linode.<br /><br />**Important:** If you already have a snapshot of this Linode, this is a destructive<br />action. The previous snapshot will be deleted.<br /> |
| <CopyableCode code="_getBackup" /> | `EXEC` | <CopyableCode code="backupId, linodeId" /> | Returns information about a Backup.<br /> |
| <CopyableCode code="_getBackups" /> | `EXEC` | <CopyableCode code="linodeId" /> | Returns information about this Linode's available backups.<br /> |
| <CopyableCode code="cancelBackups" /> | `EXEC` | <CopyableCode code="linodeId" /> | Cancels the Backup service on the given Linode. Deletes all of this Linode's existing backups forever.<br /> |
| <CopyableCode code="enableBackups" /> | `EXEC` | <CopyableCode code="linodeId" /> | Enables backups for the specified Linode.<br /> |
| <CopyableCode code="restoreBackup" /> | `EXEC` | <CopyableCode code="backupId, linodeId, data__linode_id" /> | Restores a Linode's Backup to the specified Linode.<br /> |
