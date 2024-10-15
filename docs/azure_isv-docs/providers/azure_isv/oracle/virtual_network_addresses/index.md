---
title: virtual_network_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_addresses
  - oracle
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

Creates, updates, deletes, gets or lists a <code>virtual_network_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.virtual_network_addresses" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_addresses', value: 'view', },
        { label: 'virtual_network_addresses', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cloudvmclustername" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_assigned" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualnetworkaddressname" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_ocid" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | virtualNetworkAddress resource properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, virtualnetworkaddressname" /> | Get a VirtualNetworkAddress |
| <CopyableCode code="list_by_cloud_vm_cluster" /> | `SELECT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | List VirtualNetworkAddress resources by CloudVmCluster |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, virtualnetworkaddressname" /> | Create a VirtualNetworkAddress |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, virtualnetworkaddressname" /> | Delete a VirtualNetworkAddress |

## `SELECT` examples

List VirtualNetworkAddress resources by CloudVmCluster

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_addresses', value: 'view', },
        { label: 'virtual_network_addresses', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cloudvmclustername,
domain,
ip_address,
lifecycle_details,
lifecycle_state,
ocid,
provisioning_state,
resourceGroupName,
subscriptionId,
time_assigned,
virtualnetworkaddressname,
vm_ocid
FROM azure_isv.oracle.vw_virtual_network_addresses
WHERE cloudvmclustername = '{{ cloudvmclustername }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.oracle.virtual_network_addresses
WHERE cloudvmclustername = '{{ cloudvmclustername }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_network_addresses</code> resource.

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
INSERT INTO azure_isv.oracle.virtual_network_addresses (
cloudvmclustername,
resourceGroupName,
subscriptionId,
virtualnetworkaddressname,
properties
)
SELECT 
'{{ cloudvmclustername }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualnetworkaddressname }}',
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
        - name: ipAddress
          value: string
        - name: vmOcid
          value: []
        - name: domain
          value: string
        - name: lifecycleDetails
          value: string
        - name: provisioningState
          value: []
        - name: lifecycleState
          value: []
        - name: timeAssigned
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_network_addresses</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.oracle.virtual_network_addresses
WHERE cloudvmclustername = '{{ cloudvmclustername }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualnetworkaddressname = '{{ virtualnetworkaddressname }}';
```
