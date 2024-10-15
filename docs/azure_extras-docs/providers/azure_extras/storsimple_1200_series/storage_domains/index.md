---
title: storage_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_domains
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

Creates, updates, deletes, gets or lists a <code>storage_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.storage_domains" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_domains', value: 'view', },
        { label: 'storage_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="encryption_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageDomainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_credential_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | The storage domain properties. |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, storageDomainName, subscriptionId" /> | Returns the properties of the specified storage domain name. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the storage domains in a manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managerName, resourceGroupName, storageDomainName, subscriptionId, data__properties" /> | Creates or updates the storage domain. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managerName, resourceGroupName, storageDomainName, subscriptionId" /> | Deletes the storage domain. |

## `SELECT` examples

Retrieves all the storage domains in a manager.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_domains', value: 'view', },
        { label: 'storage_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
encryption_key,
encryption_status,
managerName,
resourceGroupName,
storageDomainName,
storage_account_credential_ids,
subscriptionId,
type
FROM azure_extras.storsimple_1200_series.vw_storage_domains
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
FROM azure_extras.storsimple_1200_series.storage_domains
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_domains</code> resource.

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
INSERT INTO azure_extras.storsimple_1200_series.storage_domains (
managerName,
resourceGroupName,
storageDomainName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ storageDomainName }}',
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
        - name: storageAccountCredentialIds
          value:
            - string
        - name: encryptionKey
          value:
            - name: value
              value: string
            - name: encryptionCertificateThumbprint
              value: string
            - name: encryptionAlgorithm
              value: string
        - name: encryptionStatus
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>storage_domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.storage_domains
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageDomainName = '{{ storageDomainName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
