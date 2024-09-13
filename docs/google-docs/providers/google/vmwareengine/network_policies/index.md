---
title: network_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - network_policies
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

Creates, updates, deletes, gets or lists a <code>network_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.network_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this network policy. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1/networkPolicies/my-network-policy` |
| <CopyableCode code="description" /> | `string` | Optional. User-provided description for this network policy. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="edgeServicesCidr" /> | `string` | Required. IP address range in CIDR notation used to create internet access and external IP access. An RFC 1918 CIDR block, with a "/26" prefix, is required. The range cannot overlap with any prefixes either in the consumer VPC network or in use by the private clouds attached to that VPC network. |
| <CopyableCode code="externalIp" /> | `object` | Represents a network service that is managed by a `NetworkPolicy` resource. A network service provides a way to control an aspect of external access to VMware workloads. For example, whether the VMware workloads in the private clouds governed by a network policy can access or be accessed from the internet. |
| <CopyableCode code="internetAccess" /> | `object` | Represents a network service that is managed by a `NetworkPolicy` resource. A network service provides a way to control an aspect of external access to VMware workloads. For example, whether the VMware workloads in the private clouds governed by a network policy can access or be accessed from the internet. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |
| <CopyableCode code="vmwareEngineNetwork" /> | `string` | Optional. The relative resource name of the VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}` where `{project}` can either be a project number or a project ID. |
| <CopyableCode code="vmwareEngineNetworkCanonical" /> | `string` | Output only. The canonical name of the VMware Engine network in the form: `projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, networkPoliciesId, projectsId" /> | Retrieves a `NetworkPolicy` resource by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists `NetworkPolicy` resources in a specified project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new network policy in a given VMware Engine network of a project and location (region). A new network policy cannot be created if another network policy already exists in the same scope. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, networkPoliciesId, projectsId" /> | Deletes a `NetworkPolicy` resource. A network policy cannot be deleted when `NetworkService.state` is set to `RECONCILING` for either its external IP or internet access service. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, networkPoliciesId, projectsId" /> | Modifies a `NetworkPolicy` resource. Only the following fields can be updated: `internet_access`, `external_ip`, `edge_services_cidr`. Only fields specified in `updateMask` are applied. When updating a network policy, the external IP network service can only be disabled if there are no external IP addresses present in the scope of the policy. Also, a `NetworkService` cannot be updated when `NetworkService.state` is set to `RECONCILING`. During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes. |

## `SELECT` examples

Lists `NetworkPolicy` resources in a specified project and location.

```sql
SELECT
name,
description,
createTime,
edgeServicesCidr,
externalIp,
internetAccess,
uid,
updateTime,
vmwareEngineNetwork,
vmwareEngineNetworkCanonical
FROM google.vmwareengine.network_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_policies</code> resource.

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
INSERT INTO google.vmwareengine.network_policies (
locationsId,
projectsId,
name,
createTime,
updateTime,
internetAccess,
externalIp,
edgeServicesCidr,
uid,
vmwareEngineNetwork,
description,
vmwareEngineNetworkCanonical
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ internetAccess }}',
'{{ externalIp }}',
'{{ edgeServicesCidr }}',
'{{ uid }}',
'{{ vmwareEngineNetwork }}',
'{{ description }}',
'{{ vmwareEngineNetworkCanonical }}'
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
      - name: internetAccess
        value: '{{ internetAccess }}'
      - name: externalIp
        value: '{{ externalIp }}'
      - name: edgeServicesCidr
        value: '{{ edgeServicesCidr }}'
      - name: uid
        value: '{{ uid }}'
      - name: vmwareEngineNetwork
        value: '{{ vmwareEngineNetwork }}'
      - name: description
        value: '{{ description }}'
      - name: vmwareEngineNetworkCanonical
        value: '{{ vmwareEngineNetworkCanonical }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_policies</code> resource.

```sql
/*+ update */
UPDATE google.vmwareengine.network_policies
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
internetAccess = '{{ internetAccess }}',
externalIp = '{{ externalIp }}',
edgeServicesCidr = '{{ edgeServicesCidr }}',
uid = '{{ uid }}',
vmwareEngineNetwork = '{{ vmwareEngineNetwork }}',
description = '{{ description }}',
vmwareEngineNetworkCanonical = '{{ vmwareEngineNetworkCanonical }}'
WHERE 
locationsId = '{{ locationsId }}'
AND networkPoliciesId = '{{ networkPoliciesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>network_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmwareengine.network_policies
WHERE locationsId = '{{ locationsId }}'
AND networkPoliciesId = '{{ networkPoliciesId }}'
AND projectsId = '{{ projectsId }}';
```
