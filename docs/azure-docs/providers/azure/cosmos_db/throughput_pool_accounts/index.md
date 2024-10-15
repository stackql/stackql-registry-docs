---
title: throughput_pool_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - throughput_pool_accounts
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

Creates, updates, deletes, gets or lists a <code>throughput_pool_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>throughput_pool_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.throughput_pool_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_throughput_pool_accounts', value: 'view', },
        { label: 'throughput_pool_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_resource_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="throughputPoolAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="throughputPoolName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | An Azure Cosmos DB Global Database Account which is part of a Throughputpool. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, throughputPoolAccountName, throughputPoolName" /> | Retrieves the properties of an existing Azure Cosmos DB Throughput Pool |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, throughputPoolName" /> | Lists all the Azure Cosmos DB accounts available under the subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, throughputPoolAccountName, throughputPoolName" /> | Creates or updates an Azure Cosmos DB ThroughputPool account. The "Update" method is preferred when performing updates on an account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, throughputPoolAccountName, throughputPoolName" /> | Removes an existing Azure Cosmos DB database account from a throughput pool. |

## `SELECT` examples

Lists all the Azure Cosmos DB accounts available under the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_throughput_pool_accounts', value: 'view', },
        { label: 'throughput_pool_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
account_instance_id,
account_location,
account_resource_identifier,
provisioning_state,
resourceGroupName,
subscriptionId,
throughputPoolAccountName,
throughputPoolName
FROM azure.cosmos_db.vw_throughput_pool_accounts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND throughputPoolName = '{{ throughputPoolName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cosmos_db.throughput_pool_accounts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND throughputPoolName = '{{ throughputPoolName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>throughput_pool_accounts</code> resource.

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
INSERT INTO azure.cosmos_db.throughput_pool_accounts (
resourceGroupName,
subscriptionId,
throughputPoolAccountName,
throughputPoolName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ throughputPoolAccountName }}',
'{{ throughputPoolName }}',
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
        - name: provisioningState
          value: []
        - name: accountResourceIdentifier
          value: string
        - name: accountLocation
          value: string
        - name: accountInstanceId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>throughput_pool_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.throughput_pool_accounts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND throughputPoolAccountName = '{{ throughputPoolAccountName }}'
AND throughputPoolName = '{{ throughputPoolName }}';
```
