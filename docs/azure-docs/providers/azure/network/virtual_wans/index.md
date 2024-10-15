---
title: virtual_wans
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_wans
  - network
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

Creates, updates, deletes, gets or lists a <code>virtual_wans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_wans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_wans" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_wans', value: 'view', },
        { label: 'virtual_wans', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="VirtualWANName" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_branch_to_branch_traffic" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_vnet_to_vnet_traffic" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_vpn_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="office365_local_breakout_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_hubs" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_sites" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Parameters for VirtualWAN. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="VirtualWANName, resourceGroupName, subscriptionId" /> | Retrieves the details of a VirtualWAN. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the VirtualWANs in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the VirtualWANs in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="VirtualWANName, resourceGroupName, subscriptionId, data__location" /> | Creates a VirtualWAN resource if it doesn't exist else updates the existing VirtualWAN. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="VirtualWANName, resourceGroupName, subscriptionId" /> | Deletes a VirtualWAN. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="VirtualWANName, resourceGroupName, subscriptionId" /> | Updates a VirtualWAN tags. |

## `SELECT` examples

Lists all the VirtualWANs in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_wans', value: 'view', },
        { label: 'virtual_wans', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
VirtualWANName,
allow_branch_to_branch_traffic,
allow_vnet_to_vnet_traffic,
disable_vpn_encryption,
etag,
location,
office365_local_breakout_category,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type,
virtual_hubs,
vpn_sites
FROM azure.network.vw_virtual_wans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.virtual_wans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_wans</code> resource.

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
INSERT INTO azure.network.virtual_wans (
VirtualWANName,
resourceGroupName,
subscriptionId,
data__location,
properties,
id,
location,
tags
)
SELECT 
'{{ VirtualWANName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ properties }}',
'{{ id }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: disableVpnEncryption
          value: boolean
        - name: virtualHubs
          value:
            - - name: id
                value: string
        - name: vpnSites
          value:
            - - name: id
                value: string
        - name: allowBranchToBranchTraffic
          value: boolean
        - name: allowVnetToVnetTraffic
          value: boolean
        - name: office365LocalBreakoutCategory
          value: []
        - name: provisioningState
          value: []
        - name: type
          value: string
    - name: etag
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_wans</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_wans
WHERE VirtualWANName = '{{ VirtualWANName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
