---
title: iot_security_solutions_analytics_aggregated_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solutions_analytics_aggregated_alerts
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

Creates, updates, deletes, gets or lists a <code>iot_security_solutions_analytics_aggregated_alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_security_solutions_analytics_aggregated_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.iot_security_solutions_analytics_aggregated_alerts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_security_solutions_analytics_aggregated_alerts', value: 'view', },
        { label: 'iot_security_solutions_analytics_aggregated_alerts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="action_taken" /> | `text` | field from the `properties` object |
| <CopyableCode code="aggregatedAlertName" /> | `text` | field from the `properties` object |
| <CopyableCode code="aggregated_date_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="count" /> | `text` | field from the `properties` object |
| <CopyableCode code="effected_resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_analytics_query" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation_steps" /> | `text` | field from the `properties` object |
| <CopyableCode code="reported_severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="top_devices_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="vendor_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | IoT Security solution aggregated alert details. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="aggregatedAlertName, resourceGroupName, solutionName, subscriptionId" /> | Use this method to get a single the aggregated alert of yours IoT Security solution. This aggregation is performed by alert name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Use this method to get the aggregated alert list of yours IoT Security solution. |
| <CopyableCode code="dismiss" /> | `EXEC` | <CopyableCode code="aggregatedAlertName, resourceGroupName, solutionName, subscriptionId" /> | Use this method to dismiss an aggregated IoT Security Solution Alert. |

## `SELECT` examples

Use this method to get the aggregated alert list of yours IoT Security solution.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_security_solutions_analytics_aggregated_alerts', value: 'view', },
        { label: 'iot_security_solutions_analytics_aggregated_alerts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
action_taken,
aggregatedAlertName,
aggregated_date_utc,
alert_display_name,
alert_type,
count,
effected_resource_type,
log_analytics_query,
remediation_steps,
reported_severity,
resourceGroupName,
solutionName,
subscriptionId,
system_source,
tags,
top_devices_list,
type,
vendor_name
FROM azure.security.vw_iot_security_solutions_analytics_aggregated_alerts
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
FROM azure.security.iot_security_solutions_analytics_aggregated_alerts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

