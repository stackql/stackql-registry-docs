---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.instances.volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique ID of this Volume. |
| `hardware_type` | `string` | The storage type of this Volume. |
| `updated` | `string` | When this Volume was last updated. |
| `tags` | `array` | An array of Tags applied to this object.  Tags are for organizational purposes only.<br /> |
| `status` | `string` | The current status of the volume.  Can be one of:<br /><br />  * `creating` - the Volume is being created and is not yet available<br />    for use.<br />  * `active` - the Volume is online and available for use.<br />  * `resizing` - the Volume is in the process of upgrading<br />    its current capacity.<br /> |
| `created` | `string` | When this Volume was created. |
| `label` | `string` | The Volume's label is for display purposes only.<br /> |
| `linode_id` | `integer` | If a Volume is attached to a specific Linode, the ID of that Linode will be displayed here.<br /> |
| `filesystem_path` | `string` | The full filesystem path for the Volume based on the Volume's label. Path is /dev/disk/by-id/scsi-0Linode_Volume_ + Volume label.<br /> |
| `size` | `integer` | The Volume's size, in GiB.<br /> |
| `linode_label` | `string` | If a Volume is attached to a specific Linode, the label of that Linode will be displayed here.<br /> |
| `region` | `string` | The unique ID of this Region. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getLinodeVolumes` | `SELECT` | `linodeId` |
| `_getLinodeVolumes` | `EXEC` | `linodeId` |
