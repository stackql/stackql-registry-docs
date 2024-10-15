---
title: peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - peerings
  - peering
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

Creates, updates, deletes, gets or lists a <code>peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.peerings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_peerings', value: 'view', },
        { label: 'peerings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="direct" /> | `text` | field from the `properties` object |
| <CopyableCode code="exchange" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind of the peering. |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="peeringName" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The SKU that defines the tier and kind of the peering. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="kind" /> | `string` | The kind of the peering. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define connectivity to the Microsoft Cloud Edge. |
| <CopyableCode code="sku" /> | `object` | The SKU that defines the tier and kind of the peering. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Gets an existing peering with the specified name under the given subscription and resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the peerings under the given subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the peerings under the given subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, data__kind, data__location, data__sku" /> | Creates a new peering or updates an existing peering with the specified name under the given subscription and resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Deletes an existing peering with the specified name under the given subscription and resource group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Updates tags for a peering with the specified name under the given subscription and resource group. |

## `SELECT` examples

Lists all of the peerings under the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_peerings', value: 'view', },
        { label: 'peerings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
direct,
exchange,
kind,
location,
peeringName,
peering_location,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
type
FROM azure.peering.vw_peerings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
location,
properties,
sku,
tags,
type
FROM azure.peering.peerings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>peerings</code> resource.

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
INSERT INTO azure.peering.peerings (
peeringName,
resourceGroupName,
subscriptionId,
data__kind,
data__location,
data__sku,
sku,
kind,
properties,
location,
tags
)
SELECT 
'{{ peeringName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ data__location }}',
'{{ data__sku }}',
'{{ sku }}',
'{{ kind }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: family
          value: string
        - name: size
          value: string
    - name: kind
      value: string
    - name: properties
      value:
        - name: direct
          value:
            - name: connections
              value:
                - - name: bandwidthInMbps
                    value: integer
                  - name: provisionedBandwidthInMbps
                    value: integer
                  - name: sessionAddressProvider
                    value: string
                  - name: useForPeeringService
                    value: boolean
                  - name: microsoftTrackingId
                    value: string
                  - name: peeringDBFacilityId
                    value: integer
                  - name: connectionState
                    value: string
                  - name: bgpSession
                    value:
                      - name: sessionPrefixV4
                        value: string
                      - name: sessionPrefixV6
                        value: string
                      - name: microsoftSessionIPv4Address
                        value: string
                      - name: microsoftSessionIPv6Address
                        value: string
                      - name: peerSessionIPv4Address
                        value: string
                      - name: peerSessionIPv6Address
                        value: string
                      - name: sessionStateV4
                        value: string
                      - name: sessionStateV6
                        value: string
                      - name: maxPrefixesAdvertisedV4
                        value: integer
                      - name: maxPrefixesAdvertisedV6
                        value: integer
                      - name: md5AuthenticationKey
                        value: string
                  - name: connectionIdentifier
                    value: string
                  - name: errorMessage
                    value: string
            - name: useForPeeringService
              value: boolean
            - name: peerAsn
              value:
                - name: id
                  value: string
            - name: directPeeringType
              value: string
        - name: exchange
          value:
            - name: connections
              value:
                - - name: peeringDBFacilityId
                    value: integer
                  - name: connectionState
                    value: string
                  - name: connectionIdentifier
                    value: string
                  - name: errorMessage
                    value: string
        - name: peeringLocation
          value: string
        - name: provisioningState
          value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>peerings</code> resource.

```sql
/*+ update */
UPDATE azure.peering.peerings
SET 
tags = '{{ tags }}'
WHERE 
peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>peerings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.peering.peerings
WHERE peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
