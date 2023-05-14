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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.instances.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `snapshot` | `object` |
| `automatic` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getBackup` | `SELECT` | `backupId, linodeId` | Returns information about a Backup.<br /> |
| `getBackups` | `SELECT` | `linodeId` | Returns information about this Linode's available backups.<br /> |
| `createSnapshot` | `INSERT` | `linodeId, data__label` | Creates a snapshot Backup of a Linode.<br /><br />**Important:** If you already have a snapshot of this Linode, this is a destructive<br />action. The previous snapshot will be deleted.<br /> |
| `_getBackup` | `EXEC` | `backupId, linodeId` | Returns information about a Backup.<br /> |
| `_getBackups` | `EXEC` | `linodeId` | Returns information about this Linode's available backups.<br /> |
| `cancelBackups` | `EXEC` | `linodeId` | Cancels the Backup service on the given Linode. Deletes all of this Linode's existing backups forever.<br /> |
| `enableBackups` | `EXEC` | `linodeId` | Enables backups for the specified Linode.<br /> |
| `restoreBackup` | `EXEC` | `backupId, linodeId, data__linode_id` | Restores a Linode's Backup to the specified Linode.<br /> |
