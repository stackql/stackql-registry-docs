---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - storage
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

Creates, updates, deletes, gets or lists a <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | Gets the Kind. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the storage account. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the storage accounts available under the subscription. Note that storage keys are not returned; use the ListKeys operation for this. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the storage accounts available under the given resource group. Note that storage keys are not returned; use the ListKeys operation for this. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__kind, data__location, data__sku" /> | Asynchronously creates a new storage account with the specified parameters. If an account is already created and a subsequent create request is issued with different properties, the account properties will be updated. If an account is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Deletes a storage account in Microsoft Azure. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | The update operation can be used to update the SKU, encryption, access tier, or tags for a storage account. It can also be used to map the account to a custom domain. Only one custom domain is supported per storage account; the replacement/change of custom domain is not supported. In order to replace an old custom domain, the old value must be cleared/unregistered before a new value can be set. The update of multiple properties is supported. This call does not change the storage keys for the account. If you want to change the storage account keys, use the regenerate keys operation. The location and name of the storage account cannot be changed after creation. |
| <CopyableCode code="abort_hierarchical_namespace_migration" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Abort live Migration of storage account to enable Hns |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks that the storage account name is valid and is not already in use. |
| <CopyableCode code="customer_initiated_migration" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__properties" /> | Account Migration request can be triggered for a storage account to change its redundancy level. The migration updates the non-zonal redundant storage account to a zonal redundant account or vice-versa in order to have better reliability and availability. Zone-redundant storage (ZRS) replicates your storage account synchronously across three Azure availability zones in the primary region. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | A failover request can be triggered for a storage account in the event a primary endpoint becomes unavailable for any reason. The failover occurs from the storage account's primary cluster to the secondary cluster for RA-GRS accounts. The secondary cluster will become primary after failover and the account is converted to LRS. In the case of a Planned Failover, the primary and secondary clusters are swapped after failover and the account remains geo-replicated. Failover should continue to be used in the event of availability issues as Planned failover is only available while the primary and secondary endpoints are available. The primary use case of a Planned Failover is disaster recovery testing drills. This type of failover is invoked by setting FailoverType parameter to 'Planned'. Learn more about the failover options here- https://learn.microsoft.com/en-us/azure/storage/common/storage-disaster-recovery-guidance |
| <CopyableCode code="hierarchical_namespace_migration" /> | `EXEC` | <CopyableCode code="accountName, requestType, resourceGroupName, subscriptionId" /> | Live Migration of storage account to enable Hns |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__keyName" /> | Regenerates one of the access keys or Kerberos keys for the specified storage account. |
| <CopyableCode code="restore_blob_ranges" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__blobRanges, data__timeToRestore" /> | Restore blobs in the specified blob ranges |
| <CopyableCode code="revoke_user_delegation_keys" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Revoke user delegation keys. |

## `SELECT` examples

Lists all the storage accounts available under the subscription. Note that storage keys are not returned; use the ListKeys operation for this.


```sql
SELECT
extendedLocation,
identity,
kind,
location,
properties,
sku,
tags
FROM azure.storage.accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>accounts</code> resource.

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
INSERT INTO azure.storage.accounts (
accountName,
resourceGroupName,
subscriptionId,
data__kind,
data__location,
data__sku,
sku,
kind,
location,
extendedLocation,
tags,
identity,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ data__location }}',
'{{ data__sku }}',
'{{ sku }}',
'{{ kind }}',
'{{ location }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ identity }}',
'{{ properties }}'
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
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: kind
      value: string
    - name: location
      value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: tags
      value: object
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: allowedCopyScope
          value: string
        - name: publicNetworkAccess
          value: []
        - name: sasPolicy
          value:
            - name: sasExpirationPeriod
              value: string
            - name: expirationAction
              value: string
        - name: keyPolicy
          value:
            - name: keyExpirationPeriodInDays
              value: integer
        - name: customDomain
          value:
            - name: name
              value: string
            - name: useSubDomainName
              value: boolean
        - name: encryption
          value:
            - name: services
              value:
                - name: blob
                  value:
                    - name: enabled
                      value: boolean
                    - name: lastEnabledTime
                      value: string
                    - name: keyType
                      value: string
            - name: keySource
              value: string
            - name: requireInfrastructureEncryption
              value: boolean
            - name: keyvaultproperties
              value:
                - name: keyIdentifier
                  value: string
                - name: identity
                  value: string
            - name: identity
              value:
                - name: userAssignedIdentity
                  value: string
                - name: federatedIdentityClientId
                  value: string
        - name: networkAcls
          value:
            - name: bypass
              value: string
            - name: resourceAccessRules
              value:
                - - name: tenantId
                    value: string
                  - name: resourceId
                    value: string
            - name: virtualNetworkRules
              value:
                - - name: id
                    value: string
                  - name: action
                    value: string
                  - name: state
                    value: string
            - name: ipRules
              value:
                - - name: value
                    value: string
                  - name: action
                    value: string
            - name: defaultAction
              value: string
        - name: accessTier
          value: string
        - name: azureFilesIdentityBasedAuthentication
          value:
            - name: directoryServiceOptions
              value: string
            - name: activeDirectoryProperties
              value:
                - name: domainName
                  value: string
                - name: netBiosDomainName
                  value: string
                - name: forestName
                  value: string
                - name: domainGuid
                  value: string
                - name: domainSid
                  value: string
                - name: azureStorageSid
                  value: string
                - name: samAccountName
                  value: string
                - name: accountType
                  value: string
            - name: defaultSharePermission
              value: string
        - name: supportsHttpsTrafficOnly
          value: boolean
        - name: isSftpEnabled
          value: boolean
        - name: isLocalUserEnabled
          value: boolean
        - name: enableExtendedGroups
          value: boolean
        - name: isHnsEnabled
          value: boolean
        - name: largeFileSharesState
          value: string
        - name: routingPreference
          value:
            - name: routingChoice
              value: string
            - name: publishMicrosoftEndpoints
              value: boolean
            - name: publishInternetEndpoints
              value: boolean
        - name: allowBlobPublicAccess
          value: boolean
        - name: minimumTlsVersion
          value: string
        - name: allowSharedKeyAccess
          value: boolean
        - name: isNfsV3Enabled
          value: boolean
        - name: allowCrossTenantReplication
          value: boolean
        - name: defaultToOAuthAuthentication
          value: boolean
        - name: immutableStorageWithVersioning
          value:
            - name: enabled
              value: boolean
            - name: immutabilityPolicy
              value:
                - name: immutabilityPeriodSinceCreationInDays
                  value: integer
                - name: state
                  value: string
                - name: allowProtectedAppendWrites
                  value: boolean
        - name: dnsEndpointType
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>accounts</code> resource.

```sql
/*+ update */
UPDATE azure.storage.accounts
SET 
sku = '{{ sku }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage.accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
