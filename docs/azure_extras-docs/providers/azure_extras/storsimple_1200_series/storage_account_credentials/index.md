---
title: storage_account_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_account_credentials
  - storsimple_1200_series
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.storage_account_credentials" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="access_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentialName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_ssl" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_point" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="login" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Storage account properties |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="credentialName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified storage account credential name. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the storage account credentials in a manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="credentialName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the storage account credential |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="credentialName, managerName, resourceGroupName, subscriptionId" /> | Deletes the storage account credential |

## `SELECT` examples

Retrieves all the storage account credentials in a manager.

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
cloud_type,
credentialName,
enable_ssl,
end_point,
location,
login,
managerName,
resourceGroupName,
subscriptionId,
type
FROM azure_extras.storsimple_1200_series.vw_storage_account_credentials
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
properties,
type
FROM azure_extras.storsimple_1200_series.storage_account_credentials
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
INSERT INTO azure_extras.storsimple_1200_series.storage_account_credentials (
credentialName,
managerName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ credentialName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: properties
      value:
        - name: cloudType
          value: string
        - name: endPoint
          value: string
        - name: login
          value: string
        - name: location
          value: string
        - name: enableSSL
          value: string
        - name: accessKey
          value:
            - name: value
              value: string
            - name: encryptionCertificateThumbprint
              value: string
            - name: encryptionAlgorithm
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>storage_account_credentials</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.storage_account_credentials
WHERE credentialName = '{{ credentialName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
