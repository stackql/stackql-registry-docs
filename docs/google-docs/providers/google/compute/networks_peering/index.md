
---
title: networks_peering
hide_title: false
hide_table_of_contents: false
keywords:
  - networks_peering
  - compute
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

Creates, updates, deletes or gets an <code>networks_peering</code> resource or lists <code>networks_peering</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks_peering</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.networks_peering" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_peering" /> | `INSERT` | <CopyableCode code="network, project" /> | Adds a peering to the specified network. |
| <CopyableCode code="remove_peering" /> | `DELETE` | <CopyableCode code="network, project" /> | Removes a peering from the specified network. |
| <CopyableCode code="update_peering" /> | `UPDATE` | <CopyableCode code="network, project" /> | Updates the specified network peering with the data included in the request. You can only modify the NetworkPeering.export_custom_routes field and the NetworkPeering.import_custom_routes field. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>networks_peering</code> resource.

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
INSERT INTO google.compute.networks_peering (
network,
project,
name,
peerNetwork,
autoCreateRoutes,
networkPeering
)
SELECT 
'{{ network }}',
'{{ project }}',
'{{ name }}',
'{{ peerNetwork }}',
true|false,
'{{ networkPeering }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: peerNetwork
        value: '{{ peerNetwork }}'
      - name: autoCreateRoutes
        value: '{{ autoCreateRoutes }}'
      - name: networkPeering
        value: '{{ networkPeering }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a networks_peering only if the necessary resources are available.

```sql
UPDATE google.compute.networks_peering
SET 
networkPeering = '{{ networkPeering }}'
WHERE 
network = '{{ network }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified networks_peering resource.

```sql
DELETE FROM google.compute.networks_peering
WHERE network = '{{ network }}'
AND project = '{{ project }}';
```
