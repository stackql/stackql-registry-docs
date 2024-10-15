---
title: configuration_stores_deleted
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_stores_deleted
  - app_configuration
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

Creates, updates, deletes, gets or lists a <code>configuration_stores_deleted</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_stores_deleted</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.configuration_stores_deleted" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_stores_deleted', value: 'view', },
        { label: 'configuration_stores_deleted', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID for the deleted configuration store. |
| <CopyableCode code="name" /> | `text` | The name of the configuration store. |
| <CopyableCode code="configStoreName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_store_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="purge_protection_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_purge_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type of the configuration store. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID for the deleted configuration store. |
| <CopyableCode code="name" /> | `string` | The name of the configuration store. |
| <CopyableCode code="properties" /> | `object` | Properties of the deleted configuration store. |
| <CopyableCode code="type" /> | `string` | The resource type of the configuration store. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, location, subscriptionId" /> | Gets a deleted Azure app configuration store. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets information about the deleted configuration stores in a subscription. |

## `SELECT` examples

Gets information about the deleted configuration stores in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_stores_deleted', value: 'view', },
        { label: 'configuration_stores_deleted', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
configStoreName,
configuration_store_id,
deletion_date,
location,
purge_protection_enabled,
scheduled_purge_date,
subscriptionId,
tags,
type
FROM azure.app_configuration.vw_configuration_stores_deleted
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
FROM azure.app_configuration.configuration_stores_deleted
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

