---
title: orders
hide_title: false
hide_table_of_contents: false
keywords:
  - orders
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>orders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.orders" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="kind" /> | `string` | It specify the order api version. |
| <CopyableCode code="properties" /> | `object` | Order properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_data_box_edge_device" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
kind,
properties,
systemData,
type
FROM azure.data_box_edge.orders
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>orders</code> resource.

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
INSERT INTO azure.data_box_edge.orders (
deviceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ deviceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
    - name: type
      value: string
    - name: kind
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: orderId
          value: string
        - name: contactInformation
          value:
            - name: contactPerson
              value: string
            - name: companyName
              value: string
            - name: phone
              value: string
            - name: emailList
              value:
                - string
        - name: shippingAddress
          value:
            - name: addressLine1
              value: string
            - name: addressLine2
              value: string
            - name: addressLine3
              value: string
            - name: postalCode
              value: string
            - name: city
              value: string
            - name: state
              value: string
            - name: country
              value: string
        - name: currentStatus
          value:
            - name: status
              value: string
            - name: updateDateTime
              value: string
            - name: comments
              value: string
            - name: trackingInformation
              value:
                - name: serialNumber
                  value: string
                - name: carrierName
                  value: string
                - name: trackingId
                  value: string
                - name: trackingUrl
                  value: string
            - name: additionalOrderDetails
              value: object
        - name: orderHistory
          value:
            - - name: status
                value: string
              - name: updateDateTime
                value: string
              - name: comments
                value: string
              - name: additionalOrderDetails
                value: object
        - name: serialNumber
          value: string
        - name: deliveryTrackingInfo
          value:
            - - name: serialNumber
                value: string
              - name: carrierName
                value: string
              - name: trackingId
                value: string
              - name: trackingUrl
                value: string
        - name: returnTrackingInfo
          value:
            - - name: serialNumber
                value: string
              - name: carrierName
                value: string
              - name: trackingId
                value: string
              - name: trackingUrl
                value: string
        - name: shipmentType
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>orders</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_box_edge.orders
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
