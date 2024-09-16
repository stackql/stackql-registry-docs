---
title: spokes
hide_title: false
hide_table_of_contents: false
keywords:
  - spokes
  - networkconnectivity
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

Creates, updates, deletes, gets or lists a <code>spokes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spokes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.spokes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of the spoke. Spoke names must be unique. They use the following form: `projects/{project_number}/locations/{region}/spokes/{spoke_id}` |
| <CopyableCode code="description" /> | `string` | An optional description of the spoke. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the spoke was created. |
| <CopyableCode code="group" /> | `string` | Optional. The name of the group that this spoke is associated with. |
| <CopyableCode code="hub" /> | `string` | Immutable. The name of the hub that this spoke is attached to. |
| <CopyableCode code="labels" /> | `object` | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| <CopyableCode code="linkedInterconnectAttachments" /> | `object` | A collection of VLAN attachment resources. These resources should be redundant attachments that all advertise the same prefixes to Google Cloud. Alternatively, in active/passive configurations, all attachments should be capable of advertising the same prefixes. |
| <CopyableCode code="linkedRouterApplianceInstances" /> | `object` | A collection of router appliance instances. If you configure multiple router appliance instances to receive data from the same set of sites outside of Google Cloud, we recommend that you associate those instances with the same spoke. |
| <CopyableCode code="linkedVpcNetwork" /> | `object` | An existing VPC network. |
| <CopyableCode code="linkedVpnTunnels" /> | `object` | A collection of Cloud VPN tunnel resources. These resources should be redundant HA VPN tunnels that all advertise the same prefixes to Google Cloud. Alternatively, in a passive/active configuration, all tunnels should be capable of advertising the same prefixes. |
| <CopyableCode code="reasons" /> | `array` | Output only. The reasons for current state of the spoke. Only present when the spoke is in the `INACTIVE` state. |
| <CopyableCode code="spokeType" /> | `string` | Output only. The type of resource associated with the spoke. |
| <CopyableCode code="state" /> | `string` | Output only. The current lifecycle state of this spoke. |
| <CopyableCode code="uniqueId" /> | `string` | Output only. The Google-generated UUID for the spoke. This value is unique across all spoke resources. If a spoke is deleted and another with the same name is created, the new spoke is assigned a different `unique_id`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the spoke was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, spokesId" /> | Gets details about a Network Connectivity Center spoke. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the Network Connectivity Center spokes in a specified project and location. |
| <CopyableCode code="list_spokes" /> | `SELECT` | <CopyableCode code="hubsId, projectsId" /> | Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Network Connectivity Center spoke. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, spokesId" /> | Deletes a Network Connectivity Center spoke. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, spokesId" /> | Updates the parameters of a Network Connectivity Center spoke. |

## `SELECT` examples

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

```sql
SELECT
name,
description,
createTime,
group,
hub,
labels,
linkedInterconnectAttachments,
linkedRouterApplianceInstances,
linkedVpcNetwork,
linkedVpnTunnels,
reasons,
spokeType,
state,
uniqueId,
updateTime
FROM google.networkconnectivity.spokes
WHERE hubsId = '{{ hubsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>spokes</code> resource.

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
INSERT INTO google.networkconnectivity.spokes (
locationsId,
projectsId,
name,
createTime,
updateTime,
labels,
description,
hub,
group,
linkedVpnTunnels,
linkedInterconnectAttachments,
linkedRouterApplianceInstances,
linkedVpcNetwork,
uniqueId,
state,
reasons,
spokeType
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ hub }}',
'{{ group }}',
'{{ linkedVpnTunnels }}',
'{{ linkedInterconnectAttachments }}',
'{{ linkedRouterApplianceInstances }}',
'{{ linkedVpcNetwork }}',
'{{ uniqueId }}',
'{{ state }}',
'{{ reasons }}',
'{{ spokeType }}'
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
    - name: labels
      value: '{{ labels }}'
    - name: description
      value: '{{ description }}'
    - name: hub
      value: '{{ hub }}'
    - name: group
      value: '{{ group }}'
    - name: linkedVpnTunnels
      value: '{{ linkedVpnTunnels }}'
    - name: linkedInterconnectAttachments
      value: '{{ linkedInterconnectAttachments }}'
    - name: linkedRouterApplianceInstances
      value: '{{ linkedRouterApplianceInstances }}'
    - name: linkedVpcNetwork
      value: '{{ linkedVpcNetwork }}'
    - name: uniqueId
      value: '{{ uniqueId }}'
    - name: state
      value: '{{ state }}'
    - name: reasons
      value: '{{ reasons }}'
    - name: spokeType
      value: '{{ spokeType }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>spokes</code> resource.

```sql
/*+ update */
UPDATE google.networkconnectivity.spokes
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
hub = '{{ hub }}',
group = '{{ group }}',
linkedVpnTunnels = '{{ linkedVpnTunnels }}',
linkedInterconnectAttachments = '{{ linkedInterconnectAttachments }}',
linkedRouterApplianceInstances = '{{ linkedRouterApplianceInstances }}',
linkedVpcNetwork = '{{ linkedVpcNetwork }}',
uniqueId = '{{ uniqueId }}',
state = '{{ state }}',
reasons = '{{ reasons }}',
spokeType = '{{ spokeType }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND spokesId = '{{ spokesId }}';
```

## `DELETE` example

Deletes the specified <code>spokes</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkconnectivity.spokes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND spokesId = '{{ spokesId }}';
```
