---
title: droplets
hide_title: false
hide_table_of_contents: false
keywords:
  - droplets
  - load_balancers
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
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.load_balancers.droplets" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="load_balancers_add_droplets" /> | `INSERT` | <CopyableCode code="lb_id, data__droplet_ids" /> | To assign a Droplet to a load balancer instance, send a POST request to `/v2/load_balancers/$LOAD_BALANCER_ID/droplets`. In the body of the request, there should be a `droplet_ids` attribute containing a list of Droplet IDs. Individual Droplets can not be added to a load balancer configured with a Droplet tag. Attempting to do so will result in a "422 Unprocessable Entity" response from the API. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |
| <CopyableCode code="load_balancers_remove_droplets" /> | `DELETE` | <CopyableCode code="lb_id, data__droplet_ids" /> | To remove a Droplet from a load balancer instance, send a DELETE request to `/v2/load_balancers/$LOAD_BALANCER_ID/droplets`. In the body of the request, there should be a `droplet_ids` attribute containing a list of Droplet IDs. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>droplets</code> resource.

<Tabs
    defaultValue="all"
    values={[
        
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.load_balancers.droplets (
data__droplet_ids,
lb_id
)
SELECT 
'{{ droplet_ids }}',
'{{ lb_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: droplets
  props:
    - name: lb_id
      value: string
    - name: data__droplet_ids
      value: string
    - name: droplet_ids
      value: array

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>droplets</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.load_balancers.droplets
WHERE lb_id = '{{ lb_id }}'
AND data__droplet_ids = '{{ data__droplet_ids }}';
```
