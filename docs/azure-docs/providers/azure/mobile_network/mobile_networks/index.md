---
title: mobile_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - mobile_networks
  - mobile_network
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

Creates, updates, deletes, gets or lists a <code>mobile_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mobile_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.mobile_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mobile_networks', value: 'view', },
        { label: 'mobile_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `text` | Managed service identity (User assigned identity) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mobileNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_land_mobile_network_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_land_mobile_networks" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (User assigned identity) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Mobile network properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Gets information about the specified mobile network. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the mobile networks in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the mobile networks in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a mobile network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Deletes the specified mobile network. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Updates mobile network tags and managed identity. |

## `SELECT` examples

Lists all the mobile networks in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mobile_networks', value: 'view', },
        { label: 'mobile_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
identity,
location,
mobileNetworkName,
provisioning_state,
public_land_mobile_network_identifier,
public_land_mobile_networks,
resourceGroupName,
service_key,
subscriptionId,
tags
FROM azure.mobile_network.vw_mobile_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.mobile_network.mobile_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mobile_networks</code> resource.

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
INSERT INTO azure.mobile_network.mobile_networks (
mobileNetworkName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
identity,
tags,
location
)
SELECT 
'{{ mobileNetworkName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: provisioningState
          value: []
        - name: publicLandMobileNetworkIdentifier
          value:
            - name: mcc
              value: []
            - name: mnc
              value: []
        - name: publicLandMobileNetworks
          value:
            - - name: homeNetworkPublicKeys
                value:
                  - name: profileA
                    value: []
        - name: serviceKey
          value: string
    - name: identity
      value:
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>mobile_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.mobile_networks
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
