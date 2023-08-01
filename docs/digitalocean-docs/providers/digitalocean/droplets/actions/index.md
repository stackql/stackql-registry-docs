---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - droplets
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.droplets.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique numeric ID that can be used to identify and reference an action. |
| `resource_id` | `integer` | A unique identifier for the resource that the action is associated with. |
| `status` | `string` | The current status of the action. This can be "in-progress", "completed", or "errored". |
| `type` | `string` | This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action. |
| `resource_type` | `string` | The type of resource that the action is associated with. |
| `region_slug` | `string` | A human-readable string that is used as a unique identifier for each region. |
| `completed_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was completed. |
| `region` | `object` |  |
| `started_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was initiated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `dropletActions_get` | `SELECT` | `action_id, droplet_id` | To retrieve a Droplet action, send a GET request to<br />`/v2/droplets/$DROPLET_ID/actions/$ACTION_ID`.<br /><br />The response will be a JSON object with a key called `action`. The value will<br />be a Droplet action object.<br /> |
| `dropletActions_list` | `SELECT` | `droplet_id` | To retrieve a list of all actions that have been executed for a Droplet, send<br />a GET request to `/v2/droplets/$DROPLET_ID/actions`.<br /><br />The results will be returned as a JSON object with an `actions` key. This will<br />be set to an array filled with `action` objects containing the standard<br />`action` attributes.<br /> |
| `dropletActions_post` | `INSERT` | `droplet_id` | To initiate an action on a Droplet send a POST request to<br />`/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request,<br />set the `type` attribute to on of the supported action types:<br /><br />\| Action                                   \| Details \|<br />\| ---------------------------------------- \| ----------- \|<br />\| &lt;nobr&gt;`enable_backups`&lt;/nobr&gt;            \| Enables backups for a Droplet \|<br />\| &lt;nobr&gt;`disable_backups`&lt;/nobr&gt;           \| Disables backups for a Droplet \|<br />\| &lt;nobr&gt;`reboot`&lt;/nobr&gt;                    \| Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console. \|<br />\| &lt;nobr&gt;`power_cycle`&lt;/nobr&gt;               \| Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch. \|<br />\| &lt;nobr&gt;`shutdown`&lt;/nobr&gt;                  \| Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. \|<br />\| &lt;nobr&gt;`power_off`&lt;/nobr&gt;                 \| Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications. \|<br />\| &lt;nobr&gt;`power_on`&lt;/nobr&gt;                  \| Powers on a Droplet. \|<br />\| &lt;nobr&gt;`restore`&lt;/nobr&gt;                   \| Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact. \|<br />\| &lt;nobr&gt;`password_reset`&lt;/nobr&gt;            \| Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use. \|<br />\| &lt;nobr&gt;`resize`&lt;/nobr&gt;                    \| Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`. \|<br />\| &lt;nobr&gt;`rebuild`&lt;/nobr&gt;                   \| Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug. \|<br />\| &lt;nobr&gt;`rename`&lt;/nobr&gt;                    \| Renames a Droplet. \|<br />\| &lt;nobr&gt;`change_kernel`&lt;/nobr&gt;             \| Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default. \|<br />\| &lt;nobr&gt;`enable_ipv6`&lt;/nobr&gt;               \| Enables IPv6 for a Droplet. \|<br />\| &lt;nobr&gt;`snapshot`&lt;/nobr&gt;                  \| Takes a snapshot of a Droplet. \|<br /> |
| `_dropletActions_get` | `EXEC` | `action_id, droplet_id` | To retrieve a Droplet action, send a GET request to<br />`/v2/droplets/$DROPLET_ID/actions/$ACTION_ID`.<br /><br />The response will be a JSON object with a key called `action`. The value will<br />be a Droplet action object.<br /> |
| `_dropletActions_list` | `EXEC` | `droplet_id` | To retrieve a list of all actions that have been executed for a Droplet, send<br />a GET request to `/v2/droplets/$DROPLET_ID/actions`.<br /><br />The results will be returned as a JSON object with an `actions` key. This will<br />be set to an array filled with `action` objects containing the standard<br />`action` attributes.<br /> |
| `dropletActions_post_byTag` | `EXEC` |  | Some actions can be performed in bulk on tagged Droplets. The actions can be<br />initiated by sending a POST to `/v2/droplets/actions?tag_name=$TAG_NAME` with<br />the action arguments.<br /><br />Only a sub-set of action types are supported:<br /><br />- `power_cycle`<br />- `power_on`<br />- `power_off`<br />- `shutdown`<br />- `enable_ipv6`<br />- `enable_backups`<br />- `disable_backups`<br />- `snapshot`<br /> |
