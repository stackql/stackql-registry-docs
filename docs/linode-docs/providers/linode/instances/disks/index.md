---
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
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
<tr><td><b>Name</b></td><td><code>disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.instances.disks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This Disk's ID which must be provided for all operations impacting this Disk.<br /> |
| `created` | `string` | When this Disk was created. |
| `filesystem` | `string` | The Disk filesystem can be one of:<br /><br />  * raw - No filesystem, just a raw binary stream.<br />  * swap - Linux swap area.<br />  * ext3 - The ext3 journaling filesystem for Linux.<br />  * ext4 - The ext4 journaling filesystem for Linux.<br />  * initrd - initrd (uncompressed initrd, ext2, max 32 MB).<br /> |
| `label` | `string` | The Disk's label is for display purposes only.<br /> |
| `size` | `integer` | The size of the Disk in MB. |
| `status` | `string` | A brief description of this Disk's current state. This field may change without direct action from you, as a result of operations performed to the Disk or the Linode containing the Disk.<br /> |
| `updated` | `string` | When this Disk was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getLinodeDisk` | `SELECT` | `diskId, linodeId` | View Disk information for a Disk associated with this Linode.<br /> |
| `getLinodeDisks` | `SELECT` | `linodeId` | View Disk information for Disks associated with this Linode.<br /> |
| `addLinodeDisk` | `INSERT` | `linodeId, data__size` | Adds a new Disk to a Linode.<br /><br />* You can optionally create a Disk from an Image or an Empty Disk if no Image is provided with a request.<br /><br />* When creating an Empty Disk, providing a `label` is required.<br /><br />* If no `label` is provided, an `image` is required instead.<br /><br />* When creating a Disk from an Image, `root_pass` is required.<br /><br />* The default filesystem for new Disks is `ext4`. If creating a Disk from an Image, the filesystem<br />of the Image is used unless otherwise specified.<br /><br />* When deploying a StackScript on a Disk:<br />  * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for<br />    a list of available StackScripts.<br />  * Requires a compatible Image to be supplied.<br />    * See StackScript View ([GET /linode/stackscript/&#123;stackscriptId&#125;](/docs/api/stackscripts/#stackscript-view)) for compatible Images.<br />  * It is recommended to supply SSH keys for the root User using the `authorized_keys` field.<br />  * You may also supply a list of usernames via the `authorized_users` field.<br />    * These users must have an SSH Key associated with their Profiles first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.<br /> |
| `deleteDisk` | `DELETE` | `diskId, linodeId` | Deletes a Disk you have permission to `read_write`.<br /><br />**Deleting a Disk is a destructive action and cannot be undone.**<br /> |
| `_getLinodeDisk` | `EXEC` | `diskId, linodeId` | View Disk information for a Disk associated with this Linode.<br /> |
| `_getLinodeDisks` | `EXEC` | `linodeId` | View Disk information for Disks associated with this Linode.<br /> |
| `cloneLinodeDisk` | `EXEC` | `diskId, linodeId` | Copies a disk, byte-for-byte, into a new Disk belonging to the same Linode. The Linode must have enough storage space available to accept a new Disk of the same size as this one or this operation will fail.<br /> |
| `resetDiskPassword` | `EXEC` | `diskId, linodeId, data__password` | Resets the password of a Disk you have permission to `read_write`.<br /> |
| `resizeDisk` | `EXEC` | `diskId, linodeId, data__size` | Resizes a Disk you have permission to `read_write`.<br /><br />The Disk must not be in use. If the Disk is in use, the request will<br />succeed but the resize will ultimately fail. For a request to succeed,<br />the Linode must be shut down prior to resizing the Disk, or the Disk<br />must not be assigned to the Linode's active Configuration Profile.<br /><br />If you are resizing the Disk to a smaller size, it cannot be made smaller<br />than what is required by the total size of the files current on the Disk.<br /> |
| `updateDisk` | `EXEC` | `diskId, linodeId` | Updates a Disk that you have permission to `read_write`.<br /> |
