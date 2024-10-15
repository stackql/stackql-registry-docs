---
title: scale_units_from_json
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_units_from_json
  - fabric_admin
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

Creates, updates, deletes, gets or lists a <code>scale_units_from_json</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scale_units_from_json</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.scale_units_from_json" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="location, resourceGroupName, scaleUnit, subscriptionId" /> | Add a new scale unit. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scale_units_from_json</code> resource.

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
INSERT INTO azure_stack.fabric_admin.scale_units_from_json (
location,
resourceGroupName,
scaleUnit,
subscriptionId,
clusterName,
physicalNodes,
torSwitchBgpAsn,
softwareBgpAsn,
torSwitchBgpPeerIp,
infrastructureNetwork,
storageNetwork,
netQosPriority
)
SELECT 
'{{ location }}',
'{{ resourceGroupName }}',
'{{ scaleUnit }}',
'{{ subscriptionId }}',
'{{ clusterName }}',
'{{ physicalNodes }}',
'{{ torSwitchBgpAsn }}',
'{{ softwareBgpAsn }}',
'{{ torSwitchBgpPeerIp }}',
'{{ infrastructureNetwork }}',
'{{ storageNetwork }}',
'{{ netQosPriority }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: clusterName
      value: string
    - name: physicalNodes
      value:
        - - name: bmcIpAddress
            value: string
          - name: name
            value: string
    - name: torSwitchBgpAsn
      value: string
    - name: softwareBgpAsn
      value: string
    - name: torSwitchBgpPeerIp
      value:
        - string
    - name: infrastructureNetwork
      value:
        - name: subnet
          value:
            - string
        - name: vlanId
          value:
            - string
    - name: netQosPriority
      value: integer

```
</TabItem>
</Tabs>
