---
title: disk_encryption_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_encryption_sets
  - compute
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

Creates, updates, deletes, gets or lists a <code>disk_encryption_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_encryption_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_encryption_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_encryption_sets', value: 'view', },
        { label: 'disk_encryption_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="active_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_key_rotation_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="diskEncryptionSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="federated_client_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks. |
| <CopyableCode code="last_key_rotation_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="previous_keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rotation_to_latest_key_version_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="identity" /> | `object` | The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskEncryptionSetName, resourceGroupName, subscriptionId" /> | Gets information about a disk encryption set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the disk encryption sets under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the disk encryption sets under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diskEncryptionSetName, resourceGroupName, subscriptionId" /> | Creates or updates a disk encryption set |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskEncryptionSetName, resourceGroupName, subscriptionId" /> | Deletes a disk encryption set. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="diskEncryptionSetName, resourceGroupName, subscriptionId" /> | Updates (patches) a disk encryption set. |

## `SELECT` examples

Lists all the disk encryption sets under a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_encryption_sets', value: 'view', },
        { label: 'disk_encryption_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
active_key,
auto_key_rotation_error,
diskEncryptionSetName,
encryption_type,
federated_client_id,
identity,
last_key_rotation_timestamp,
location,
previous_keys,
provisioning_state,
resourceGroupName,
rotation_to_latest_key_version_enabled,
subscriptionId,
tags,
type
FROM azure.compute.vw_disk_encryption_sets
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
tags,
type
FROM azure.compute.disk_encryption_sets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>disk_encryption_sets</code> resource.

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
INSERT INTO azure.compute.disk_encryption_sets (
diskEncryptionSetName,
resourceGroupName,
subscriptionId,
identity,
properties,
location,
tags
)
SELECT 
'{{ diskEncryptionSetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ identity }}',
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
    - name: properties
      value:
        - name: encryptionType
          value: []
        - name: activeKey
          value:
            - name: sourceVault
              value:
                - name: id
                  value: string
            - name: keyUrl
              value: string
        - name: previousKeys
          value:
            - - name: keyUrl
                value: string
        - name: provisioningState
          value: string
        - name: rotationToLatestKeyVersionEnabled
          value: boolean
        - name: lastKeyRotationTimestamp
          value: string
        - name: autoKeyRotationError
          value:
            - name: details
              value:
                - - name: code
                    value: string
                  - name: target
                    value: string
                  - name: message
                    value: string
            - name: innererror
              value:
                - name: exceptiontype
                  value: string
                - name: errordetail
                  value: string
            - name: code
              value: string
            - name: target
              value: string
            - name: message
              value: string
        - name: federatedClientId
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>disk_encryption_sets</code> resource.

```sql
/*+ update */
UPDATE azure.compute.disk_encryption_sets
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
diskEncryptionSetName = '{{ diskEncryptionSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>disk_encryption_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.disk_encryption_sets
WHERE diskEncryptionSetName = '{{ diskEncryptionSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
