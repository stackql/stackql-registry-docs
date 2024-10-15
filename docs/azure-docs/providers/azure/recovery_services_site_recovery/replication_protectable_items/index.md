---
title: replication_protectable_items
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protectable_items
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_protectable_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_protectable_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protectable_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protectable_items', value: 'view', },
        { label: 'replication_protectable_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="custom_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="protectableItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectionContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_readiness_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_services_provider_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_protected_item_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_replication_providers" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Replication protected item custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, protectableItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to get the details of a protectable item. |
| <CopyableCode code="list_by_replication_protection_containers" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Lists the protectable items in a protection container. |

## `SELECT` examples

Lists the protectable items in a protection container.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protectable_items', value: 'view', },
        { label: 'replication_protectable_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
custom_details,
fabricName,
friendly_name,
location,
protectableItemName,
protectionContainerName,
protection_readiness_errors,
protection_status,
recovery_services_provider_id,
replication_protected_item_id,
resourceGroupName,
resourceName,
subscriptionId,
supported_replication_providers,
type
FROM azure.recovery_services_site_recovery.vw_replication_protectable_items
WHERE fabricName = '{{ fabricName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.recovery_services_site_recovery.replication_protectable_items
WHERE fabricName = '{{ fabricName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

