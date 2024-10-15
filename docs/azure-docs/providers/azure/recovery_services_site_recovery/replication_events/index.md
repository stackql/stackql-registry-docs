---
title: replication_events
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_events
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

Creates, updates, deletes, gets or lists a <code>replication_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_events" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_events', value: 'view', },
        { label: 'replication_events', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="affected_object_correlation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="affected_object_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="eventName" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="provider_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_of_occurrence" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | The properties of a monitoring event. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventName, resourceGroupName, resourceName, subscriptionId" /> | The operation to get the details of an Azure Site recovery event. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the list of Azure Site Recovery events for the vault. |

## `SELECT` examples

Gets the list of Azure Site Recovery events for the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_events', value: 'view', },
        { label: 'replication_events', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
affected_object_correlation_id,
affected_object_friendly_name,
eventName,
event_code,
event_specific_details,
event_type,
fabric_id,
health_errors,
location,
provider_specific_details,
resourceGroupName,
resourceName,
severity,
subscriptionId,
time_of_occurrence,
type
FROM azure.recovery_services_site_recovery.vw_replication_events
WHERE resourceGroupName = '{{ resourceGroupName }}'
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
FROM azure.recovery_services_site_recovery.replication_events
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

