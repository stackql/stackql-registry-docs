---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - media_services
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

Creates, updates, deletes, gets or lists a <code>assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.assets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assets', value: 'view', },
        { label: 'assets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="alternate_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="assetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="asset_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="container" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_encryption_format" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Asset properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId" /> | Get the details of an Asset in the Media Services account |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List Assets in the Media Services account with optional filtering and ordering |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId" /> | Creates or updates an Asset in the Media Services account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId" /> | Deletes an Asset in the Media Services account |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId" /> | Updates an existing Asset in the Media Services account |

## `SELECT` examples

List Assets in the Media Services account with optional filtering and ordering

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assets', value: 'view', },
        { label: 'assets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accountName,
alternate_id,
assetName,
asset_id,
container,
created,
encryption_scope,
last_modified,
resourceGroupName,
storage_account_name,
storage_encryption_format,
subscriptionId,
system_data
FROM azure.media_services.vw_assets
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.media_services.assets
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assets</code> resource.

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
INSERT INTO azure.media_services.assets (
accountName,
assetName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ assetName }}',
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
        - name: assetId
          value: string
        - name: created
          value: string
        - name: lastModified
          value: string
        - name: alternateId
          value: string
        - name: description
          value: string
        - name: container
          value: string
        - name: storageAccountName
          value: string
        - name: storageEncryptionFormat
          value: string
        - name: encryptionScope
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

Updates a <code>assets</code> resource.

```sql
/*+ update */
UPDATE azure.media_services.assets
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>assets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.assets
WHERE accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
