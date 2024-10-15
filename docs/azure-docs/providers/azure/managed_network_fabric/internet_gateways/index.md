---
title: internet_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateways
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

Creates, updates, deletes, gets or lists a <code>internet_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>internet_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.internet_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_internet_gateways', value: 'view', },
        { label: 'internet_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="internetGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="internet_gateway_rule_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv4_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="network_fabric_controller_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Internet Gateway Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="internetGatewayName, resourceGroupName, subscriptionId" /> | Implements Gateway GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays Internet Gateways list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays Internet Gateways list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="internetGatewayName, resourceGroupName, subscriptionId, data__properties" /> | Creates a Network Fabric Service Internet Gateway resource instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="internetGatewayName, resourceGroupName, subscriptionId" /> | Execute a delete on Network Fabric Service Internet Gateway. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="internetGatewayName, resourceGroupName, subscriptionId" /> | Execute patch on Network Fabric Service Internet Gateway. |

## `SELECT` examples

Displays Internet Gateways list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_internet_gateways', value: 'view', },
        { label: 'internet_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
annotation,
internetGatewayName,
internet_gateway_rule_id,
ipv4_address,
location,
network_fabric_controller_id,
port,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.managed_network_fabric.vw_internet_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.internet_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>internet_gateways</code> resource.

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
INSERT INTO azure.managed_network_fabric.internet_gateways (
internetGatewayName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ internetGatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: properties
      value:
        - name: annotation
          value: string
        - name: internetGatewayRuleId
          value: []
        - name: ipv4Address
          value: string
        - name: port
          value: integer
        - name: type
          value: string
        - name: networkFabricControllerId
          value: []
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>internet_gateways</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.internet_gateways
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
internetGatewayName = '{{ internetGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>internet_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.internet_gateways
WHERE internetGatewayName = '{{ internetGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
