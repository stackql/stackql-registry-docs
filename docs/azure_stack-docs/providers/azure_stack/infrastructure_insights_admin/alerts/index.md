---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
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

Creates, updates, deletes, gets or lists a <code>alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.infrastructure_insights_admin.alerts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts', value: 'view', },
        { label: 'alerts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="alertName" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="closed_by_user_alias" /> | `text` | field from the `properties` object |
| <CopyableCode code="closed_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="fault_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="fault_type_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_valid_remediation_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="impacted_resource_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="impacted_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The Azure Region where the resource lives |
| <CopyableCode code="remediation" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_provider_registration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_registration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The Azure Region where the resource lives |
| <CopyableCode code="properties" /> | `object` | Contains alert data. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertName, location, resourceGroupName, subscriptionId" /> | Returns the requested an alert. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns the list of all alerts in a given region. |
| <CopyableCode code="close" /> | `EXEC` | <CopyableCode code="alertName, location, resourceGroupName, subscriptionId, user" /> | Closes the given alert. |
| <CopyableCode code="repair" /> | `EXEC` | <CopyableCode code="alertName, location, resourceGroupName, subscriptionId" /> | Repairs an alert. |

## `SELECT` examples

Returns the list of all alerts in a given region.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts', value: 'view', },
        { label: 'alerts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
alertName,
alert_id,
alert_properties,
closed_by_user_alias,
closed_timestamp,
created_timestamp,
fault_id,
fault_type_id,
has_valid_remediation_action,
impacted_resource_display_name,
impacted_resource_id,
last_updated_timestamp,
location,
remediation,
resourceGroupName,
resource_provider_registration_id,
resource_registration_id,
severity,
state,
subscriptionId,
tags,
title
FROM azure_stack.infrastructure_insights_admin.vw_alerts
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
FROM azure_stack.infrastructure_insights_admin.alerts
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

