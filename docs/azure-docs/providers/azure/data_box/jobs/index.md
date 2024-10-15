---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - data_box
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box.jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the object. |
| <CopyableCode code="name" /> | `text` | Name of the object. |
| <CopyableCode code="all_devices_lost" /> | `text` | field from the `properties` object |
| <CopyableCode code="cancellation_reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="delayed_stage" /> | `text` | field from the `properties` object |
| <CopyableCode code="delivery_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="delivery_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Msi identity details of the resource |
| <CopyableCode code="is_cancellable" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_cancellable_without_fee" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deletable" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_prepare_to_ship_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_shipping_address_editable" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="reverse_shipping_details_update" /> | `text` | field from the `properties` object |
| <CopyableCode code="reverse_transport_preference_update" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The Sku. |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). |
| <CopyableCode code="transfer_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="identity" /> | `object` | Msi identity details of the resource |
| <CopyableCode code="location" /> | `string` | The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. |
| <CopyableCode code="properties" /> | `object` | Job Properties |
| <CopyableCode code="sku" /> | `object` | The Sku. |
| <CopyableCode code="systemData" /> | `object` | Provides details about resource creation and update time |
| <CopyableCode code="tags" /> | `object` | The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). |
| <CopyableCode code="type" /> | `string` | Type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Gets information about the specified job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the jobs available under the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the jobs available under the given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, data__properties" /> | Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Deletes a job. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing job. |
| <CopyableCode code="book_shipment_pick_up" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, data__endTime, data__shipmentLocation, data__startTime" /> | Book shipment pick up. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, data__reason" /> | CancelJob. |
| <CopyableCode code="mark_devices_shipped" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, data__deliverToDcPackageDetails" /> | Request to mark devices for a given job as shipped |

## `SELECT` examples

