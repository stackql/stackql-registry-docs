---
title: health_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - health_reports
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

Creates, updates, deletes, gets or lists a <code>health_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.health_reports" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_health_reports', value: 'view', },
        { label: 'health_reports', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="affected_defenders_plans" /> | `text` | field from the `properties` object |
| <CopyableCode code="affected_defenders_sub_plans" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="healthReportName" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_data_classification" /> | `text` | field from the `properties` object |
| <CopyableCode code="issues" /> | `text` | field from the `properties` object |
| <CopyableCode code="report_additional_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of the health report |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="healthReportName, resourceId" /> | Get health report of resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get a list of all health reports inside a scope. Valid scopes are: subscription (format: 'subscriptions/{subscriptionId}'), or security connector (format: 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})' |

## `SELECT` examples

Get a list of all health reports inside a scope. Valid scopes are: subscription (format: 'subscriptions/{subscriptionId}'), or security connector (format: 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_health_reports', value: 'view', },
        { label: 'health_reports', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
affected_defenders_plans,
affected_defenders_sub_plans,
environment_details,
healthReportName,
health_data_classification,
issues,
report_additional_data,
resourceId,
resource_details,
scope,
status,
type
FROM azure.security.vw_health_reports
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.health_reports
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

