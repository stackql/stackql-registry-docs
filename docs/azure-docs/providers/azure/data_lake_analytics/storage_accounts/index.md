---
title: storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_accounts
  - data_lake_analytics
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

Creates, updates, deletes, gets or lists a <code>storage_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_analytics.storage_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_accounts', value: 'view', },
        { label: 'storage_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="suffix" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The Azure Storage account properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, storageAccountName, subscriptionId" /> | Gets the specified Azure Storage account linked to the given Data Lake Analytics account. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the first page of Azure Storage accounts, if any, linked to the specified Data Lake Analytics account. The response includes a link to the next page, if any. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, storageAccountName, subscriptionId" /> | Updates the specified Data Lake Analytics account to remove an Azure Storage account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, storageAccountName, subscriptionId" /> | Updates the Data Lake Analytics account to replace Azure Storage blob account details, such as the access key and/or suffix. |
| <CopyableCode code="add" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, storageAccountName, subscriptionId, data__properties" /> | Updates the specified Data Lake Analytics account to add an Azure Storage account. |

## `SELECT` examples

Gets the first page of Azure Storage accounts, if any, linked to the specified Data Lake Analytics account. The response includes a link to the next page, if any.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_accounts', value: 'view', },
        { label: 'storage_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
resourceGroupName,
storageAccountName,
subscriptionId,
suffix,
type
FROM azure.data_lake_analytics.vw_storage_accounts
WHERE accountName = '{{ accountName }}'
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
FROM azure.data_lake_analytics.storage_accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>storage_accounts</code> resource.

```sql
/*+ update */
UPDATE azure.data_lake_analytics.storage_accounts
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageAccountName = '{{ storageAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>storage_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_lake_analytics.storage_accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageAccountName = '{{ storageAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
