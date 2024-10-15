---
title: monitoring_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_settings
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>monitoring_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.monitoring_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_monitoring_settings', value: 'view', },
        { label: 'monitoring_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="app_insights_agent_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_insights_instrumentation_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_insights_sampling_rate" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="trace_enabled" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Monitoring Setting properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get the Monitoring Setting and its properties. |
| <CopyableCode code="update_patch" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Update the Monitoring Setting. |
| <CopyableCode code="update_put" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Update the Monitoring Setting. |

## `SELECT` examples

Get the Monitoring Setting and its properties.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_monitoring_settings', value: 'view', },
        { label: 'monitoring_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
app_insights_agent_versions,
app_insights_instrumentation_key,
app_insights_sampling_rate,
error,
provisioning_state,
resourceGroupName,
serviceName,
subscriptionId,
trace_enabled
FROM azure.spring_apps.vw_monitoring_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.monitoring_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

