---
title: droplets
hide_title: false
hide_table_of_contents: false
keywords:
  - droplets
  - firewalls
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

Creates, updates, deletes, gets or lists a <code>droplets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>droplets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.firewalls.droplets" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="firewalls_delete_droplets" /> | `DELETE` | <CopyableCode code="firewall_id, data__droplet_ids" /> | To remove a Droplet from a firewall, send a DELETE request to `/v2/firewalls/$FIREWALL_ID/droplets`. In the body of the request, there should be a `droplet_ids` attribute containing a list of Droplet IDs. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |
| <CopyableCode code="firewalls_assign_droplets" /> | `EXEC` | <CopyableCode code="firewall_id, data__droplet_ids" /> | To assign a Droplet to a firewall, send a POST request to `/v2/firewalls/$FIREWALL_ID/droplets`. In the body of the request, there should be a `droplet_ids` attribute containing a list of Droplet IDs. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |

## `DELETE` example

Deletes the specified <code>droplets</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.firewalls.droplets
WHERE firewall_id = '{{ firewall_id }}'
AND data__droplet_ids = '{{ data__droplet_ids }}';
```
