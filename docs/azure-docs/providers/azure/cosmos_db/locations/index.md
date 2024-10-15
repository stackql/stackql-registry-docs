---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
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

Creates, updates, deletes, gets or lists a <code>locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.locations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_locations', value: 'view', },
        { label: 'locations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `text` | The name of the database account. |
| <CopyableCode code="backup_storage_redundancies" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_residency_restricted" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_subscription_region_access_allowed_for_az" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_subscription_region_access_allowed_for_regular" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supports_availability_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | Cosmos DB location metadata |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get the properties of an existing Cosmos DB location |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Cosmos DB locations and their properties |

## `SELECT` examples

List Cosmos DB locations and their properties

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_locations', value: 'view', },
        { label: 'locations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backup_storage_redundancies,
is_residency_restricted,
is_subscription_region_access_allowed_for_az,
is_subscription_region_access_allowed_for_regular,
location,
status,
subscriptionId,
supports_availability_zone,
type
FROM azure.cosmos_db.vw_locations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.cosmos_db.locations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

