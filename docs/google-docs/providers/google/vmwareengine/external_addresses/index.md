---
title: external_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - external_addresses
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

Creates, updates, deletes, gets or lists a <code>external_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.external_addresses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this external IP address. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-address` |
| <CopyableCode code="description" /> | `string` | User-provided description for this resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="externalIp" /> | `string` | Output only. The external IP address of a workload VM. |
| <CopyableCode code="internalIp" /> | `string` | The internal IP address of a workload VM. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the resource. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="externalAddressesId, locationsId, privateCloudsId, projectsId" /> | Gets details of a single external IP address. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists external IP addresses assigned to VMware workload VMs in a given private cloud. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Creates a new `ExternalAddress` resource in a given private cloud. The network policy that corresponds to the private cloud must have the external IP address network service enabled (`NetworkPolicy.external_ip`). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="externalAddressesId, locationsId, privateCloudsId, projectsId" /> | Deletes a single external IP address. When you delete an external IP address, connectivity between the external IP address and the corresponding internal IP address is lost. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="externalAddressesId, locationsId, privateCloudsId, projectsId" /> | Updates the parameters of a single external IP address. Only fields specified in `update_mask` are applied. During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes. |

## `SELECT` examples

Lists external IP addresses assigned to VMware workload VMs in a given private cloud.

```sql
SELECT
name,
description,
createTime,
externalIp,
internalIp,
state,
uid,
updateTime
FROM google.vmwareengine.external_addresses
WHERE locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>external_addresses</code> resource.

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
INSERT INTO google.vmwareengine.external_addresses (
locationsId,
privateCloudsId,
projectsId,
internalIp,
description
)
SELECT 
'{{ locationsId }}',
'{{ privateCloudsId }}',
'{{ projectsId }}',
'{{ internalIp }}',
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
    - name: internalIp
      value: string
    - name: externalIp
      value: string
    - name: state
      value: string
    - name: uid
      value: string
    - name: description
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>external_addresses</code> resource.

```sql
/*+ update */
UPDATE google.vmwareengine.external_addresses
SET 
internalIp = '{{ internalIp }}',
description = '{{ description }}'
WHERE 
externalAddressesId = '{{ externalAddressesId }}'
AND locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>external_addresses</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmwareengine.external_addresses
WHERE externalAddressesId = '{{ externalAddressesId }}'
AND locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}';
```
