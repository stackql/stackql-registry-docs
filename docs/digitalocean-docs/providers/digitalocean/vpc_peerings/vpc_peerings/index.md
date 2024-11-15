---
title: vpc_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_peerings
  - vpc_peerings
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

Creates, updates, deletes, gets or lists a <code>vpc_peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.vpc_peerings.vpc_peerings" /></td></tr>
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
| <CopyableCode code="vpc_peerings_get" /> | `SELECT` | <CopyableCode code="vpc_peering_id" /> | To show information about an existing VPC Peering, send a GET request to `/v2/vpc_peerings/$VPC_PEERING_ID`. |
| <CopyableCode code="vpc_peerings_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of the VPC peerings on your account, send a GET request to `/v2/vpc_peerings`. |
| <CopyableCode code="vpc_peerings_create" /> | `INSERT` | <CopyableCode code="" /> | To create a new VPC Peering, send a POST request to `/v2/vpc_peerings` specifying a name and a list of two VPC IDs to peer. The response code, 202 Accepted, does not indicate the success or failure of the operation, just that the request has been accepted for processing. |
| <CopyableCode code="vpc_peerings_delete" /> | `DELETE` | <CopyableCode code="vpc_peering_id" /> | To delete a VPC peering, send a DELETE request to `/v2/vpc_peerings/$VPC_PEERING_ID`. |
| <CopyableCode code="vpc_peerings_patch" /> | `UPDATE` | <CopyableCode code="vpc_peering_id" /> | To update the name of a VPC peering, send a PATCH request to `/v2/vpc_peerings/$VPC_PEERING_ID` with the new `name` in the request body. |

## `SELECT` examples

To list all of the VPC peerings on your account, send a GET request to `/v2/vpc_peerings`.


```sql
SELECT
id,
name,
created_at,
status,
vpc_ids
FROM digitalocean.vpc_peerings.vpc_peerings
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_peerings</code> resource.

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
INSERT INTO digitalocean.vpc_peerings.vpc_peerings (

)
SELECT 

;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: vpc_peerings
  props: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>vpc_peerings</code> resource.

```sql
/*+ update */
UPDATE digitalocean.vpc_peerings.vpc_peerings
SET 

WHERE 
vpc_peering_id = '{{ vpc_peering_id }}';
```

## `DELETE` example

Deletes the specified <code>vpc_peerings</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.vpc_peerings.vpc_peerings
WHERE vpc_peering_id = '{{ vpc_peering_id }}';
```
