---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - volumes
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.volumes.volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique ID of this Volume. |
| `hardware_type` | `string` | The storage type of this Volume. |
| `linode_label` | `string` | If a Volume is attached to a specific Linode, the label of that Linode will be displayed here.<br /> |
| `tags` | `array` | An array of Tags applied to this object.  Tags are for organizational purposes only.<br /> |
| `created` | `string` | When this Volume was created. |
| `label` | `string` | The Volume's label is for display purposes only.<br /> |
| `size` | `integer` | The Volume's size, in GiB.<br /> |
| `region` | `string` | The unique ID of this Region. |
| `updated` | `string` | When this Volume was last updated. |
| `status` | `string` | The current status of the volume.  Can be one of:<br /><br />  * `creating` - the Volume is being created and is not yet available<br />    for use.<br />  * `active` - the Volume is online and available for use.<br />  * `resizing` - the Volume is in the process of upgrading<br />    its current capacity.<br /> |
| `linode_id` | `integer` | If a Volume is attached to a specific Linode, the ID of that Linode will be displayed here.<br /> |
| `filesystem_path` | `string` | The full filesystem path for the Volume based on the Volume's label. Path is /dev/disk/by-id/scsi-0Linode_Volume_ + Volume label.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getVolume` | `SELECT` | `volumeId` | Get information about a single Volume.<br /> |
| `getVolumes` | `SELECT` |  | Returns a paginated list of Volumes you have permission to view.<br /> |
| `createVolume` | `INSERT` | `data__label` | Creates a Volume on your Account. In order for this to complete successfully, your User must have the `add_volumes` grant. Creating a new Volume will start accruing additional charges on your account.<br /> |
| `deleteVolume` | `DELETE` | `volumeId` | Deletes a Volume you have permission to `read_write`.<br /><br />* **Deleting a Volume is a destructive action and cannot be undone.**<br /><br />* Deleting stops billing for the Volume. You will be billed for time used within<br />the billing period the Volume was active.<br /><br />* Volumes that are migrating cannot be deleted until the migration is finished.<br /> |
| `_getVolume` | `EXEC` | `volumeId` | Get information about a single Volume.<br /> |
| `_getVolumes` | `EXEC` |  | Returns a paginated list of Volumes you have permission to view.<br /> |
| `attachVolume` | `EXEC` | `volumeId, data__linode_id` | Attaches a Volume on your Account to an existing Linode on your Account. In order for this request to complete successfully, your User must have `read_only` or `read_write` permission to the Volume and `read_write` permission to the Linode. Additionally, the Volume and Linode must be located in the same Region.<br /> |
| `cloneVolume` | `EXEC` | `volumeId, data__label` | Creates a Volume on your Account. In order for this request to complete successfully, your User must have the `add_volumes` grant. The new Volume will have the same size and data as the source Volume. Creating a new Volume will incur a charge on your Account.<br />* Only Volumes with a `status` of "active" can be cloned.<br /> |
| `detachVolume` | `EXEC` | `volumeId` | Detaches a Volume on your Account from a Linode on your Account. In order for this request to complete successfully, your User must have `read_write` access to the Volume and `read_write` access to the Linode.<br /> |
| `resizeVolume` | `EXEC` | `volumeId, data__size` | Resize an existing Volume on your Account. In order for this request to complete successfully, your User must have the `read_write` permissions to the Volume.<br />* Volumes can only be resized up.<br />* Only Volumes with a `status` of "active" can be resized.<br /> |
| `updateVolume` | `EXEC` | `volumeId` | Updates a Volume that you have permission to `read_write`.<br /> |
