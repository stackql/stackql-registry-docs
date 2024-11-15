---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
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

Creates, updates, deletes, gets or lists a <code>rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.firewalls.rules" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="firewalls_add_rules" /> | `INSERT` | <CopyableCode code="firewall_id" /> | To add additional access rules to a firewall, send a POST request to `/v2/firewalls/$FIREWALL_ID/rules`. The body of the request may include an inbound_rules and/or outbound_rules attribute containing an array of rules to be added. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |
| <CopyableCode code="firewalls_delete_rules" /> | `DELETE` | <CopyableCode code="firewall_id" /> | To remove access rules from a firewall, send a DELETE request to `/v2/firewalls/$FIREWALL_ID/rules`. The body of the request may include an `inbound_rules` and/or `outbound_rules` attribute containing an array of rules to be removed. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rules</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.firewalls.rules (
firewall_id
)
SELECT 
'{{ firewall_id }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.firewalls.rules (
data__inbound_rules,
firewall_id
)
SELECT 
'{{ inbound_rules }}',
'{{ firewall_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: rules
  props:
    - name: firewall_id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>rules</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.firewalls.rules
WHERE firewall_id = '{{ firewall_id }}';
```
