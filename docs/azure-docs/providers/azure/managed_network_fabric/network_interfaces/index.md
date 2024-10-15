---
title: network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interfaces
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>network_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_interfaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_interfaces', value: 'view', },
        { label: 'network_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="connected_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="interface_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv4_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv6_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkDeviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkInterfaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="physical_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Network Interface Properties defines the properties of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkDeviceName, networkInterfaceName, resourceGroupName, subscriptionId" /> | Get the Network Interface resource details. |
| <CopyableCode code="list_by_network_device" /> | `SELECT` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | List all the Network Interface resources in a given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkDeviceName, networkInterfaceName, resourceGroupName, subscriptionId, data__properties" /> | Create a Network Interface resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkDeviceName, networkInterfaceName, resourceGroupName, subscriptionId" /> | Delete the Network Interface resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkDeviceName, networkInterfaceName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network Interface resource. |

## `SELECT` examples

List all the Network Interface resources in a given resource group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_interfaces', value: 'view', },
        { label: 'network_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
annotation,
connected_to,
interface_type,
ipv4_address,
ipv6_address,
networkDeviceName,
networkInterfaceName,
physical_identifier,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.managed_network_fabric.vw_network_interfaces
WHERE networkDeviceName = '{{ networkDeviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.managed_network_fabric.network_interfaces
WHERE networkDeviceName = '{{ networkDeviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_interfaces</code> resource.

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
INSERT INTO azure.managed_network_fabric.network_interfaces (
networkDeviceName,
networkInterfaceName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ networkDeviceName }}',
'{{ networkInterfaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: annotation
          value: string
        - name: physicalIdentifier
          value: string
        - name: connectedTo
          value: string
        - name: interfaceType
          value: string
        - name: ipv4Address
          value: string
        - name: ipv6Address
          value: string
        - name: provisioningState
          value: []
        - name: administrativeState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_interfaces</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.network_interfaces
SET 
properties = '{{ properties }}'
WHERE 
networkDeviceName = '{{ networkDeviceName }}'
AND networkInterfaceName = '{{ networkInterfaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_interfaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.network_interfaces
WHERE networkDeviceName = '{{ networkDeviceName }}'
AND networkInterfaceName = '{{ networkInterfaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
