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

Creates, updates, deletes, gets or lists a <code>networks_peering</code> resource.

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
{{ autoCreateRoutes }},
'{{ networkPeering }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: peerNetwork
      value: string
    - name: autoCreateRoutes
      value: boolean
    - name: networkPeering
      value:
        - name: name
          value: string
        - name: network
          value: string
        - name: state
          value: string
        - name: stateDetails
          value: string
        - name: autoCreateRoutes
          value: boolean
        - name: exportCustomRoutes
          value: boolean
        - name: importCustomRoutes
          value: boolean
        - name: exchangeSubnetRoutes
          value: boolean
        - name: exportSubnetRoutesWithPublicIp
          value: boolean
        - name: importSubnetRoutesWithPublicIp
          value: boolean
        - name: peerMtu
          value: integer
        - name: stackType
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>networks_peering</code> resource.

```sql
/*+ update */
UPDATE google.compute.networks_peering
SET 
networkPeering = '{{ networkPeering }}'
WHERE 
network = '{{ network }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified <code>networks_peering</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.networks_peering
WHERE network = '{{ network }}'
AND project = '{{ project }}';
```
