---
title: devices_signed
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_signed
  - sasportal
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

Creates, updates, deletes, gets or lists a <code>devices_signed</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices_signed</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sasportal.devices_signed" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="customers_deployments_devices_create_signed" /> | `INSERT` | <CopyableCode code="customersId, deploymentsId" /> | Creates a signed device under a node or customer. |
| <CopyableCode code="customers_devices_create_signed" /> | `INSERT` | <CopyableCode code="customersId" /> | Creates a signed device under a node or customer. |
| <CopyableCode code="customers_nodes_devices_create_signed" /> | `INSERT` | <CopyableCode code="customersId, nodesId" /> | Creates a signed device under a node or customer. |
| <CopyableCode code="nodes_deployments_devices_create_signed" /> | `INSERT` | <CopyableCode code="deploymentsId, nodesId" /> | Creates a signed device under a node or customer. |
| <CopyableCode code="nodes_devices_create_signed" /> | `INSERT` | <CopyableCode code="nodesId" /> | Creates a signed device under a node or customer. |
| <CopyableCode code="nodes_nodes_devices_create_signed" /> | `INSERT` | <CopyableCode code="nodesId, nodesId1" /> | Creates a signed device under a node or customer. |
| <CopyableCode code="customers_devices_update_signed" /> | `UPDATE` | <CopyableCode code="customersId, devicesId" /> | Updates a signed device. |
| <CopyableCode code="deployments_devices_update_signed" /> | `UPDATE` | <CopyableCode code="deploymentsId, devicesId" /> | Updates a signed device. |
| <CopyableCode code="nodes_devices_update_signed" /> | `UPDATE` | <CopyableCode code="devicesId, nodesId" /> | Updates a signed device. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>devices_signed</code> resource.

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
INSERT INTO google.sasportal.devices_signed (
nodesId,
installerId,
encodedDevice
)
SELECT 
'{{ nodesId }}',
'{{ installerId }}',
'{{ encodedDevice }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
installerId: string
encodedDevice: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>devices_signed</code> resource.

```sql
/*+ update */
UPDATE google.sasportal.devices_signed
SET 
installerId = '{{ installerId }}',
encodedDevice = '{{ encodedDevice }}'
WHERE 
devicesId = '{{ devicesId }}'
AND nodesId = '{{ nodesId }}';
```
