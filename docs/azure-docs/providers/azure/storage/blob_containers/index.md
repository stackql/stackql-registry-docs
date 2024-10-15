---
title: blob_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - blob_containers
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

Creates, updates, deletes, gets or lists a <code>blob_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>blob_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.blob_containers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_blob_containers', value: 'view', },
        { label: 'blob_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="containerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_encryption_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="deleted_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="deny_encryption_scope_override" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_nfs_v3_all_squash" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_nfs_v3_root_squash" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="has_immutability_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_legal_hold" /> | `text` | field from the `properties` object |
| <CopyableCode code="immutability_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="immutable_storage_with_versioning" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="lease_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="lease_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="lease_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="legal_hold" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="remaining_retention_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | The properties of a container. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId" /> | Gets properties of a specified container.  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all containers and does not support a prefix like data plane. Also SRP today does not return continuation token. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId" /> | Creates a new container under the specified account as described by request body. The container resource includes metadata and properties for that container. It does not include a list of the blobs contained by the container.  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId" /> | Deletes specified container under its account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId" /> | Updates container properties as specified in request body. Properties not mentioned in the request will be unchanged. Update fails if the specified container doesn't already exist.  |
| <CopyableCode code="clear_legal_hold" /> | `EXEC` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId, data__tags" /> | Clears legal hold tags. Clearing the same or non-existent tag results in an idempotent operation. ClearLegalHold clears out only the specified tags in the request. |
| <CopyableCode code="extend_immutability_policy" /> | `EXEC` | <CopyableCode code="If-Match, accountName, containerName, resourceGroupName, subscriptionId, data__properties" /> | Extends the immutabilityPeriodSinceCreationInDays of a locked immutabilityPolicy. The only action allowed on a Locked policy will be this action. ETag in If-Match is required for this operation. |
| <CopyableCode code="lease" /> | `EXEC` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId, data__action" /> | The Lease Container operation establishes and manages a lock on a container for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite. |
| <CopyableCode code="lock_immutability_policy" /> | `EXEC` | <CopyableCode code="If-Match, accountName, containerName, resourceGroupName, subscriptionId" /> | Sets the ImmutabilityPolicy to Locked state. The only action allowed on a Locked policy is ExtendImmutabilityPolicy action. ETag in If-Match is required for this operation. |
| <CopyableCode code="object_level_worm" /> | `EXEC` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId" /> | This operation migrates a blob container from container level WORM to object level immutability enabled container. Prerequisites require a container level immutability policy either in locked or unlocked state, Account level versioning must be enabled and there should be no Legal hold on the container. |
| <CopyableCode code="set_legal_hold" /> | `EXEC` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId, data__tags" /> | Sets legal hold tags. Setting the same tag results in an idempotent operation. SetLegalHold follows an append pattern and does not clear out the existing tags that are not specified in the request. |

## `SELECT` examples

Lists all containers and does not support a prefix like data plane. Also SRP today does not return continuation token.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_blob_containers', value: 'view', },
        { label: 'blob_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
containerName,
default_encryption_scope,
deleted,
deleted_time,
deny_encryption_scope_override,
enable_nfs_v3_all_squash,
enable_nfs_v3_root_squash,
etag,
has_immutability_policy,
has_legal_hold,
immutability_policy,
immutable_storage_with_versioning,
last_modified_time,
lease_duration,
lease_state,
lease_status,
legal_hold,
metadata,
public_access,
remaining_retention_days,
resourceGroupName,
subscriptionId,
version
FROM azure.storage.vw_blob_containers
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.storage.blob_containers
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>blob_containers</code> resource.

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
INSERT INTO azure.storage.blob_containers (
accountName,
containerName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ containerName }}',
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
    - name: properties
      value:
        - name: version
          value: string
        - name: deleted
          value: boolean
        - name: deletedTime
          value: string
        - name: remainingRetentionDays
          value: integer
        - name: defaultEncryptionScope
          value: string
        - name: denyEncryptionScopeOverride
          value: boolean
        - name: publicAccess
          value: string
        - name: lastModifiedTime
          value: string
        - name: leaseStatus
          value: string
        - name: leaseState
          value: string
        - name: leaseDuration
          value: string
        - name: metadata
          value: object
        - name: immutabilityPolicy
          value:
            - name: properties
              value:
                - name: immutabilityPeriodSinceCreationInDays
                  value: integer
                - name: state
                  value: string
                - name: allowProtectedAppendWrites
                  value: boolean
                - name: allowProtectedAppendWritesAll
                  value: boolean
            - name: etag
              value: string
            - name: updateHistory
              value:
                - - name: update
                    value: string
                  - name: immutabilityPeriodSinceCreationInDays
                    value: integer
                  - name: timestamp
                    value: string
                  - name: objectIdentifier
                    value: string
                  - name: tenantId
                    value: string
                  - name: upn
                    value: string
                  - name: allowProtectedAppendWrites
                    value: boolean
                  - name: allowProtectedAppendWritesAll
                    value: boolean
        - name: legalHold
          value:
            - name: hasLegalHold
              value: boolean
            - name: tags
              value:
                - - name: tag
                    value: string
                  - name: timestamp
                    value: string
                  - name: objectIdentifier
                    value: string
                  - name: tenantId
                    value: string
                  - name: upn
                    value: string
            - name: protectedAppendWritesHistory
              value:
                - name: allowProtectedAppendWritesAll
                  value: boolean
                - name: timestamp
                  value: string
        - name: hasLegalHold
          value: boolean
        - name: hasImmutabilityPolicy
          value: boolean
        - name: immutableStorageWithVersioning
          value:
            - name: enabled
              value: boolean
            - name: timeStamp
              value: string
            - name: migrationState
              value: string
        - name: enableNfsV3RootSquash
          value: boolean
        - name: enableNfsV3AllSquash
          value: boolean
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>blob_containers</code> resource.

```sql
/*+ update */
UPDATE azure.storage.blob_containers
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND containerName = '{{ containerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>blob_containers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage.blob_containers
WHERE accountName = '{{ accountName }}'
AND containerName = '{{ containerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
