---
title: order_items
hide_title: false
hide_table_of_contents: false
keywords:
  - order_items
  - edge_order
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

Creates, updates, deletes, gets or lists a <code>order_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>order_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_order.order_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_order_items', value: 'view', },
        { label: 'order_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="address_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Msi identity details of the resource |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="orderItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="order_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="order_item_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Msi identity details of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents order item properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId" /> | Get an order item. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List order items at resource group level. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List order items at subscription level. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId, data__properties" /> | Create an order item. Existing order item cannot be updated with this api and should instead be updated with the Update order item
API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId" /> | Delete an order item. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId" /> | Update the properties of an existing order item. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId, data__reason" /> | Cancel order item. |
| <CopyableCode code="return" /> | `EXEC` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId, data__returnReason" /> | Return order item. |

## `SELECT` examples

List order items at subscription level.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_order_items', value: 'view', },
        { label: 'order_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
address_details,
identity,
location,
orderItemName,
order_id,
order_item_details,
provisioning_state,
resourceGroupName,
start_time,
subscriptionId,
tags
FROM azure_extras.edge_order.vw_order_items
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
FROM azure_extras.edge_order.order_items
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>order_items</code> resource.

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
INSERT INTO azure_extras.edge_order.order_items (
orderItemName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties,
identity
)
SELECT 
'{{ orderItemName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: orderItemDetails
          value:
            - name: productDetails
              value:
                - name: displayInfo
                  value:
                    - name: productFamilyDisplayName
                      value: string
                    - name: configurationDisplayName
                      value: string
                - name: hierarchyInformation
                  value:
                    - name: productFamilyName
                      value: string
                    - name: productLineName
                      value: string
                    - name: productName
                      value: string
                    - name: configurationName
                      value: string
                    - name: configurationIdDisplayName
                      value: string
                - name: productDoubleEncryptionStatus
                  value: string
                - name: identificationType
                  value: string
                - name: parentDeviceDetails
                  value:
                    - name: serialNumber
                      value: string
                    - name: displaySerialNumber
                      value: string
                    - name: managementResourceId
                      value: string
                    - name: managementResourceTenantId
                      value: string
                    - name: provisioningSupport
                      value: []
                    - name: provisioningDetails
                      value:
                        - name: quantity
                          value: integer
                        - name: provisioningArmId
                          value: string
                        - name: provisioningEndPoint
                          value: string
                        - name: serialNumber
                          value: string
                        - name: vendorName
                          value: string
                        - name: readyToConnectArmId
                          value: string
                        - name: managementResourceArmId
                          value: string
                        - name: uniqueDeviceIdentifier
                          value: string
                        - name: autoProvisioningStatus
                          value: []
                        - name: devicePresenceVerification
                          value:
                            - name: status
                              value: []
                            - name: message
                              value: string
                - name: optInAdditionalConfigurations
                  value:
                    - - name: quantity
                        value: integer
                      - name: provisioningDetails
                        value:
                          - - name: quantity
                              value: integer
                            - name: provisioningArmId
                              value: string
                            - name: provisioningEndPoint
                              value: string
                            - name: serialNumber
                              value: string
                            - name: vendorName
                              value: string
                            - name: readyToConnectArmId
                              value: string
                            - name: managementResourceArmId
                              value: string
                            - name: uniqueDeviceIdentifier
                              value: string
                - name: childConfigurationDeviceDetails
                  value:
                    - - name: quantity
                        value: integer
                      - name: identificationType
                        value: string
                      - name: deviceDetails
                        value:
                          - - name: serialNumber
                              value: string
                            - name: displaySerialNumber
                              value: string
                            - name: managementResourceId
                              value: string
                            - name: managementResourceTenantId
                              value: string
                      - name: termCommitmentInformation
                        value:
                          - name: termCommitmentType
                            value: []
                          - name: termCommitmentTypeDuration
                            value: string
                          - name: pendingDaysForTerm
                            value: integer
            - name: orderItemType
              value: string
            - name: orderItemMode
              value: string
            - name: siteDetails
              value:
                - name: siteId
                  value: string
            - name: currentStage
              value:
                - name: stageStatus
                  value: string
                - name: stageName
                  value: string
                - name: displayName
                  value: string
                - name: startTime
                  value: string
            - name: orderItemStageHistory
              value:
                - - name: stageStatus
                    value: string
                  - name: stageName
                    value: string
                  - name: displayName
                    value: string
                  - name: startTime
                    value: string
            - name: preferences
              value:
                - name: notificationPreferences
                  value:
                    - - name: stageName
                        value: string
                      - name: sendNotification
                        value: boolean
                - name: transportPreferences
                  value:
                    - name: preferredShipmentType
                      value: string
                - name: encryptionPreferences
                  value:
                    - name: doubleEncryptionStatus
                      value: string
                - name: managementResourcePreferences
                  value:
                    - name: preferredManagementResourceId
                      value: string
                - name: termCommitmentPreferences
                  value:
                    - name: preferredTermCommitmentDuration
                      value: string
            - name: forwardShippingDetails
              value:
                - name: carrierName
                  value: string
                - name: carrierDisplayName
                  value: string
                - name: trackingId
                  value: string
                - name: trackingUrl
                  value: string
            - name: reverseShippingDetails
              value:
                - name: sasKeyForLabel
                  value: string
                - name: carrierName
                  value: string
                - name: carrierDisplayName
                  value: string
                - name: trackingId
                  value: string
                - name: trackingUrl
                  value: string
            - name: notificationEmailList
              value:
                - string
            - name: cancellationReason
              value: string
            - name: cancellationStatus
              value: string
            - name: deletionStatus
              value: string
            - name: returnReason
              value: string
            - name: returnStatus
              value: string
            - name: managementRpDetailsList
              value:
                - - name: resourceProviderNamespace
                    value: string
            - name: error
              value:
                - name: code
                  value: string
                - name: message
                  value: string
                - name: target
                  value: string
                - name: details
                  value:
                    - - name: code
                        value: string
                      - name: message
                        value: string
                      - name: target
                        value: string
                      - name: details
                        value:
                          - - name: code
                              value: string
                            - name: message
                              value: string
                            - name: target
                              value: string
                            - name: details
                              value:
                                - - name: code
                                    value: string
                                  - name: message
                                    value: string
                                  - name: target
                                    value: string
                                  - name: details
                                    value:
                                      - - name: code
                                          value: string
                                        - name: message
                                          value: string
                                        - name: target
                                          value: string
                                        - name: details
                                          value:
                                            - - name: code
                                                value: string
                                              - name: message
                                                value: string
                                              - name: target
                                                value: string
                                              - name: details
                                                value:
                                                  - - name: code
                                                      value: string
                                                    - name: message
                                                      value: string
                                                    - name: target
                                                      value: string
                                                    - name: details
                                                      value:
                                                        - - name: code
                                                            value: string
                                                          - name: message
                                                            value: string
                                                          - name: target
                                                            value: string
                                                          - name: details
                                                            value:
                                                              - []
                                                          - name: additionalInfo
                                                            value:
                                                              - []
                                                    - name: additionalInfo
                                                      value:
                                                        - - name: type
                                                            value: string
                                                          - name: info
                                                            value: object
                                              - name: additionalInfo
                                                value:
                                                  - - name: type
                                                      value: string
                                                    - name: info
                                                      value: object
                                        - name: additionalInfo
                                          value:
                                            - - name: type
                                                value: string
                                              - name: info
                                                value: object
                                  - name: additionalInfo
                                    value:
                                      - - name: type
                                          value: string
                                        - name: info
                                          value: object
                            - name: additionalInfo
                              value:
                                - - name: type
                                    value: string
                                  - name: info
                                    value: object
                      - name: additionalInfo
                        value:
                          - - name: type
                              value: string
                            - name: info
                              value: object
                - name: additionalInfo
                  value:
                    - - name: type
                        value: string
                      - name: info
                        value: object
        - name: addressDetails
          value:
            - name: forwardAddress
              value:
                - name: addressClassification
                  value: []
                - name: shippingAddress
                  value:
                    - name: streetAddress1
                      value: string
                    - name: streetAddress2
                      value: string
                    - name: streetAddress3
                      value: string
                    - name: city
                      value: string
                    - name: stateOrProvince
                      value: string
                    - name: country
                      value: string
                    - name: postalCode
                      value: string
                    - name: zipExtendedCode
                      value: string
                    - name: companyName
                      value: string
                    - name: addressType
                      value: string
                - name: contactDetails
                  value:
                    - name: contactName
                      value: string
                    - name: phone
                      value: string
                    - name: phoneExtension
                      value: string
                    - name: mobile
                      value: string
                    - name: emailList
                      value:
                        - string
                - name: addressValidationStatus
                  value: string
                - name: provisioningState
                  value: []
        - name: startTime
          value: string
        - name: orderId
          value: string
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>order_items</code> resource.

```sql
/*+ update */
UPDATE azure_extras.edge_order.order_items
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
orderItemName = '{{ orderItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>order_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.edge_order.order_items
WHERE orderItemName = '{{ orderItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
