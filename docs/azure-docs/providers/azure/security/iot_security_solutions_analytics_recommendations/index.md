---
title: iot_security_solutions_analytics_recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solutions_analytics_recommendations
  - security
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

Creates, updates, deletes, gets or lists a <code>iot_security_solutions_analytics_recommendations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_security_solutions_analytics_recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.iot_security_solutions_analytics_recommendations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_security_solutions_analytics_recommendations', value: 'view', },
        { label: 'iot_security_solutions_analytics_recommendations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="aggregatedRecommendationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="detected_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="healthy_devices" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_analytics_query" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendation_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendation_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendation_type_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation_steps" /> | `text` | field from the `properties` object |
| <CopyableCode code="reported_severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="unhealthy_device_count" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | IoT Security solution aggregated recommendation information |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="aggregatedRecommendationName, resourceGroupName, solutionName, subscriptionId" /> | Use this method to get the aggregated security analytics recommendation of yours IoT Security solution. This aggregation is performed by recommendation name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Use this method to get the list of aggregated security analytics recommendations of yours IoT Security solution. |

## `SELECT` examples

Use this method to get the list of aggregated security analytics recommendations of yours IoT Security solution.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_security_solutions_analytics_recommendations', value: 'view', },
        { label: 'iot_security_solutions_analytics_recommendations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
aggregatedRecommendationName,
detected_by,
healthy_devices,
log_analytics_query,
recommendation_display_name,
recommendation_name,
recommendation_type_id,
remediation_steps,
reported_severity,
resourceGroupName,
solutionName,
subscriptionId,
tags,
type,
unhealthy_device_count
FROM azure.security.vw_iot_security_solutions_analytics_recommendations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
tags,
type
FROM azure.security.iot_security_solutions_analytics_recommendations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

