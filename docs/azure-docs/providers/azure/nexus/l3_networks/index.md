---
title: l3_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - l3_networks
  - nexus
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

Creates, updates, deletes, gets or lists a <code>l3_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>l3_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.l3_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_l3_networks', value: 'view', },
        { label: 'l3_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associated_resource_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybrid_aks_clusters_associated_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybrid_aks_ipam_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybrid_aks_plugin_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="interface_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_allocation_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv4_connected_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv6_connected_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="l3NetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="l3_isolation_domain_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="virtual_machines_associated_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="vlan" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="l3NetworkName, resourceGroupName, subscriptionId" /> | Get properties of the provided layer 3 (L3) network. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of layer 3 (L3) networks in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of layer 3 (L3) networks in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="l3NetworkName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new layer 3 (L3) network or update the properties of the existing network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="l3NetworkName, resourceGroupName, subscriptionId" /> | Delete the provided layer 3 (L3) network. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="l3NetworkName, resourceGroupName, subscriptionId" /> | Update tags associated with the provided layer 3 (L3) network. |

## `SELECT` examples

Get a list of layer 3 (L3) networks in the provided subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_l3_networks', value: 'view', },
        { label: 'l3_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
associated_resource_ids,
cluster_id,
detailed_status,
detailed_status_message,
extended_location,
hybrid_aks_clusters_associated_ids,
hybrid_aks_ipam_enabled,
hybrid_aks_plugin_type,
interface_name,
ip_allocation_type,
ipv4_connected_prefix,
ipv6_connected_prefix,
l3NetworkName,
l3_isolation_domain_id,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
virtual_machines_associated_ids,
vlan
FROM azure.nexus.vw_l3_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.nexus.l3_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>l3_networks</code> resource.

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
INSERT INTO azure.nexus.l3_networks (
l3NetworkName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
data__properties,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ l3NetworkName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ data__properties }}',
'{{ extendedLocation }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: associatedResourceIds
          value:
            - string
        - name: clusterId
          value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: hybridAksClustersAssociatedIds
          value:
            - string
        - name: hybridAksIpamEnabled
          value: string
        - name: hybridAksPluginType
          value: string
        - name: interfaceName
          value: string
        - name: ipAllocationType
          value: string
        - name: ipv4ConnectedPrefix
          value: string
        - name: ipv6ConnectedPrefix
          value: string
        - name: l3IsolationDomainId
          value: string
        - name: provisioningState
          value: string
        - name: virtualMachinesAssociatedIds
          value:
            - string
        - name: vlan
          value: integer
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>l3_networks</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.l3_networks
SET 
tags = '{{ tags }}'
WHERE 
l3NetworkName = '{{ l3NetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>l3_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.l3_networks
WHERE l3NetworkName = '{{ l3NetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
