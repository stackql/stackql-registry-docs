---
title: private_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_connections
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

Creates, updates, deletes, gets or lists a <code>private_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.private_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the private connection. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1/privateConnections/my-connection` |
| <CopyableCode code="description" /> | `string` | Optional. User-provided description for this private connection. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="peeringId" /> | `string` | Output only. VPC network peering id between given network VPC and VMwareEngineNetwork. |
| <CopyableCode code="peeringState" /> | `string` | Output only. Peering state between service network and VMware Engine network. |
| <CopyableCode code="routingMode" /> | `string` | Optional. Routing Mode. Default value is set to GLOBAL. For type = PRIVATE_SERVICE_ACCESS, this field can be set to GLOBAL or REGIONAL, for other types only GLOBAL is supported. |
| <CopyableCode code="serviceNetwork" /> | `string` | Required. Service network to create private connection. Specify the name in the following form: `projects/{project}/global/networks/{network_id}` For type = PRIVATE_SERVICE_ACCESS, this field represents servicenetworking VPC, e.g. projects/project-tp/global/networks/servicenetworking. For type = NETAPP_CLOUD_VOLUME, this field represents NetApp service VPC, e.g. projects/project-tp/global/networks/netapp-tenant-vpc. For type = DELL_POWERSCALE, this field represent Dell service VPC, e.g. projects/project-tp/global/networks/dell-tenant-vpc. For type= THIRD_PARTY_SERVICE, this field could represent a consumer VPC or any other producer VPC to which the VMware Engine Network needs to be connected, e.g. projects/project/global/networks/vpc. |
| <CopyableCode code="state" /> | `string` | Output only. State of the private connection. |
| <CopyableCode code="type" /> | `string` | Required. Private connection type. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |
| <CopyableCode code="vmwareEngineNetwork" /> | `string` | Required. The relative resource name of Legacy VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}` where `{project}`, `{location}` will be same as specified in private connection resource name and `{vmware_engine_network_id}` will be in the form of `{location}`-default e.g. projects/project/locations/us-central1/vmwareEngineNetworks/us-central1-default. |
| <CopyableCode code="vmwareEngineNetworkCanonical" /> | `string` | Output only. The canonical name of the VMware Engine network in the form: `projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Retrieves a `PrivateConnection` resource by its resource name. The resource contains details of the private connection, such as connected network, routing mode and state. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists `PrivateConnection` resources in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new private connection that can be used for accessing private Clouds. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Deletes a `PrivateConnection` resource. When a private connection is deleted for a VMware Engine network, the connected network becomes inaccessible to that VMware Engine network. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Modifies a `PrivateConnection` resource. Only `description` and `routing_mode` fields can be updated. Only fields specified in `updateMask` are applied. |

## `SELECT` examples

Lists `PrivateConnection` resources in a given project and location.

```sql
SELECT
name,
description,
createTime,
peeringId,
peeringState,
routingMode,
serviceNetwork,
state,
type,
uid,
updateTime,
vmwareEngineNetwork,
vmwareEngineNetworkCanonical
FROM google.vmwareengine.private_connections
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_connections</code> resource.

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
INSERT INTO google.vmwareengine.private_connections (
locationsId,
projectsId,
name,
createTime,
updateTime,
description,
state,
vmwareEngineNetwork,
vmwareEngineNetworkCanonical,
type,
peeringId,
routingMode,
uid,
serviceNetwork,
peeringState
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ description }}',
'{{ state }}',
'{{ vmwareEngineNetwork }}',
'{{ vmwareEngineNetworkCanonical }}',
'{{ type }}',
'{{ peeringId }}',
'{{ routingMode }}',
'{{ uid }}',
'{{ serviceNetwork }}',
'{{ peeringState }}'
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
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: description
        value: '{{ description }}'
      - name: state
        value: '{{ state }}'
      - name: vmwareEngineNetwork
        value: '{{ vmwareEngineNetwork }}'
      - name: vmwareEngineNetworkCanonical
        value: '{{ vmwareEngineNetworkCanonical }}'
      - name: type
        value: '{{ type }}'
      - name: peeringId
        value: '{{ peeringId }}'
      - name: routingMode
        value: '{{ routingMode }}'
      - name: uid
        value: '{{ uid }}'
      - name: serviceNetwork
        value: '{{ serviceNetwork }}'
      - name: peeringState
        value: '{{ peeringState }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>private_connections</code> resource.

```sql
/*+ update */
UPDATE google.vmwareengine.private_connections
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
description = '{{ description }}',
state = '{{ state }}',
vmwareEngineNetwork = '{{ vmwareEngineNetwork }}',
vmwareEngineNetworkCanonical = '{{ vmwareEngineNetworkCanonical }}',
type = '{{ type }}',
peeringId = '{{ peeringId }}',
routingMode = '{{ routingMode }}',
uid = '{{ uid }}',
serviceNetwork = '{{ serviceNetwork }}',
peeringState = '{{ peeringState }}'
WHERE 
locationsId = '{{ locationsId }}'
AND privateConnectionsId = '{{ privateConnectionsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>private_connections</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmwareengine.private_connections
WHERE locationsId = '{{ locationsId }}'
AND privateConnectionsId = '{{ privateConnectionsId }}'
AND projectsId = '{{ projectsId }}';
```
