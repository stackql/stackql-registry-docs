---
title: storage_account_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_account_credentials
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>storage_account_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_account_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.storage_account_credentials" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_account_credentials', value: 'view', },
        { label: 'storage_account_credentials', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The name of the object. |
| <CopyableCode code="access_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_point" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssl_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageAccountCredentialName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
| <CopyableCode code="volumes_count" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The storage account credential properties. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, storageAccountCredentialName, subscriptionId" /> | Gets the properties of the specified storage account credential name. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Gets all the storage account credentials in a manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managerName, resourceGroupName, storageAccountCredentialName, subscriptionId, data__properties" /> | Creates or updates the storage account credential. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managerName, resourceGroupName, storageAccountCredentialName, subscriptionId" /> | Deletes the storage account credential. |

## `SELECT` examples

Gets all the storage account credentials in a manager.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_account_credentials', value: 'view', },
        { label: 'storage_account_credentials', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
access_key,
end_point,
kind,
managerName,
resourceGroupName,
ssl_status,
storageAccountCredentialName,
subscriptionId,
type,
volumes_count
FROM azure_extras.storsimple_8000_series.vw_storage_account_credentials
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure_extras.storsimple_8000_series.storage_account_credentials
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_account_credentials</code> resource.

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
INSERT INTO azure_extras.storsimple_8000_series.storage_account_credentials (
managerName,
resourceGroupName,
storageAccountCredentialName,
subscriptionId,
data__properties,
kind,
properties
)
SELECT 
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ storageAccountCredentialName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: kind
      value: string
    - name: properties
      value:
        - name: endPoint
          value: string
        - name: sslStatus
          value: string
        - name: accessKey
          value:
            - name: value
              value: string
            - name: encryptionCertThumbprint
              value: string
            - name: encryptionAlgorithm
              value: string
        - name: volumesCount
          value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>storage_account_credentials</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_8000_series.storage_account_credentials
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageAccountCredentialName = '{{ storageAccountCredentialName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
