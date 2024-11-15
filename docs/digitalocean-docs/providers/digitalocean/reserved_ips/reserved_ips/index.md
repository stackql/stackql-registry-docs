---
title: reserved_ips
hide_title: false
hide_table_of_contents: false
keywords:
  - reserved_ips
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

Creates, updates, deletes, gets or lists a <code>reserved_ips</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reserved_ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.reserved_ips.reserved_ips" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="droplet" /> | `` | The Droplet that the reserved IP has been assigned to. When you query a reserved IP, if it is assigned to a Droplet, the entire Droplet object will be returned. If it is not assigned, the value will be null. |
| <CopyableCode code="ip" /> | `string` | The public IP address of the reserved IP. It also serves as its identifier. |
| <CopyableCode code="locked" /> | `boolean` | A boolean value indicating whether or not the reserved IP has pending actions preventing new ones from being submitted. |
| <CopyableCode code="project_id" /> | `string` | The UUID of the project to which the reserved IP currently belongs. |
| <CopyableCode code="region" /> | `object` | The region that the reserved IP is reserved to. When you query a reserved IP, the entire region object will be returned. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="reserved_ips_get" /> | `SELECT` | <CopyableCode code="reserved_ip" /> | To show information about a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP_ADDR`. |
| <CopyableCode code="reserved_ips_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of the reserved IPs available on your account, send a GET request to `/v2/reserved_ips`. |
| <CopyableCode code="reserved_ips_create" /> | `INSERT` | <CopyableCode code="" /> | On creation, a reserved IP must be either assigned to a Droplet or reserved to a region. * To create a new reserved IP assigned to a Droplet, send a POST request to `/v2/reserved_ips` with the `droplet_id` attribute. * To create a new reserved IP reserved to a region, send a POST request to `/v2/reserved_ips` with the `region` attribute. **Note**: In addition to the standard rate limiting, only 12 reserved IPs may be created per 60 seconds. |
| <CopyableCode code="reserved_ips_delete" /> | `DELETE` | <CopyableCode code="reserved_ip" /> | To delete a reserved IP and remove it from your account, send a DELETE request to `/v2/reserved_ips/$RESERVED_IP_ADDR`. A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. |

## `SELECT` examples

To list all of the reserved IPs available on your account, send a GET request to `/v2/reserved_ips`.


```sql
SELECT
droplet,
ip,
locked,
project_id,
region
FROM digitalocean.reserved_ips.reserved_ips
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>reserved_ips</code> resource.

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
INSERT INTO digitalocean.reserved_ips.reserved_ips (
data__droplet_id
)
SELECT 
'{{ droplet_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: reserved_ips
  props:
    - name: droplet_id
      value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>reserved_ips</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.reserved_ips.reserved_ips
WHERE reserved_ip = '{{ reserved_ip }}';
```
