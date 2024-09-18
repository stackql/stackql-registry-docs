---
title: vmware_engine_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - vmware_engine_networks
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

Creates, updates, deletes, gets or lists a <code>vmware_engine_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vmware_engine_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.vmware_engine_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the VMware Engine network. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/global/vmwareEngineNetworks/my-network` |
| <CopyableCode code="description" /> | `string` | User-provided description for this VMware Engine network. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="etag" /> | `string` | Checksum that may be sent on update and delete requests to ensure that the user-provided value is up to date before the server processes a request. The server computes checksums based on the value of other fields in the request. |
| <CopyableCode code="state" /> | `string` | Output only. State of the VMware Engine network. |
| <CopyableCode code="type" /> | `string` | Required. VMware Engine network type. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |
| <CopyableCode code="vpcNetworks" /> | `array` | Output only. VMware Engine service VPC networks that provide connectivity from a private cloud to customer projects, the internet, and other Google Cloud services. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, vmwareEngineNetworksId" /> | Retrieves a `VmwareEngineNetwork` resource by its resource name. The resource contains details of the VMware Engine network, such as its VMware Engine network type, peered networks in a service project, and state (for example, `CREATING`, `ACTIVE`, `DELETING`). |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists `VmwareEngineNetwork` resources in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new VMware Engine network that can be used by a private cloud. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, vmwareEngineNetworksId" /> | Deletes a `VmwareEngineNetwork` resource. You can only delete a VMware Engine network after all resources that refer to it are deleted. For example, a private cloud, a network peering, and a network policy can all refer to the same VMware Engine network. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, vmwareEngineNetworksId" /> | Modifies a VMware Engine network resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied. |

## `SELECT` examples

Lists `VmwareEngineNetwork` resources in a given project and location.

```sql
SELECT
name,
description,
createTime,
etag,
state,
type,
uid,
updateTime,
vpcNetworks
FROM google.vmwareengine.vmware_engine_networks
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vmware_engine_networks</code> resource.

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
INSERT INTO google.vmwareengine.vmware_engine_networks (
locationsId,
projectsId,
description,
type,
etag
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ type }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
description: string
vpcNetworks:
  - type: string
    network: string
state: string
type: string
uid: string
etag: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>vmware_engine_networks</code> resource.

```sql
/*+ update */
UPDATE google.vmwareengine.vmware_engine_networks
SET 
description = '{{ description }}',
type = '{{ type }}',
etag = '{{ etag }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND vmwareEngineNetworksId = '{{ vmwareEngineNetworksId }}';
```

## `DELETE` example

Deletes the specified <code>vmware_engine_networks</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmwareengine.vmware_engine_networks
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND vmwareEngineNetworksId = '{{ vmwareEngineNetworksId }}';
```
