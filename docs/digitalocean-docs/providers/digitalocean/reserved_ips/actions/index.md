---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - reserved_ips
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
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.reserved_ips.actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="reserved_ips_actions_get" /> | `SELECT` | <CopyableCode code="action_id, reserved_ip" /> | To retrieve the status of a reserved IP action, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions/$ACTION_ID`. |
| <CopyableCode code="reserved_ips_actions_list" /> | `SELECT` | <CopyableCode code="reserved_ip" /> | To retrieve all actions that have been executed on a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions`. |
| <CopyableCode code="reserved_ips_actions_post" /> | `EXEC` | <CopyableCode code="reserved_ip" /> | To initiate an action on a reserved IP send a POST request to `/v2/reserved_ips/$RESERVED_IP/actions`. In the JSON body to the request, set the `type` attribute to on of the supported action types: \| Action \| Details \|------------\|-------- \| `assign` \| Assigns a reserved IP to a Droplet \| `unassign` \| Unassign a reserved IP from a Droplet |

## `SELECT` examples

To retrieve all actions that have been executed on a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions`.


```sql
SELECT
column_anon
FROM digitalocean.reserved_ips.actions
WHERE reserved_ip = '{{ reserved_ip }}';
```