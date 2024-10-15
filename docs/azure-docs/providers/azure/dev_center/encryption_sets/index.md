---
title: encryption_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_sets
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>encryption_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>encryption_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.encryption_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_encryption_sets', value: 'view', },
        { label: 'encryption_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="devbox_disks_encryption_enable_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryptionSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="key_encryption_key_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the devcenter encryption set. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devCenterName, encryptionSetName, resourceGroupName, subscriptionId" /> | Gets a devcenter encryption set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Lists all encryption sets in the devcenter. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="devCenterName, encryptionSetName, resourceGroupName, subscriptionId" /> | Creates or updates a devcenter encryption set resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="devCenterName, encryptionSetName, resourceGroupName, subscriptionId" /> | Deletes a devcenter encryption set |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="devCenterName, encryptionSetName, resourceGroupName, subscriptionId" /> | Partially updates a devcenter encryption set. |

## `SELECT` examples

Lists all encryption sets in the devcenter.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_encryption_sets', value: 'view', },
        { label: 'encryption_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
devCenterName,
devbox_disks_encryption_enable_status,
encryptionSetName,
identity,
key_encryption_key_url,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.dev_center.vw_encryption_sets
WHERE devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.dev_center.encryption_sets
WHERE devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>encryption_sets</code> resource.

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
INSERT INTO azure.dev_center.encryption_sets (
devCenterName,
encryptionSetName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
identity
)
SELECT 
'{{ devCenterName }}',
'{{ encryptionSetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: devboxDisksEncryptionEnableStatus
          value: []
        - name: keyEncryptionKeyUrl
          value: string
        - name: provisioningState
          value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>encryption_sets</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.encryption_sets
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
devCenterName = '{{ devCenterName }}'
AND encryptionSetName = '{{ encryptionSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>encryption_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.encryption_sets
WHERE devCenterName = '{{ devCenterName }}'
AND encryptionSetName = '{{ encryptionSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
