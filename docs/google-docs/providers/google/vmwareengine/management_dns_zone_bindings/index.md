---
title: management_dns_zone_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - management_dns_zone_bindings
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

Creates, updates, deletes, gets or lists a <code>management_dns_zone_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management_dns_zone_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.management_dns_zone_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this binding. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding` |
| <CopyableCode code="description" /> | `string` | User-provided description for this resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the resource. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |
| <CopyableCode code="vmwareEngineNetwork" /> | `string` | Network to bind is a VMware Engine network. Specify the name in the following form for VMware engine network: `projects/{project}/locations/global/vmwareEngineNetworks/{vmware_engine_network_id}`. `{project}` can either be a project number or a project ID. |
| <CopyableCode code="vpcNetwork" /> | `string` | Network to bind is a standard consumer VPC. Specify the name in the following form for consumer VPC network: `projects/{project}/global/networks/{network_id}`. `{project}` can either be a project number or a project ID. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, managementDnsZoneBindingsId, privateCloudsId, projectsId" /> | Retrieves a 'ManagementDnsZoneBinding' resource by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists Consumer VPCs bound to Management DNS Zone of a given private cloud. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Creates a new `ManagementDnsZoneBinding` resource in a private cloud. This RPC creates the DNS binding and the resource that represents the DNS binding of the consumer VPC network to the management DNS zone. A management DNS zone is the Cloud DNS cross-project binding zone that VMware Engine creates for each private cloud. It contains FQDNs and corresponding IP addresses for the private cloud's ESXi hosts and management VM appliances like vCenter and NSX Manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, managementDnsZoneBindingsId, privateCloudsId, projectsId" /> | Deletes a `ManagementDnsZoneBinding` resource. When a management DNS zone binding is deleted, the corresponding consumer VPC network is no longer bound to the management DNS zone. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, managementDnsZoneBindingsId, privateCloudsId, projectsId" /> | Updates a `ManagementDnsZoneBinding` resource. Only fields specified in `update_mask` are applied. |
| <CopyableCode code="repair" /> | `EXEC` | <CopyableCode code="locationsId, managementDnsZoneBindingsId, privateCloudsId, projectsId" /> | Retries to create a `ManagementDnsZoneBinding` resource that is in failed state. |

## `SELECT` examples

Lists Consumer VPCs bound to Management DNS Zone of a given private cloud.

```sql
SELECT
name,
description,
createTime,
state,
uid,
updateTime,
vmwareEngineNetwork,
vpcNetwork
FROM google.vmwareengine.management_dns_zone_bindings
WHERE locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>management_dns_zone_bindings</code> resource.

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
INSERT INTO google.vmwareengine.management_dns_zone_bindings (
locationsId,
privateCloudsId,
projectsId,
name,
createTime,
updateTime,
state,
description,
vpcNetwork,
vmwareEngineNetwork,
uid
)
SELECT 
'{{ locationsId }}',
'{{ privateCloudsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ state }}',
'{{ description }}',
'{{ vpcNetwork }}',
'{{ vmwareEngineNetwork }}',
'{{ uid }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: state
      value: '{{ state }}'
    - name: description
      value: '{{ description }}'
    - name: vpcNetwork
      value: '{{ vpcNetwork }}'
    - name: vmwareEngineNetwork
      value: '{{ vmwareEngineNetwork }}'
    - name: uid
      value: '{{ uid }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>management_dns_zone_bindings</code> resource.

```sql
/*+ update */
UPDATE google.vmwareengine.management_dns_zone_bindings
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
state = '{{ state }}',
description = '{{ description }}',
vpcNetwork = '{{ vpcNetwork }}',
vmwareEngineNetwork = '{{ vmwareEngineNetwork }}',
uid = '{{ uid }}'
WHERE 
locationsId = '{{ locationsId }}'
AND managementDnsZoneBindingsId = '{{ managementDnsZoneBindingsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>management_dns_zone_bindings</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmwareengine.management_dns_zone_bindings
WHERE locationsId = '{{ locationsId }}'
AND managementDnsZoneBindingsId = '{{ managementDnsZoneBindingsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}';
```
