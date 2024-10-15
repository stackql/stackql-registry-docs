---
title: file_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - file_shares
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

Creates, updates, deletes, gets or lists a <code>file_shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.file_shares" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_shares', value: 'view', },
        { label: 'file_shares', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="access_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_tier_change_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_tier_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="deleted_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_protocols" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="lease_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="lease_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="lease_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="remaining_retention_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="root_squash" /> | `text` | field from the `properties` object |
| <CopyableCode code="shareName" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_quota" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_usage_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="signed_identifiers" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshot_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | The properties of the file share. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId" /> | Gets properties of a specified share. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all shares. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId" /> | Creates a new share under the specified account as described by request body. The share resource includes metadata and properties for that share. It does not include a list of the files contained by the share.  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId" /> | Deletes specified share under its account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId" /> | Updates share properties as specified in request body. Properties not mentioned in the request will not be changed. Update fails if the specified share does not already exist.  |
| <CopyableCode code="lease" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId, data__action" /> | The Lease Share operation establishes and manages a lock on a share for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId, data__deletedShareName, data__deletedShareVersion" /> | Restore a file share within a valid retention days if share soft delete is enabled |

## `SELECT` examples

Lists all shares.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_shares', value: 'view', },
        { label: 'file_shares', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
access_tier,
access_tier_change_time,
access_tier_status,
accountName,
deleted,
deleted_time,
enabled_protocols,
etag,
last_modified_time,
lease_duration,
lease_state,
lease_status,
metadata,
remaining_retention_days,
resourceGroupName,
root_squash,
shareName,
share_quota,
share_usage_bytes,
signed_identifiers,
snapshot_time,
subscriptionId,
version
FROM azure.storage.vw_file_shares
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
FROM azure.storage.file_shares
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>file_shares</code> resource.

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
INSERT INTO azure.storage.file_shares (
accountName,
resourceGroupName,
shareName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ shareName }}',
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
        - name: lastModifiedTime
          value: string
        - name: metadata
          value: object
        - name: shareQuota
          value: integer
        - name: enabledProtocols
          value: string
        - name: rootSquash
          value: string
        - name: version
          value: string
        - name: deleted
          value: boolean
        - name: deletedTime
          value: string
        - name: remainingRetentionDays
          value: integer
        - name: accessTier
          value: string
        - name: accessTierChangeTime
          value: string
        - name: accessTierStatus
          value: string
        - name: shareUsageBytes
          value: integer
        - name: leaseStatus
          value: string
        - name: leaseState
          value: string
        - name: leaseDuration
          value: string
        - name: signedIdentifiers
          value:
            - - name: id
                value: string
              - name: accessPolicy
                value:
                  - name: startTime
                    value: string
                  - name: expiryTime
                    value: string
                  - name: permission
                    value: string
        - name: snapshotTime
          value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>file_shares</code> resource.

```sql
/*+ update */
UPDATE azure.storage.file_shares
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>file_shares</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage.file_shares
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
