---
title: forwarding_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - forwarding_rules
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

Creates, updates, deletes, gets or lists a <code>forwarding_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>forwarding_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.load_balancers.forwarding_rules" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="load_balancers_add_forwarding_rules" /> | `INSERT` | <CopyableCode code="lb_id, data__forwarding_rules" /> | To add an additional forwarding rule to a load balancer instance, send a POST request to `/v2/load_balancers/$LOAD_BALANCER_ID/forwarding_rules`. In the body of the request, there should be a `forwarding_rules` attribute containing an array of rules to be added. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |
| <CopyableCode code="load_balancers_remove_forwarding_rules" /> | `DELETE` | <CopyableCode code="lb_id, data__forwarding_rules" /> | To remove forwarding rules from a load balancer instance, send a DELETE request to `/v2/load_balancers/$LOAD_BALANCER_ID/forwarding_rules`. In the body of the request, there should be a `forwarding_rules` attribute containing an array of rules to be removed. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>forwarding_rules</code> resource.

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
INSERT INTO digitalocean.load_balancers.forwarding_rules (
data__forwarding_rules,
lb_id
)
SELECT 
'{{ forwarding_rules }}',
'{{ lb_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: forwarding_rules
  props:
    - name: lb_id
      value: string
    - name: data__forwarding_rules
      value: string
    - name: forwarding_rules
      value: array
      props:
        - name: entry_protocol
          value: string
        - name: entry_port
          value: integer
        - name: target_protocol
          value: string
        - name: target_port
          value: integer
        - name: certificate_id
          value: string
        - name: tls_passthrough
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>forwarding_rules</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.load_balancers.forwarding_rules
WHERE lb_id = '{{ lb_id }}'
AND data__forwarding_rules = '{{ data__forwarding_rules }}';
```
