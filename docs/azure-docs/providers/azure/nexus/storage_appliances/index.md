---
title: storage_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_appliances
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

Creates, updates, deletes, gets or lists a <code>storage_appliances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.storage_appliances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_appliances', value: 'view', },
        { label: 'storage_appliances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrator_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_used" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="management_ipv4_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="manufacturer" /> | `text` | field from the `properties` object |
| <CopyableCode code="model" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="rack_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="rack_slot" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_vendor_management_feature" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_vendor_management_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_rotation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageApplianceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_appliance_sku_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId" /> | Get properties of the provided storage appliance. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of storage appliances in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of storage appliances in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new storage appliance or update the properties of the existing one.
All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId" /> | Delete the provided storage appliance.
All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId" /> | Update properties of the provided storage appliance, or update tags associated with the storage appliance Properties and tag updates can be done independently. |
| <CopyableCode code="disable_remote_vendor_management" /> | `EXEC` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId" /> | Disable remote vendor management of the provided storage appliance. |
| <CopyableCode code="enable_remote_vendor_management" /> | `EXEC` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId" /> | Enable remote vendor management of the provided storage appliance. |

## `SELECT` examples

Get a list of storage appliances in the provided subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_appliances', value: 'view', },
        { label: 'storage_appliances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrator_credentials,
capacity,
capacity_used,
cluster_id,
detailed_status,
detailed_status_message,
extended_location,
location,
management_ipv4_address,
manufacturer,
model,
provisioning_state,
rack_id,
rack_slot,
remote_vendor_management_feature,
remote_vendor_management_status,
resourceGroupName,
secret_rotation_status,
serial_number,
storageApplianceName,
storage_appliance_sku_id,
subscriptionId,
tags,
version
FROM azure.nexus.vw_storage_appliances
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
FROM azure.nexus.storage_appliances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_appliances</code> resource.

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
INSERT INTO azure.nexus.storage_appliances (
resourceGroupName,
storageApplianceName,
subscriptionId,
data__extendedLocation,
data__properties,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ storageApplianceName }}',
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
        - name: administratorCredentials
          value:
            - name: password
              value: string
            - name: username
              value: string
        - name: capacity
          value: integer
        - name: capacityUsed
          value: integer
        - name: clusterId
          value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: managementIpv4Address
          value: string
        - name: manufacturer
          value: string
        - name: model
          value: string
        - name: provisioningState
          value: string
        - name: rackId
          value: string
        - name: rackSlot
          value: integer
        - name: remoteVendorManagementFeature
          value: string
        - name: remoteVendorManagementStatus
          value: string
        - name: secretRotationStatus
          value:
            - - name: expirePeriodDays
                value: integer
              - name: lastRotationTime
                value: string
              - name: rotationPeriodDays
                value: integer
              - name: secretArchiveReference
                value:
                  - name: keyVaultId
                    value: string
                  - name: secretName
                    value: string
                  - name: secretVersion
                    value: string
              - name: secretType
                value: string
        - name: serialNumber
          value: string
        - name: storageApplianceSkuId
          value: string
        - name: version
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>storage_appliances</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.storage_appliances
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND storageApplianceName = '{{ storageApplianceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>storage_appliances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.storage_appliances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageApplianceName = '{{ storageApplianceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
