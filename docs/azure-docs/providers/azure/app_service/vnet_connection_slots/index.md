---
title: vnet_connection_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - vnet_connection_slots
  - app_service
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

Creates, updates, deletes, gets or lists a <code>vnet_connection_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vnet_connection_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.vnet_connection_slots" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vnet_connection_slots', value: 'view', },
        { label: 'vnet_connection_slots', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="cert_blob" /> | `text` | field from the `properties` object |
| <CopyableCode code="cert_thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_servers" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_swift" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of resource. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resync_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="routes" /> | `text` | field from the `properties` object |
| <CopyableCode code="slot" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="vnetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Virtual Network information contract. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Gets a virtual network the app (or deployment slot) is connected to by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the virtual networks the app (or deployment slot) is connected to. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Deletes a connection from an app (or deployment slot to a named virtual network. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). |

## `SELECT` examples

Description for Gets the virtual networks the app (or deployment slot) is connected to.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vnet_connection_slots', value: 'view', },
        { label: 'vnet_connection_slots', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cert_blob,
cert_thumbprint,
dns_servers,
is_swift,
kind,
resourceGroupName,
resync_required,
routes,
slot,
subscriptionId,
type,
vnetName,
vnet_resource_id
FROM azure.app_service.vw_vnet_connection_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.vnet_connection_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vnet_connection_slots</code> resource.

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
INSERT INTO azure.app_service.vnet_connection_slots (
name,
resourceGroupName,
slot,
subscriptionId,
vnetName,
kind,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ slot }}',
'{{ subscriptionId }}',
'{{ vnetName }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: vnetResourceId
          value: string
        - name: certThumbprint
          value: string
        - name: certBlob
          value: string
        - name: routes
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: kind
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: startAddress
                    value: string
                  - name: endAddress
                    value: string
                  - name: routeType
                    value: string
        - name: resyncRequired
          value: boolean
        - name: dnsServers
          value: string
        - name: isSwift
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>vnet_connection_slots</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.vnet_connection_slots
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vnetName = '{{ vnetName }}';
```

## `DELETE` example

Deletes the specified <code>vnet_connection_slots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.vnet_connection_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vnetName = '{{ vnetName }}';
```
