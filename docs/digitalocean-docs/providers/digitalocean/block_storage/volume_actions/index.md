---
title: volume_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_actions
  - block_storage
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.block_storage.volume_actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique numeric ID that can be used to identify and reference an action. |
| `completed_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was completed. |
| `action_resource_id` | `integer` | A unique identifier for the resource that the action is associated with. |
| `region_slug` | `string` | A human-readable string that is used as a unique identifier for each region. |
| `action_type` | `string` | This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action. |
| `region` | `object` |  |
| `started_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was initiated. |
| `resource_type` | `string` | The type of resource that the action is associated with. |
| `status` | `string` | The current status of the action. This can be "in-progress", "completed", or "errored". |
| `type` | `string` | This is the type of action that the object represents. For example, this could be "attach_volume" to represent the state of a volume attach action. |
| `resource_id` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `volumeActions_get` | `SELECT` | `action_id, volume_id` | To retrieve the status of a volume action, send a GET request to `/v2/volumes/$VOLUME_ID/actions/$ACTION_ID`.<br /><br /> |
| `volumeActions_list` | `SELECT` | `volume_id` | To retrieve all actions that have been executed on a volume, send a GET request to `/v2/volumes/$VOLUME_ID/actions`.<br /><br /> |
| `volumeActions_post` | `INSERT` |  | To initiate an action on a block storage volume by Name, send a POST request to<br />`~/v2/volumes/actions`. The body should contain the appropriate<br />attributes for the respective action.<br /><br />## Attach a Block Storage Volume to a Droplet<br /><br />\| Attribute   \| Details                                                             \|<br />\| ----------- \| ------------------------------------------------------------------- \|<br />\| type        \| This must be `attach`                                               \|<br />\| volume_name \| The name of the block storage volume                                \|<br />\| droplet_id  \| Set to the Droplet's ID                                             \|<br />\| region      \| Set to the slug representing the region where the volume is located \|<br /><br />Each volume may only be attached to a single Droplet. However, up to five<br />volumes may be attached to a Droplet at a time. Pre-formatted volumes will be<br />automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS<br />Droplets created on or after April 26, 2018 when attached. On older Droplets,<br />[additional configuration](https://www.digitalocean.com/community/tutorials/how-to-partition-and-format-digitalocean-block-storage-volumes-in-linux#mounting-the-filesystems)<br />is required.<br /><br />## Remove a Block Storage Volume from a Droplet<br /><br />\| Attribute   \| Details                                                             \|<br />\| ----------- \| ------------------------------------------------------------------- \|<br />\| type        \| This must be `detach`                                               \|<br />\| volume_name \| The name of the block storage volume                                \|<br />\| droplet_id  \| Set to the Droplet's ID                                             \|<br />\| region      \| Set to the slug representing the region where the volume is located \|<br /> |
| `_volumeActions_get` | `EXEC` | `action_id, volume_id` | To retrieve the status of a volume action, send a GET request to `/v2/volumes/$VOLUME_ID/actions/$ACTION_ID`.<br /><br /> |
| `_volumeActions_list` | `EXEC` | `volume_id` | To retrieve all actions that have been executed on a volume, send a GET request to `/v2/volumes/$VOLUME_ID/actions`.<br /><br /> |
| `volumeActions_post_byId` | `EXEC` | `volume_id` | To initiate an action on a block storage volume by Id, send a POST request to<br />`~/v2/volumes/$VOLUME_ID/actions`. The body should contain the appropriate<br />attributes for the respective action.<br /><br />## Attach a Block Storage Volume to a Droplet<br /><br />\| Attribute  \| Details                                                             \|<br />\| ---------- \| ------------------------------------------------------------------- \|<br />\| type       \| This must be `attach`                                               \|<br />\| droplet_id \| Set to the Droplet's ID                                             \|<br />\| region     \| Set to the slug representing the region where the volume is located \|<br /><br />Each volume may only be attached to a single Droplet. However, up to seven<br />volumes may be attached to a Droplet at a time. Pre-formatted volumes will be<br />automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS<br />Droplets created on or after April 26, 2018 when attached. On older Droplets,<br />[additional configuration](https://www.digitalocean.com/community/tutorials/how-to-partition-and-format-digitalocean-block-storage-volumes-in-linux#mounting-the-filesystems)<br />is required.<br /><br />## Remove a Block Storage Volume from a Droplet<br /><br />\| Attribute  \| Details                                                             \|<br />\| ---------- \| ------------------------------------------------------------------- \|<br />\| type       \| This must be `detach`                                               \|<br />\| droplet_id \| Set to the Droplet's ID                                             \|<br />\| region     \| Set to the slug representing the region where the volume is located \|<br /><br />## Resize a Volume<br /><br />\| Attribute      \| Details                                                             \|<br />\| -------------- \| ------------------------------------------------------------------- \|<br />\| type           \| This must be `resize`                                               \|<br />\| size_gigabytes \| The new size of the block storage volume in GiB (1024^3)            \|<br />\| region         \| Set to the slug representing the region where the volume is located \|<br /><br />Volumes may only be resized upwards. The maximum size for a volume is 16TiB.<br /> |
