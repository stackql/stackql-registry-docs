---
title: private_clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds
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

Creates, updates, deletes, gets or lists a <code>private_clouds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_clouds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.private_clouds" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this private cloud. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud` |
| <CopyableCode code="description" /> | `string` | User-provided description for this private cloud. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Time when the resource was scheduled for deletion. |
| <CopyableCode code="expireTime" /> | `string` | Output only. Time when the resource will be irreversibly deleted. |
| <CopyableCode code="hcx" /> | `object` | Details about a HCX Cloud Manager appliance. |
| <CopyableCode code="managementCluster" /> | `object` | Management cluster configuration. |
| <CopyableCode code="networkConfig" /> | `object` | Network configuration in the consumer project with which the peering has to be done. |
| <CopyableCode code="nsx" /> | `object` | Details about a NSX Manager appliance. |
| <CopyableCode code="state" /> | `string` | Output only. State of the resource. New values may be added to this enum when appropriate. |
| <CopyableCode code="type" /> | `string` | Optional. Type of the private cloud. Defaults to STANDARD. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |
| <CopyableCode code="vcenter" /> | `object` | Details about a vCenter Server management appliance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Retrieves a `PrivateCloud` resource by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists `PrivateCloud` resources in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new `PrivateCloud` resource in a given project and location. Private clouds of type `STANDARD` and `TIME_LIMITED` are zonal resources, `STRETCHED` private clouds are regional. Creating a private cloud also creates a [management cluster](https://cloud.google.com/vmware-engine/docs/concepts-vmware-components) for that private cloud. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Schedules a `PrivateCloud` resource for deletion. A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `expireTime` set to the time when deletion is final and can no longer be reversed. The delete operation is marked as done as soon as the `PrivateCloud` is successfully scheduled for deletion (this also applies when `delayHours` is set to zero), and the operation is not kept in pending state until `PrivateCloud` is purged. `PrivateCloud` can be restored using `UndeletePrivateCloud` method before the `expireTime` elapses. When `expireTime` is reached, deletion is final and all private cloud resources are irreversibly removed and billing stops. During the final removal process, `PrivateCloud.state` is set to `PURGING`. `PrivateCloud` can be polled using standard `GET` method for the whole period of deletion and purging. It will not be returned only when it is completely purged. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Modifies a `PrivateCloud` resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied. During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes. |
| <CopyableCode code="reset_nsx_credentials" /> | `EXEC` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Resets credentials of the NSX appliance. |
| <CopyableCode code="reset_vcenter_credentials" /> | `EXEC` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Resets credentials of the Vcenter appliance. |
| <CopyableCode code="show_nsx_credentials" /> | `EXEC` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Gets details of credentials for NSX appliance. |
| <CopyableCode code="show_vcenter_credentials" /> | `EXEC` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Gets details of credentials for Vcenter appliance. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Restores a private cloud that was previously scheduled for deletion by `DeletePrivateCloud`. A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `PrivateCloud.expireTime` set to the time when deletion can no longer be reversed. |

## `SELECT` examples

Lists `PrivateCloud` resources in a given project and location.

```sql
SELECT
name,
description,
createTime,
deleteTime,
expireTime,
hcx,
managementCluster,
networkConfig,
nsx,
state,
type,
uid,
updateTime,
vcenter
FROM google.vmwareengine.private_clouds
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_clouds</code> resource.

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
INSERT INTO google.vmwareengine.private_clouds (
locationsId,
projectsId,
name,
createTime,
updateTime,
deleteTime,
expireTime,
state,
networkConfig,
managementCluster,
description,
hcx,
nsx,
vcenter,
uid,
type
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ expireTime }}',
'{{ state }}',
'{{ networkConfig }}',
'{{ managementCluster }}',
'{{ description }}',
'{{ hcx }}',
'{{ nsx }}',
'{{ vcenter }}',
'{{ uid }}',
'{{ type }}'
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
    - name: deleteTime
      value: '{{ deleteTime }}'
    - name: expireTime
      value: '{{ expireTime }}'
    - name: state
      value: '{{ state }}'
    - name: networkConfig
      value: '{{ networkConfig }}'
    - name: managementCluster
      value: '{{ managementCluster }}'
    - name: description
      value: '{{ description }}'
    - name: hcx
      value: '{{ hcx }}'
    - name: nsx
      value: '{{ nsx }}'
    - name: vcenter
      value: '{{ vcenter }}'
    - name: uid
      value: '{{ uid }}'
    - name: type
      value: '{{ type }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>private_clouds</code> resource.

```sql
/*+ update */
UPDATE google.vmwareengine.private_clouds
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
deleteTime = '{{ deleteTime }}',
expireTime = '{{ expireTime }}',
state = '{{ state }}',
networkConfig = '{{ networkConfig }}',
managementCluster = '{{ managementCluster }}',
description = '{{ description }}',
hcx = '{{ hcx }}',
nsx = '{{ nsx }}',
vcenter = '{{ vcenter }}',
uid = '{{ uid }}',
type = '{{ type }}'
WHERE 
locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>private_clouds</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmwareengine.private_clouds
WHERE locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}';
```