Lists all the jobs available under the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
all_devices_lost,
cancellation_reason,
delayed_stage,
delivery_info,
delivery_type,
details,
error,
identity,
is_cancellable,
is_cancellable_without_fee,
is_deletable,
is_prepare_to_ship_enabled,
is_shipping_address_editable,
jobName,
location,
resourceGroupName,
reverse_shipping_details_update,
reverse_transport_preference_update,
sku,
start_time,
status,
subscriptionId,
system_data,
tags,
transfer_type,
type
FROM azure.data_box.vw_jobs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.data_box.jobs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jobs</code> resource.

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
INSERT INTO azure.data_box.jobs (
jobName,
resourceGroupName,
subscriptionId,
data__properties,
location,
tags,
sku,
identity,
properties
)
SELECT 
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: string
        - name: displayName
          value: string
        - name: family
          value: string
        - name: model
          value: []
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: object
    - name: properties
      value:
        - name: transferType
          value: string
        - name: isCancellable
          value: boolean
        - name: isDeletable
          value: boolean
        - name: isShippingAddressEditable
          value: boolean
        - name: reverseShippingDetailsUpdate
          value: string
        - name: reverseTransportPreferenceUpdate
          value: string
        - name: isPrepareToShipEnabled
          value: boolean
        - name: status
          value: string
        - name: delayedStage
          value: string
        - name: startTime
          value: string
        - name: error
          value:
            - name: additionalInfo
              value:
                - - name: info
                    value: object
                  - name: type
                    value: string
            - name: code
              value: string
            - name: details
              value:
                - - name: additionalInfo
                    value:
                      - - name: info
                          value: object
                        - name: type
                          value: string
                  - name: code
                    value: string
                  - name: details
                    value:
                      - - name: additionalInfo
                          value:
                            - - name: info
                                value: object
                              - name: type
                                value: string
                        - name: code
                          value: string
                        - name: details
                          value:
                            - - name: additionalInfo
                                value:
                                  - - name: info
                                      value: object
                                    - name: type
                                      value: string
                              - name: code
                                value: string
                              - name: details
                                value:
                                  - - name: additionalInfo
                                      value:
                                        - - name: info
                                            value: object
                                          - name: type
                                            value: string
                                    - name: code
                                      value: string
                                    - name: details
                                      value:
                                        - - name: additionalInfo
                                            value:
                                              - - name: info
                                                  value: object
                                                - name: type
                                                  value: string
                                          - name: code
                                            value: string
                                          - name: details
                                            value:
                                              - - name: additionalInfo
                                                  value:
                                                    - - name: info
                                                        value: object
                                                      - name: type
                                                        value: string
                                                - name: code
                                                  value: string
                                                - name: details
                                                  value:
                                                    - - name: additionalInfo
                                                        value:
                                                          - - name: info
                                                              value: object
                                                            - name: type
                                                              value: string
                                                      - name: code
                                                        value: string
                                                      - name: details
                                                        value:
                                                          - - name: additionalInfo
                                                              value:
                                                                - []
                                                            - name: code
                                                              value: string
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: message
                                                              value: string
                                                            - name: target
                                                              value: string
                                                      - name: message
                                                        value: string
                                                      - name: target
                                                        value: string
                                                - name: message
                                                  value: string
                                                - name: target
                                                  value: string
                                          - name: message
                                            value: string
                                          - name: target
                                            value: string
                                    - name: message
                                      value: string
                                    - name: target
                                      value: string
                              - name: message
                                value: string
                              - name: target
                                value: string
                        - name: message
                          value: string
                        - name: target
                          value: string
                  - name: message
                    value: string
                  - name: target
                    value: string
            - name: message
              value: string
            - name: target
              value: string
        - name: details
          value:
            - name: jobStages
              value:
                - - name: stageName
                    value: string
                  - name: displayName
                    value: string
                  - name: stageStatus
                    value: string
                  - name: stageTime
                    value: string
                  - name: jobStageDetails
                    value: object
                  - name: delayInformation
                    value:
                      - - name: status
                          value: string
                        - name: errorCode
                          value: string
                        - name: description
                          value: string
                        - name: startTime
                          value: string
                        - name: resolutionTime
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
                - name: notificationPreference
                  value:
                    - - name: stageName
                        value: string
                      - name: sendNotification
                        value: boolean
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
                - name: skipAddressValidation
                  value: boolean
                - name: taxIdentificationNumber
                  value: string
            - name: deliveryPackage
              value:
                - name: trackingUrl
                  value: string
                - name: carrierName
                  value: string
                - name: trackingId
                  value: string
            - name: dataImportDetails
              value:
                - - name: accountDetails
                    value:
                      - name: dataAccountType
                        value: string
                      - name: sharePassword
                        value: string
                  - name: logCollectionLevel
                    value: string
            - name: dataExportDetails
              value:
                - - name: transferConfiguration
                    value:
                      - name: transferConfigurationType
                        value: string
                      - name: transferFilterDetails
                        value:
                          - name: include
                            value:
                              - name: dataAccountType
                                value: string
                              - name: blobFilterDetails
                                value:
                                  - name: blobPrefixList
                                    value:
                                      - string
                                  - name: blobPathList
                                    value:
                                      - string
                                  - name: containerList
                                    value:
                                      - string
                              - name: azureFileFilterDetails
                                value:
                                  - name: filePrefixList
                                    value:
                                      - string
                                  - name: filePathList
                                    value:
                                      - string
                                  - name: fileShareList
                                    value:
                                      - string
                              - name: filterFileDetails
                                value:
                                  - - name: filterFileType
                                      value: string
                                    - name: filterFilePath
                                      value: string
                      - name: transferAllDetails
                        value:
                          - name: include
                            value:
                              - name: dataAccountType
                                value: string
                              - name: transferAllBlobs
                                value: boolean
                              - name: transferAllFiles
                                value: boolean
                  - name: logCollectionLevel
                    value: string
            - name: jobDetailsType
              value: string
            - name: preferences
              value:
                - name: preferredDataCenterRegion
                  value:
                    - string
                - name: transportPreferences
                  value:
                    - name: preferredShipmentType
                      value: string
                    - name: isUpdated
                      value: boolean
                - name: encryptionPreferences
                  value:
                    - name: doubleEncryption
                      value: string
                    - name: hardwareEncryption
                      value: string
                - name: storageAccountAccessTierPreferences
                  value:
                    - string
            - name: reverseShippingDetails
              value:
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
                - name: isUpdated
                  value: boolean
            - name: copyLogDetails
              value:
                - - name: copyLogDetailsType
                    value: string
            - name: reverseShipmentLabelSasKey
              value: string
            - name: chainOfCustodySasKey
              value: string
            - name: deviceErasureDetails
              value:
                - name: deviceErasureStatus
                  value: string
                - name: erasureOrDestructionCertificateSasKey
                  value: string
            - name: keyEncryptionKey
              value:
                - name: kekType
                  value: string
                - name: identityProperties
                  value:
                    - name: type
                      value: string
                    - name: userAssigned
                      value:
                        - name: resourceId
                          value: string
                - name: kekUrl
                  value: string
                - name: kekVaultResourceID
                  value: string
            - name: expectedDataSizeInTeraBytes
              value: integer
            - name: actions
              value:
                - string
            - name: lastMitigationActionOnJob
              value:
                - name: actionDateTimeInUtc
                  value: string
                - name: isPerformedByCustomer
                  value: boolean
                - name: customerResolution
                  value: string
            - name: datacenterAddress
              value:
                - name: datacenterAddressType
                  value: string
                - name: supportedCarriersForReturnShipment
                  value:
                    - string
                - name: dataCenterAzureLocation
                  value: string
            - name: dataCenterCode
              value: string
        - name: cancellationReason
          value: string
        - name: deliveryType
          value: string
        - name: deliveryInfo
          value:
            - name: scheduledDateTime
              value: string
        - name: isCancellableWithoutFee
          value: boolean
        - name: allDevicesLost
          value: boolean
    - name: name
      value: string
    - name: id
      value: string
    - name: type
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>jobs</code> resource.

```sql
/*+ update */
UPDATE azure.data_box.jobs
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_box.jobs
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
