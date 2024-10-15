---
title: service_healths
hide_title: false
hide_table_of_contents: false
keywords:
  - service_healths
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

Creates, updates, deletes, gets or lists a <code>service_healths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_healths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.infrastructure_insights_admin.service_healths" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_service_healths', value: 'view', },
        { label: 'service_healths', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="alert_summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="infra_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The Azure Region where the resource lives |
| <CopyableCode code="namespace" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="route_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceHealth" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The Azure Region where the resource lives |
| <CopyableCode code="properties" /> | `object` | Holds information about the health of a service. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, serviceHealth, subscriptionId" /> | Returns the requested service health object. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns the list of all resource provider health states. |

## `SELECT` examples

Returns the list of all resource provider health states.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_service_healths', value: 'view', },
        { label: 'service_healths', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
alert_summary,
display_name,
health_state,
infra_uri,
location,
namespace,
registration_id,
resourceGroupName,
route_prefix,
serviceHealth,
service_location,
subscriptionId,
tags
FROM azure_stack.infrastructure_insights_admin.vw_service_healths
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_stack.infrastructure_insights_admin.service_healths
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

