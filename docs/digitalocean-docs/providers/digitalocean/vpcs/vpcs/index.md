---
title: vpcs
hide_title: false
hide_table_of_contents: false
keywords:
  - vpcs
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

Creates, updates, deletes, gets or lists a <code>vpcs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpcs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.vpcs.vpcs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference the VPC. |
| <CopyableCode code="name" /> | `string` | The name of the VPC. Must be unique and may only contain alphanumeric characters, dashes, and periods. |
| <CopyableCode code="description" /> | `string` | A free-form text field for describing the VPC's purpose. It may be a maximum of 255 characters. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format. |
| <CopyableCode code="default" /> | `boolean` | A boolean value indicating whether or not the VPC is the default network for the region. All applicable resources are placed into the default VPC network unless otherwise specified during their creation. The `default` field cannot be unset from `true`. If you want to set a new default VPC network, update the `default` field of another VPC network in the same region. The previous network's `default` field will be set to `false` when a new default VPC has been defined. |
| <CopyableCode code="ip_range" /> | `string` | The range of IP addresses in the VPC in CIDR notation. Network ranges cannot overlap with other networks in the same account and must be in range of private addresses as defined in RFC1918. It may not be smaller than `/28` nor larger than `/16`. If no IP range is specified, a `/20` network range is generated that won't conflict with other VPC networks in your account. |
| <CopyableCode code="region" /> | `string` | The slug identifier for the region where the VPC will be created. |
| <CopyableCode code="urn" /> | `string` | The uniform resource name (URN) for the resource in the format do:resource_type:resource_id. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="vpcs_get" /> | `SELECT` | <CopyableCode code="vpc_id" /> | To show information about an existing VPC, send a GET request to `/v2/vpcs/$VPC_ID`. |
| <CopyableCode code="vpcs_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of the VPCs on your account, send a GET request to `/v2/vpcs`. |
| <CopyableCode code="vpcs_create" /> | `INSERT` | <CopyableCode code="" /> | To create a VPC, send a POST request to `/v2/vpcs` specifying the attributes in the table below in the JSON body. **Note:** If you do not currently have a VPC network in a specific datacenter region, the first one that you create will be set as the default for that region. The default VPC for a region cannot be changed or deleted. |
| <CopyableCode code="vpcs_delete" /> | `DELETE` | <CopyableCode code="vpc_id" /> | To delete a VPC, send a DELETE request to `/v2/vpcs/$VPC_ID`. A 204 status code with no body will be returned in response to a successful request. The default VPC for a region can not be deleted. Additionally, a VPC can only be deleted if it does not contain any member resources. Attempting to delete a region's default VPC or a VPC that still has members will result in a 403 Forbidden error response. |
| <CopyableCode code="vpcs_patch" /> | `UPDATE` | <CopyableCode code="vpc_id" /> | To update a subset of information about a VPC, send a PATCH request to `/v2/vpcs/$VPC_ID`. |
| <CopyableCode code="vpcs_update" /> | `EXEC` | <CopyableCode code="vpc_id" /> | To update information about a VPC, send a PUT request to `/v2/vpcs/$VPC_ID`. |

## `SELECT` examples

To list all of the VPCs on your account, send a GET request to `/v2/vpcs`.


```sql
SELECT
id,
name,
description,
created_at,
default,
ip_range,
region,
urn
FROM digitalocean.vpcs.vpcs
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpcs</code> resource.

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
INSERT INTO digitalocean.vpcs.vpcs (

)
SELECT 

;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: vpcs
  props: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>vpcs</code> resource.

```sql
/*+ update */
UPDATE digitalocean.vpcs.vpcs
SET 

WHERE 
vpc_id = '{{ vpc_id }}';
```

## `DELETE` example

Deletes the specified <code>vpcs</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.vpcs.vpcs
WHERE vpc_id = '{{ vpc_id }}';
```
