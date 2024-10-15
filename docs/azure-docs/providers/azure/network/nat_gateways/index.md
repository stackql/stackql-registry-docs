---
title: nat_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_gateways
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

Creates, updates, deletes, gets or lists a <code>nat_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nat_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.nat_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_nat_gateways', value: 'view', },
        { label: 'nat_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="idle_timeout_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="natGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_prefixes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU of nat gateway. |
| <CopyableCode code="subnets" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="zones" /> | `text` | A list of availability zones denoting the zone in which Nat Gateway should be deployed. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Nat Gateway properties. |
| <CopyableCode code="sku" /> | `object` | SKU of nat gateway. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting the zone in which Nat Gateway should be deployed. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="natGatewayName, resourceGroupName, subscriptionId" /> | Gets the specified nat gateway in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all nat gateways in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the Nat Gateways in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="natGatewayName, resourceGroupName, subscriptionId" /> | Creates or updates a nat gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="natGatewayName, resourceGroupName, subscriptionId" /> | Deletes the specified nat gateway. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="natGatewayName, resourceGroupName, subscriptionId" /> | Updates nat gateway tags. |

## `SELECT` examples

Gets all the Nat Gateways in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_nat_gateways', value: 'view', },
        { label: 'nat_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
idle_timeout_in_minutes,
location,
natGatewayName,
provisioning_state,
public_ip_addresses,
public_ip_prefixes,
resourceGroupName,
resource_guid,
sku,
subnets,
subscriptionId,
tags,
type,
zones
FROM azure.network.vw_nat_gateways
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
sku,
tags,
type,
zones
FROM azure.network.nat_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>nat_gateways</code> resource.

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
INSERT INTO azure.network.nat_gateways (
natGatewayName,
resourceGroupName,
subscriptionId,
sku,
properties,
zones,
id,
location,
tags
)
SELECT 
'{{ natGatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ sku }}',
'{{ properties }}',
'{{ zones }}',
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
    - name: sku
      value:
        - name: name
          value: string
    - name: properties
      value:
        - name: idleTimeoutInMinutes
          value: integer
        - name: publicIpAddresses
          value:
            - - name: id
                value: string
        - name: publicIpPrefixes
          value:
            - - name: id
                value: string
        - name: subnets
          value:
            - - name: id
                value: string
        - name: resourceGuid
          value: string
        - name: provisioningState
          value: []
    - name: zones
      value:
        - string
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

Deletes the specified <code>nat_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.nat_gateways
WHERE natGatewayName = '{{ natGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
