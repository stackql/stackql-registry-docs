---
title: volumes_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes_actions
  - block_storage
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

Creates, updates, deletes, gets or lists a <code>volumes_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.block_storage.volumes_actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="volume_actions_get" /> | `SELECT` | <CopyableCode code="action_id, volume_id" /> | To retrieve the status of a volume action, send a GET request to `/v2/volumes/$VOLUME_ID/actions/$ACTION_ID`. |
| <CopyableCode code="volume_actions_list" /> | `SELECT` | <CopyableCode code="volume_id" /> | To retrieve all actions that have been executed on a volume, send a GET request to `/v2/volumes/$VOLUME_ID/actions`. |
| <CopyableCode code="volume_actions_post" /> | `EXEC` | <CopyableCode code="" /> | To initiate an action on a block storage volume by Name, send a POST request to `~/v2/volumes/actions`. The body should contain the appropriate attributes for the respective action. ## Attach a Block Storage Volume to a Droplet \| Attribute \| Details \| \| ----------- \| ------------------------------------------------------------------- \| \| type \| This must be `attach` \| \| volume_name \| The name of the block storage volume \| \| droplet_id \| Set to the Droplet's ID \| \| region \| Set to the slug representing the region where the volume is located \| Each volume may only be attached to a single Droplet. However, up to fifteen volumes may be attached to a Droplet at a time. Pre-formatted volumes will be automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018 when attached. On older Droplets, [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/) is required. ## Remove a Block Storage Volume from a Droplet \| Attribute \| Details \| \| ----------- \| ------------------------------------------------------------------- \| \| type \| This must be `detach` \| \| volume_name \| The name of the block storage volume \| \| droplet_id \| Set to the Droplet's ID \| \| region \| Set to the slug representing the region where the volume is located \| |
| <CopyableCode code="volume_actions_post_by_id" /> | `EXEC` | <CopyableCode code="volume_id" /> | To initiate an action on a block storage volume by Id, send a POST request to `~/v2/volumes/$VOLUME_ID/actions`. The body should contain the appropriate attributes for the respective action. ## Attach a Block Storage Volume to a Droplet \| Attribute \| Details \| \| ---------- \| ------------------------------------------------------------------- \| \| type \| This must be `attach` \| \| droplet_id \| Set to the Droplet's ID \| \| region \| Set to the slug representing the region where the volume is located \| Each volume may only be attached to a single Droplet. However, up to fifteen volumes may be attached to a Droplet at a time. Pre-formatted volumes will be automatically mounted to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018 when attached. On older Droplets, [additional configuration](https://docs.digitalocean.com/products/volumes/how-to/mount/) is required. ## Remove a Block Storage Volume from a Droplet \| Attribute \| Details \| \| ---------- \| ------------------------------------------------------------------- \| \| type \| This must be `detach` \| \| droplet_id \| Set to the Droplet's ID \| \| region \| Set to the slug representing the region where the volume is located \| ## Resize a Volume \| Attribute \| Details \| \| -------------- \| ------------------------------------------------------------------- \| \| type \| This must be `resize` \| \| size_gigabytes \| The new size of the block storage volume in GiB (1024^3) \| \| region \| Set to the slug representing the region where the volume is located \| Volumes may only be resized upwards. The maximum size for a volume is 16TiB. |

## `SELECT` examples

To retrieve all actions that have been executed on a volume, send a GET request to `/v2/volumes/$VOLUME_ID/actions`.


```sql
SELECT
column_anon
FROM digitalocean.block_storage.volumes_actions
WHERE volume_id = '{{ volume_id }}';
```