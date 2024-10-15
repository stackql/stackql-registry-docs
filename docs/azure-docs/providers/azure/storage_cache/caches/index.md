---
title: caches
hide_title: false
hide_table_of_contents: false
keywords:
  - caches
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>caches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>caches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.caches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A fully qualified URL. |
| <CopyableCode code="name" /> | `string` | Schema for the name of resources served by this provider. Note that objects will contain an odata @id annotation as appropriate. This will contain the complete resource id of the object. These names are case-preserving, but not case sensitive. |
| <CopyableCode code="identity" /> | `object` | Cache identity properties. |
| <CopyableCode code="location" /> | `string` | Region name string. |
| <CopyableCode code="properties" /> | `object` | Properties of the cache. |
| <CopyableCode code="sku" /> | `object` | SKU for the cache. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Type of the cache; Microsoft.StorageCache/Cache |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Returns a cache. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all caches the user has access to under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all caches the user has access to under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Create or update a cache. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Schedules a cache for deletion. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Update a cache instance. |
| <CopyableCode code="debug_info" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Tells a cache to write generate debug info for support to process. |
| <CopyableCode code="flush" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Tells a cache to write all dirty data to the Storage Target(s). During the flush, clients will see errors returned until the flush is complete. |
| <CopyableCode code="pause_priming_job" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId, data__primingJobId" /> | Schedule a priming job to be paused. |
| <CopyableCode code="resume_priming_job" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId, data__primingJobId" /> | Resumes a paused priming job. |
| <CopyableCode code="space_allocation" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Update cache space allocation. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Tells a Stopped state cache to transition to Active state. |
| <CopyableCode code="start_priming_job" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId, data__primingJobName, data__primingManifestUrl" /> | Create a priming job. This operation is only allowed when the cache is healthy. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Tells an Active cache to transition to Stopped state. |
| <CopyableCode code="stop_priming_job" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId, data__primingJobId" /> | Schedule a priming job for deletion. |
| <CopyableCode code="upgrade_firmware" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Upgrade a cache's firmware if a new version is available. Otherwise, this operation has no effect. |

## `SELECT` examples

Returns all caches the user has access to under a subscription.


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
FROM azure.storage_cache.caches
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>caches</code> resource.

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
INSERT INTO azure.storage_cache.caches (
cacheName,
resourceGroupName,
subscriptionId,
tags,
location,
identity,
properties,
sku
)
SELECT 
'{{ cacheName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
'{{ properties }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: id
      value: []
    - name: location
      value: string
    - name: name
      value: []
    - name: type
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
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
        - name: cacheSizeGB
          value: integer
        - name: health
          value:
            - name: state
              value: string
            - name: statusDescription
              value: string
            - name: conditions
              value:
                - - name: timestamp
                    value: string
                  - name: message
                    value: string
        - name: mountAddresses
          value:
            - string
        - name: provisioningState
          value: string
        - name: upgradeStatus
          value:
            - name: currentFirmwareVersion
              value: string
            - name: firmwareUpdateStatus
              value: string
            - name: firmwareUpdateDeadline
              value: string
            - name: lastFirmwareUpdate
              value: string
            - name: pendingFirmwareVersion
              value: string
        - name: upgradeSettings
          value:
            - name: upgradeScheduleEnabled
              value: boolean
            - name: scheduledTime
              value: string
        - name: networkSettings
          value:
            - name: mtu
              value: integer
            - name: utilityAddresses
              value:
                - string
            - name: dnsServers
              value:
                - string
            - name: dnsSearchDomain
              value: string
            - name: ntpServer
              value: string
        - name: encryptionSettings
          value:
            - name: keyEncryptionKey
              value:
                - name: keyUrl
                  value: string
                - name: sourceVault
                  value:
                    - name: id
                      value: string
            - name: rotationToLatestKeyVersionEnabled
              value: boolean
        - name: securitySettings
          value:
            - name: accessPolicies
              value:
                - - name: name
                    value: string
                  - name: accessRules
                    value:
                      - - name: scope
                          value: string
                        - name: filter
                          value: string
                        - name: access
                          value: string
                        - name: suid
                          value: boolean
                        - name: submountAccess
                          value: boolean
                        - name: rootSquash
                          value: boolean
                        - name: anonymousUID
                          value: string
                        - name: anonymousGID
                          value: string
        - name: directoryServicesSettings
          value:
            - name: activeDirectory
              value:
                - name: primaryDnsIpAddress
                  value: string
                - name: secondaryDnsIpAddress
                  value: string
                - name: domainName
                  value: string
                - name: domainNetBiosName
                  value: string
                - name: cacheNetBiosName
                  value: string
                - name: domainJoined
                  value: string
                - name: credentials
                  value:
                    - name: username
                      value: string
                    - name: password
                      value: string
            - name: usernameDownload
              value:
                - name: extendedGroups
                  value: boolean
                - name: usernameSource
                  value: string
                - name: groupFileURI
                  value: string
                - name: userFileURI
                  value: string
                - name: ldapServer
                  value: string
                - name: ldapBaseDN
                  value: string
                - name: encryptLdapConnection
                  value: boolean
                - name: requireValidCertificate
                  value: boolean
                - name: autoDownloadCertificate
                  value: boolean
                - name: caCertificateURI
                  value: string
                - name: usernameDownloaded
                  value: string
                - name: credentials
                  value:
                    - name: bindDn
                      value: string
                    - name: bindPassword
                      value: string
        - name: zones
          value:
            - string
        - name: primingJobs
          value: []
        - name: spaceAllocation
          value: []
    - name: sku
      value:
        - name: name
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>caches</code> resource.

```sql
/*+ update */
UPDATE azure.storage_cache.caches
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>caches</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_cache.caches
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
