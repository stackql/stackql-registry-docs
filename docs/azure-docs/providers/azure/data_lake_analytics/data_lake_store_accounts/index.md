---
title: data_lake_store_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - data_lake_store_accounts
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

Creates, updates, deletes, gets or lists a <code>data_lake_store_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_lake_store_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_analytics.data_lake_store_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_lake_store_accounts', value: 'view', },
        { label: 'data_lake_store_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataLakeStoreAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="suffix" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The Data Lake Store account properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, dataLakeStoreAccountName, resourceGroupName, subscriptionId" /> | Gets the specified Data Lake Store account details in the specified Data Lake Analytics account. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the first page of Data Lake Store accounts linked to the specified Data Lake Analytics account. The response includes a link to the next page, if any. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, dataLakeStoreAccountName, resourceGroupName, subscriptionId" /> | Updates the Data Lake Analytics account specified to remove the specified Data Lake Store account. |
| <CopyableCode code="add" /> | `EXEC` | <CopyableCode code="accountName, dataLakeStoreAccountName, resourceGroupName, subscriptionId" /> | Updates the specified Data Lake Analytics account to include the additional Data Lake Store account. |

## `SELECT` examples

Gets the first page of Data Lake Store accounts linked to the specified Data Lake Analytics account. The response includes a link to the next page, if any.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_lake_store_accounts', value: 'view', },
        { label: 'data_lake_store_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
dataLakeStoreAccountName,
resourceGroupName,
subscriptionId,
suffix,
type
FROM azure.data_lake_analytics.vw_data_lake_store_accounts
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
FROM azure.data_lake_analytics.data_lake_store_accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>data_lake_store_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_lake_analytics.data_lake_store_accounts
WHERE accountName = '{{ accountName }}'
AND dataLakeStoreAccountName = '{{ dataLakeStoreAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
