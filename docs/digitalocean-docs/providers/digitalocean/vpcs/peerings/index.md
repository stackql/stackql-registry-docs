---
title: peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - peerings
  - vpcs
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

Creates, updates, deletes, gets or lists a <code>peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.vpcs.peerings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference the VPC peering. |
| <CopyableCode code="name" /> | `string` | The name of the VPC peering. Must be unique within the team and may only contain alphanumeric characters and dashes. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format. |
| <CopyableCode code="status" /> | `string` | The current status of the VPC peering. |
| <CopyableCode code="vpc_ids" /> | `array` | An array of the two peered VPCs IDs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="vpcs_list_peerings" /> | `SELECT` | <CopyableCode code="vpc_id" /> | To list all of a VPC's peerings, send a GET request to `/v2/vpcs/$VPC_ID/peerings`. |
| <CopyableCode code="vpcs_create_peerings" /> | `INSERT` | <CopyableCode code="vpc_id, data__name, data__vpc_id" /> | To create a new VPC peering for a given VPC, send a POST request to `/v2/vpcs/$VPC_ID/peerings`. |
| <CopyableCode code="vpcs_patch_peerings" /> | `UPDATE` | <CopyableCode code="vpc_id, vpc_peering_id" /> | To update the name of a VPC peering in a particular VPC, send a PATCH request to `/v2/vpcs/$VPC_ID/peerings/$VPC_PEERING_ID` with the new `name` in the request body. |

## `SELECT` examples

To list all of a VPC's peerings, send a GET request to `/v2/vpcs/$VPC_ID/peerings`.


```sql
SELECT
id,
name,
created_at,
status,
vpc_ids
FROM digitalocean.vpcs.peerings
WHERE vpc_id = '{{ vpc_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>peerings</code> resource.

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
INSERT INTO digitalocean.vpcs.peerings (
data__name,
data__vpc_id,
vpc_id
)
SELECT 
'{{ name }}',
'{{ vpc_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: peerings
  props:
    - name: vpc_id
      value: string
    - name: data__name
      value: string
    - name: data__vpc_id
      value: string
    - name: name
      value: string
    - name: vpc_id
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>peerings</code> resource.

```sql
/*+ update */
UPDATE digitalocean.vpcs.peerings
SET 

WHERE 
vpc_id = '{{ vpc_id }}'
AND vpc_peering_id = '{{ vpc_peering_id }}';
```
