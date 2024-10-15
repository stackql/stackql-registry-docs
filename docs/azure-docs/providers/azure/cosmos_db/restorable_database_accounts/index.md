---
title: restorable_database_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_database_accounts
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>restorable_database_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restorable_database_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.restorable_database_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restorable_database_accounts', value: 'view', },
        { label: 'restorable_database_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `text` | The name of the ARM resource. |
| <CopyableCode code="account_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="oldest_restorable_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorable_locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="properties" /> | `object` | The properties of a restorable database account. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_location" /> | `SELECT` | <CopyableCode code="instanceId, location, subscriptionId" /> | Retrieves the properties of an existing Azure Cosmos DB restorable database account.  This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read/*' permission. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the restorable Azure Cosmos DB database accounts available under the subscription. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Lists all the restorable Azure Cosmos DB database accounts available under the subscription and in a region.  This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission. |

## `SELECT` examples

Lists all the restorable Azure Cosmos DB database accounts available under the subscription. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restorable_database_accounts', value: 'view', },
        { label: 'restorable_database_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
account_name,
api_type,
creation_time,
deletion_time,
instanceId,
location,
oldest_restorable_time,
restorable_locations,
subscriptionId,
type
FROM azure.cosmos_db.vw_restorable_database_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.cosmos_db.restorable_database_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

