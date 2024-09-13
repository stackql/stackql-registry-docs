---
title: nat_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_addresses
  - apigee
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>nat_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nat_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.nat_addresses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Resource ID of the NAT address. |
| <CopyableCode code="ipAddress" /> | `string` | Output only. The static IPV4 address. |
| <CopyableCode code="state" /> | `string` | Output only. State of the nat address. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_instances_nat_addresses_get" /> | `SELECT` | <CopyableCode code="instancesId, natAddressesId, organizationsId" /> | Gets the details of a NAT address. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_instances_nat_addresses_list" /> | `SELECT` | <CopyableCode code="instancesId, organizationsId" /> | Lists the NAT addresses for an Apigee instance. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_instances_nat_addresses_create" /> | `INSERT` | <CopyableCode code="instancesId, organizationsId" /> | Creates a NAT address. The address is created in the RESERVED state and a static external IP address will be provisioned. At this time, the instance will not use this IP address for Internet egress traffic. The address can be activated for use once any required firewall IP whitelisting has been completed. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_instances_nat_addresses_delete" /> | `DELETE` | <CopyableCode code="instancesId, natAddressesId, organizationsId" /> | Deletes the NAT address. Connections that are actively using the address are drained before it is removed. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_instances_nat_addresses_activate" /> | `EXEC` | <CopyableCode code="instancesId, natAddressesId, organizationsId" /> | Activates the NAT address. The Apigee instance can now use this for Internet egress traffic. **Note:** Not supported for Apigee hybrid. |

## `SELECT` examples

Lists the NAT addresses for an Apigee instance. **Note:** Not supported for Apigee hybrid.

```sql
SELECT
name,
ipAddress,
state
FROM google.apigee.nat_addresses
WHERE instancesId = '{{ instancesId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>nat_addresses</code> resource.

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
INSERT INTO google.apigee.nat_addresses (
instancesId,
organizationsId,
state,
ipAddress,
name
)
SELECT 
'{{ instancesId }}',
'{{ organizationsId }}',
'{{ state }}',
'{{ ipAddress }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: state
        value: '{{ state }}'
      - name: ipAddress
        value: '{{ ipAddress }}'
      - name: name
        value: '{{ name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>nat_addresses</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.nat_addresses
WHERE instancesId = '{{ instancesId }}'
AND natAddressesId = '{{ natAddressesId }}'
AND organizationsId = '{{ organizationsId }}';
```
