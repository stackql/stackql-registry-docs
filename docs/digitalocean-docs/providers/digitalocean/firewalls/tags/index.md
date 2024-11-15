---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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

Creates, updates, deletes, gets or lists a <code>tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.firewalls.tags" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="firewalls_add_tags" /> | `INSERT` | <CopyableCode code="firewall_id, data__tags" /> | To assign a tag representing a group of Droplets to a firewall, send a POST request to `/v2/firewalls/$FIREWALL_ID/tags`. In the body of the request, there should be a `tags` attribute containing a list of tag names. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |
| <CopyableCode code="firewalls_delete_tags" /> | `DELETE` | <CopyableCode code="firewall_id, data__tags" /> | To remove a tag representing a group of Droplets from a firewall, send a DELETE request to `/v2/firewalls/$FIREWALL_ID/tags`. In the body of the request, there should be a `tags` attribute containing a list of tag names. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tags</code> resource.

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
INSERT INTO digitalocean.firewalls.tags (
data__tags,
firewall_id
)
SELECT 
'{{ tags }}',
'{{ firewall_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: tags
  props:
    - name: firewall_id
      value: string
    - name: data__tags
      value: string
    - name: tags
      value: array

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>tags</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.firewalls.tags
WHERE firewall_id = '{{ firewall_id }}'
AND data__tags = '{{ data__tags }}';
```
