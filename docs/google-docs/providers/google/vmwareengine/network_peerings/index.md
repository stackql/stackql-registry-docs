---
title: network_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - network_peerings
  - vmwareengine
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

Creates, updates, deletes, gets or lists a <code>network_peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.network_peerings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the network peering. NetworkPeering is a global resource and location can only be global. Resource names are scheme-less URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/global/networkPeerings/my-peering` |
| <CopyableCode code="description" /> | `string` | Optional. User-provided description for this network peering. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="exchangeSubnetRoutes" /> | `boolean` | Optional. True if full mesh connectivity is created and managed automatically between peered networks; false otherwise. Currently this field is always true because Google Compute Engine automatically creates and manages subnetwork routes between two VPC networks when peering state is 'ACTIVE'. |
| <CopyableCode code="exportCustomRoutes" /> | `boolean` | Optional. True if custom routes are exported to the peered network; false otherwise. The default value is true. |
| <CopyableCode code="exportCustomRoutesWithPublicIp" /> | `boolean` | Optional. True if all subnet routes with a public IP address range are exported; false otherwise. The default value is true. IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always exported to peers and are not controlled by this field. |
| <CopyableCode code="importCustomRoutes" /> | `boolean` | Optional. True if custom routes are imported from the peered network; false otherwise. The default value is true. |
| <CopyableCode code="importCustomRoutesWithPublicIp" /> | `boolean` | Optional. True if all subnet routes with public IP address range are imported; false otherwise. The default value is true. IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always imported to peers and are not controlled by this field. |
| <CopyableCode code="peerMtu" /> | `integer` | Optional. Maximum transmission unit (MTU) in bytes. The default value is `1500`. If a value of `0` is provided for this field, VMware Engine uses the default value instead. |
| <CopyableCode code="peerNetwork" /> | `string` | Required. The relative resource name of the network to peer with a standard VMware Engine network. The provided network can be a consumer VPC network or another standard VMware Engine network. If the `peer_network_type` is VMWARE_ENGINE_NETWORK, specify the name in the form: `projects/{project}/locations/global/vmwareEngineNetworks/{vmware_engine_network_id}`. Otherwise specify the name in the form: `projects/{project}/global/networks/{network_id}`, where `{project}` can either be a project number or a project ID. |
| <CopyableCode code="peerNetworkType" /> | `string` | Required. The type of the network to peer with the VMware Engine network. |
| <CopyableCode code="state" /> | `string` | Output only. State of the network peering. This field has a value of 'ACTIVE' when there's a matching configuration in the peer network. New values may be added to this enum when appropriate. |
| <CopyableCode code="stateDetails" /> | `string` | Output only. Output Only. Details about the current state of the network peering. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |
| <CopyableCode code="vmwareEngineNetwork" /> | `string` | Required. The relative resource name of the VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}` where `{project}` can either be a project number or a project ID. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, networkPeeringsId, projectsId" /> | Retrieves a `NetworkPeering` resource by its resource name. The resource contains details of the network peering, such as peered networks, import and export custom route configurations, and peering state. NetworkPeering is a global resource and location can only be global. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists `NetworkPeering` resources in a given project. NetworkPeering is a global resource and location can only be global. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new network peering between the peer network and VMware Engine network provided in a `NetworkPeering` resource. NetworkPeering is a global resource and location can only be global. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, networkPeeringsId, projectsId" /> | Deletes a `NetworkPeering` resource. When a network peering is deleted for a VMware Engine network, the peer network becomes inaccessible to that VMware Engine network. NetworkPeering is a global resource and location can only be global. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, networkPeeringsId, projectsId" /> | Modifies a `NetworkPeering` resource. Only the `description` field can be updated. Only fields specified in `updateMask` are applied. NetworkPeering is a global resource and location can only be global. |

## `SELECT` examples

Lists `NetworkPeering` resources in a given project. NetworkPeering is a global resource and location can only be global.

```sql
SELECT
name,
description,
createTime,
exchangeSubnetRoutes,
exportCustomRoutes,
exportCustomRoutesWithPublicIp,
importCustomRoutes,
importCustomRoutesWithPublicIp,
peerMtu,
peerNetwork,
peerNetworkType,
state,
stateDetails,
uid,
updateTime,
vmwareEngineNetwork
FROM google.vmwareengine.network_peerings
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_peerings</code> resource.

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
INSERT INTO google.vmwareengine.network_peerings (
locationsId,
projectsId,
peerNetwork,
exportCustomRoutes,
importCustomRoutes,
exchangeSubnetRoutes,
exportCustomRoutesWithPublicIp,
importCustomRoutesWithPublicIp,
peerMtu,
peerNetworkType,
vmwareEngineNetwork,
description
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ peerNetwork }}',
{{ exportCustomRoutes }},
{{ importCustomRoutes }},
{{ exchangeSubnetRoutes }},
{{ exportCustomRoutesWithPublicIp }},
{{ importCustomRoutesWithPublicIp }},
'{{ peerMtu }}',
'{{ peerNetworkType }}',
'{{ vmwareEngineNetwork }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: peerNetwork
      value: string
    - name: exportCustomRoutes
      value: boolean
    - name: importCustomRoutes
      value: boolean
    - name: exchangeSubnetRoutes
      value: boolean
    - name: exportCustomRoutesWithPublicIp
      value: boolean
    - name: importCustomRoutesWithPublicIp
      value: boolean
    - name: state
      value: string
    - name: stateDetails
      value: string
    - name: peerMtu
      value: integer
    - name: peerNetworkType
      value: string
    - name: uid
      value: string
    - name: vmwareEngineNetwork
      value: string
    - name: description
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_peerings</code> resource.

```sql
/*+ update */
UPDATE google.vmwareengine.network_peerings
SET 
peerNetwork = '{{ peerNetwork }}',
exportCustomRoutes = true|false,
importCustomRoutes = true|false,
exchangeSubnetRoutes = true|false,
exportCustomRoutesWithPublicIp = true|false,
importCustomRoutesWithPublicIp = true|false,
peerMtu = '{{ peerMtu }}',
peerNetworkType = '{{ peerNetworkType }}',
vmwareEngineNetwork = '{{ vmwareEngineNetwork }}',
description = '{{ description }}'
WHERE 
locationsId = '{{ locationsId }}'
AND networkPeeringsId = '{{ networkPeeringsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>network_peerings</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmwareengine.network_peerings
WHERE locationsId = '{{ locationsId }}'
AND networkPeeringsId = '{{ networkPeeringsId }}'
AND projectsId = '{{ projectsId }}';
```
