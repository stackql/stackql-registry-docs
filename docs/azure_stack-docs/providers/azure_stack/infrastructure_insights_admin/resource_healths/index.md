---
title: resource_healths
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_healths
  - infrastructure_insights_admin
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

Creates, updates, deletes, gets or lists a <code>resource_healths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_healths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.infrastructure_insights_admin.resource_healths" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_healths', value: 'view', },
        { label: 'resource_healths', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="alert_summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The Azure Region where the resource lives |
| <CopyableCode code="namespace" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceRegistrationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="route_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="rp_registration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceRegistrationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="usage_metrics" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The Azure Region where the resource lives |
| <CopyableCode code="properties" /> | `object` | Health information related to a resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, resourceRegistrationId, serviceRegistrationId, subscriptionId" /> | Returns the requested health information about a resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, serviceRegistrationId, subscriptionId" /> | Returns a list of each resource's health under a service. |

## `SELECT` examples

Returns a list of each resource's health under a service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_healths', value: 'view', },
        { label: 'resource_healths', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
alert_summary,
health_state,
location,
namespace,
registration_id,
resourceGroupName,
resourceRegistrationId,
resource_display_name,
resource_location,
resource_name,
resource_type,
resource_uri,
route_prefix,
rp_registration_id,
serviceRegistrationId,
subscriptionId,
tags,
usage_metrics
FROM azure_stack.infrastructure_insights_admin.vw_resource_healths
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceRegistrationId = '{{ serviceRegistrationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_stack.infrastructure_insights_admin.resource_healths
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceRegistrationId = '{{ serviceRegistrationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

