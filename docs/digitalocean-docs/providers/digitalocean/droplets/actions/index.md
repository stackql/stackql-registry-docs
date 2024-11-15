---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - droplets
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="droplet_actions_get" /> | `SELECT` | <CopyableCode code="action_id, droplet_id" /> | To retrieve a Droplet action, send a GET request to `/v2/droplets/$DROPLET_ID/actions/$ACTION_ID`. The response will be a JSON object with a key called `action`. The value will be a Droplet action object. |
| <CopyableCode code="droplet_actions_list" /> | `SELECT` | <CopyableCode code="droplet_id" /> | To retrieve a list of all actions that have been executed for a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/actions`. The results will be returned as a JSON object with an `actions` key. This will be set to an array filled with `action` objects containing the standard `action` attributes. |
| <CopyableCode code="droplet_actions_post" /> | `EXEC` | <CopyableCode code="droplet_id" /> | To initiate an action on a Droplet send a POST request to `/v2/droplets/$DROPLET_ID/actions`. In the JSON body to the request, set the `type` attribute to on of the supported action types: \| Action \| Details \| \| ---------------------------------------- \| ----------- \| \| `enable_backups` \| Enables backups for a Droplet \| \| `disable_backups` \| Disables backups for a Droplet \| \| `change_backup_policy` \| Update the backup policy for a Droplet \| \| `reboot` \| Reboots a Droplet. A `reboot` action is an attempt to reboot the Droplet in a graceful way, similar to using the `reboot` command from the console. \| \| `power_cycle` \| Power cycles a Droplet. A `powercycle` action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch. \| \| `shutdown` \| Shutsdown a Droplet. A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the `shutdown` command from the console. Since a `shutdown` command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a `power_off` action to ensure the Droplet is off. \| \| `power_off` \| Powers off a Droplet. A `power_off` event is a hard shutdown and should only be used if the `shutdown` action is not successful. It is similar to cutting the power on a server and could lead to complications. \| \| `power_on` \| Powers on a Droplet. \| \| `restore` \| Restore a Droplet using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact. \| \| `password_reset` \| Resets the root password for a Droplet. A new password will be provided via email. It must be changed after first use. \| \| `resize` \| Resizes a Droplet. Set the `size` attribute to a size slug. If a permanent resize with disk changes included is desired, set the `disk` attribute to `true`. \| \| `rebuild` \| Rebuilds a Droplet from a new base image. Set the `image` attribute to an image ID or slug. \| \| `rename` \| Renames a Droplet. \| \| `change_kernel` \| Changes a Droplet's kernel. Only applies to Droplets with externally managed kernels. All Droplets created after March 2017 use internal kernels by default. \| \| `enable_ipv6` \| Enables IPv6 for a Droplet. Once enabled for a Droplet, IPv6 can not be disabled. When enabling IPv6 on an existing Droplet, [additional OS-level configuration](https://docs.digitalocean.com/products/networking/ipv6/how-to/enable/#on-existing-droplets) is required. \| \| `snapshot` \| Takes a snapshot of a Droplet. \| |
| <CopyableCode code="droplet_actions_post_by_tag" /> | `EXEC` | <CopyableCode code="" /> | Some actions can be performed in bulk on tagged Droplets. The actions can be initiated by sending a POST to `/v2/droplets/actions?tag_name=$TAG_NAME` with the action arguments. Only a sub-set of action types are supported: - `power_cycle` - `power_on` - `power_off` - `shutdown` - `enable_ipv6` - `enable_backups` - `disable_backups` - `snapshot` |

## `SELECT` examples

To retrieve a list of all actions that have been executed for a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/actions`. The results will be returned as a JSON object with an `actions` key. This will be set to an array filled with `action` objects containing the standard `action` attributes.


```sql
SELECT
column_anon
FROM digitalocean.droplets.actions
WHERE droplet_id = '{{ droplet_id }}';
```