---
title: volume_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_groups
  - netapp
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

Creates, updates, deletes, gets or lists a <code>volume_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.volume_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volume_groups', value: 'view', },
        { label: 'volume_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_meta_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="volumeGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumes" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Volume group properties |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, volumeGroupName" /> | Get details of the specified volume group |
| <CopyableCode code="list_by_netapp_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List all volume groups for given account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, volumeGroupName" /> | Create a volume group along with specified volumes |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, volumeGroupName" /> | Delete the specified volume group only if there are no volumes under volume group. |

## `SELECT` examples

List all volume groups for given account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volume_groups', value: 'view', },
        { label: 'volume_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
group_meta_data,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
type,
volumeGroupName,
volumes
FROM azure_isv.netapp.vw_volume_groups
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure_isv.netapp.volume_groups
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volume_groups</code> resource.

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
INSERT INTO azure_isv.netapp.volume_groups (
accountName,
resourceGroupName,
subscriptionId,
volumeGroupName,
location,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ volumeGroupName }}',
'{{ location }}',
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: groupMetaData
          value:
            - name: groupDescription
              value: string
            - name: applicationType
              value: string
            - name: applicationIdentifier
              value: string
            - name: globalPlacementRules
              value:
                - - name: key
                    value: string
                  - name: value
                    value: string
            - name: volumesCount
              value: integer
        - name: volumes
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: tags
                value: []
              - name: zones
                value:
                  - string
              - name: properties
                value:
                  - name: fileSystemId
                    value: string
                  - name: creationToken
                    value: string
                  - name: serviceLevel
                    value: []
                  - name: usageThreshold
                    value: integer
                  - name: exportPolicy
                    value: string
                  - name: protocolTypes
                    value:
                      - string
                  - name: provisioningState
                    value: string
                  - name: snapshotId
                    value: string
                  - name: deleteBaseSnapshot
                    value: boolean
                  - name: backupId
                    value: string
                  - name: baremetalTenantId
                    value: string
                  - name: subnetId
                    value: string
                  - name: networkFeatures
                    value: []
                  - name: networkSiblingSetId
                    value: string
                  - name: storageToNetworkProximity
                    value: string
                  - name: mountTargets
                    value:
                      - - name: mountTargetId
                          value: string
                        - name: fileSystemId
                          value: string
                        - name: ipAddress
                          value: string
                        - name: smbServerFqdn
                          value: string
                  - name: volumeType
                    value: string
                  - name: dataProtection
                    value: string
                  - name: isRestoring
                    value: boolean
                  - name: snapshotDirectoryVisible
                    value: boolean
                  - name: kerberosEnabled
                    value: boolean
                  - name: securityStyle
                    value: string
                  - name: smbEncryption
                    value: boolean
                  - name: smbAccessBasedEnumeration
                    value: []
                  - name: smbNonBrowsable
                    value: []
                  - name: smbContinuouslyAvailable
                    value: boolean
                  - name: throughputMibps
                    value: number
                  - name: actualThroughputMibps
                    value: number
                  - name: encryptionKeySource
                    value: string
                  - name: keyVaultPrivateEndpointResourceId
                    value: string
                  - name: ldapEnabled
                    value: boolean
                  - name: coolAccess
                    value: boolean
                  - name: coolnessPeriod
                    value: integer
                  - name: coolAccessRetrievalPolicy
                    value: []
                  - name: unixPermissions
                    value: string
                  - name: cloneProgress
                    value: integer
                  - name: fileAccessLogs
                    value: string
                  - name: avsDataStore
                    value: string
                  - name: dataStoreResourceId
                    value:
                      - string
                  - name: isDefaultQuotaEnabled
                    value: boolean
                  - name: defaultUserQuotaInKiBs
                    value: integer
                  - name: defaultGroupQuotaInKiBs
                    value: integer
                  - name: maximumNumberOfFiles
                    value: integer
                  - name: volumeGroupName
                    value: string
                  - name: capacityPoolResourceId
                    value: string
                  - name: proximityPlacementGroup
                    value: string
                  - name: t2Network
                    value: string
                  - name: volumeSpecName
                    value: string
                  - name: encrypted
                    value: boolean
                  - name: placementRules
                    value:
                      - - name: key
                          value: string
                        - name: value
                          value: string
                  - name: enableSubvolumes
                    value: string
                  - name: provisionedAvailabilityZone
                    value: string
                  - name: isLargeVolume
                    value: boolean
                  - name: originatingResourceId
                    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>volume_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.volume_groups
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeGroupName = '{{ volumeGroupName }}';
```
