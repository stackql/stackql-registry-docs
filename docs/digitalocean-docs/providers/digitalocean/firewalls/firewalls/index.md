---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
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

Creates, updates, deletes, gets or lists a <code>firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.firewalls.firewalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="firewalls_get" /> | `SELECT` | <CopyableCode code="firewall_id" /> | To show information about an existing firewall, send a GET request to `/v2/firewalls/$FIREWALL_ID`. |
| <CopyableCode code="firewalls_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of the firewalls available on your account, send a GET request to `/v2/firewalls`. |
| <CopyableCode code="firewalls_create" /> | `INSERT` | <CopyableCode code="" /> | To create a new firewall, send a POST request to `/v2/firewalls`. The request must contain at least one inbound or outbound access rule. |
| <CopyableCode code="firewalls_delete" /> | `DELETE` | <CopyableCode code="firewall_id" /> | To delete a firewall send a DELETE request to `/v2/firewalls/$FIREWALL_ID`. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |
| <CopyableCode code="firewalls_update" /> | `EXEC` | <CopyableCode code="firewall_id" /> | To update the configuration of an existing firewall, send a PUT request to `/v2/firewalls/$FIREWALL_ID`. The request should contain a full representation of the firewall including existing attributes. **Note that any attributes that are not provided will be reset to their default values.** |

## `SELECT` examples

To list all of the firewalls available on your account, send a GET request to `/v2/firewalls`.


```sql
SELECT
column_anon
FROM digitalocean.firewalls.firewalls
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewalls</code> resource.

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
INSERT INTO digitalocean.firewalls.firewalls (

)
SELECT 

;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.firewalls.firewalls (
data__inbound_rules
)
SELECT 
'{{ inbound_rules }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: firewalls
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>firewalls</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.firewalls.firewalls
WHERE firewall_id = '{{ firewall_id }}';
```
