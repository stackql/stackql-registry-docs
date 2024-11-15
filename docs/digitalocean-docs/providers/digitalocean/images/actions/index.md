---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - images
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
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.images.actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | A unique numeric ID that can be used to identify and reference an action. |
| <CopyableCode code="completed_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the action was completed. |
| <CopyableCode code="region" /> | `object` |  |
| <CopyableCode code="region_slug" /> | `string` | A human-readable string that is used as a unique identifier for each region. |
| <CopyableCode code="resource_id" /> | `integer` | A unique identifier for the resource that the action is associated with. |
| <CopyableCode code="resource_type" /> | `string` | The type of resource that the action is associated with. |
| <CopyableCode code="started_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the action was initiated. |
| <CopyableCode code="status" /> | `string` | The current status of the action. This can be "in-progress", "completed", or "errored". |
| <CopyableCode code="type" /> | `string` | This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="image_actions_get" /> | `SELECT` | <CopyableCode code="action_id, image_id" /> | To retrieve the status of an image action, send a GET request to `/v2/images/$IMAGE_ID/actions/$IMAGE_ACTION_ID`. |
| <CopyableCode code="image_actions_list" /> | `SELECT` | <CopyableCode code="image_id" /> | To retrieve all actions that have been executed on an image, send a GET request to `/v2/images/$IMAGE_ID/actions`. |
| <CopyableCode code="image_actions_post" /> | `EXEC` | <CopyableCode code="image_id" /> | The following actions are available on an Image. ## Convert an Image to a Snapshot To convert an image, for example, a backup to a snapshot, send a POST request to `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `convert`. ## Transfer an Image To transfer an image to another region, send a POST request to `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `transfer` and set `region` attribute to the slug identifier of the region you wish to transfer to. |

## `SELECT` examples

To retrieve all actions that have been executed on an image, send a GET request to `/v2/images/$IMAGE_ID/actions`.


```sql
SELECT
id,
completed_at,
region,
region_slug,
resource_id,
resource_type,
started_at,
status,
type
FROM digitalocean.images.actions
WHERE image_id = '{{ image_id }}';
```