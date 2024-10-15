---
title: chaos_faults
hide_title: false
hide_table_of_contents: false
keywords:
  - chaos_faults
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

Creates, updates, deletes, gets or lists a <code>chaos_faults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>chaos_faults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.chaos_faults" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_chaos_faults', value: 'view', },
        { label: 'chaos_faults', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="action" /> | `text` | field from the `properties` object |
| <CopyableCode code="chaosFault" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="region" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A request object to enable/disable the chaos fault. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, chaosFault, resourceGroupName, subscriptionId" /> | Get Chaos Fault for a CosmosdB account for a particular Chaos Fault. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List Chaos Faults for CosmosDB account. |
| <CopyableCode code="enable_disable" /> | `EXEC` | <CopyableCode code="accountName, chaosFault, resourceGroupName, subscriptionId" /> | Enable, disable Chaos Fault in a CosmosDB account. |

## `SELECT` examples

List Chaos Faults for CosmosDB account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_chaos_faults', value: 'view', },
        { label: 'chaos_faults', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
action,
chaosFault,
container_name,
database_name,
provisioning_state,
region,
resourceGroupName,
subscriptionId
FROM azure.cosmos_db.vw_chaos_faults
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cosmos_db.chaos_faults
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

