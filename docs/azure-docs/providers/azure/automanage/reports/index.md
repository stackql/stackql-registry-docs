---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - automanage
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

Creates, updates, deletes, gets or lists a <code>reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.reports" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reports', value: 'view', },
        { label: 'reports', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configurationProfileAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="reportName" /> | `text` | field from the `properties` object |
| <CopyableCode code="report_format_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Data related to the report detail. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationProfileAssignmentName, reportName, resourceGroupName, subscriptionId, vmName" /> | Get information about a report associated with a configuration profile assignment run |
| <CopyableCode code="list_by_configuration_profile_assignments" /> | `SELECT` | <CopyableCode code="configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName" /> | Retrieve a list of reports within a given configuration profile assignment |

## `SELECT` examples

Retrieve a list of reports within a given configuration profile assignment

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reports', value: 'view', },
        { label: 'reports', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
configurationProfileAssignmentName,
configuration_profile,
duration,
end_time,
error,
last_modified_time,
reportName,
report_format_version,
resourceGroupName,
resources,
start_time,
status,
subscriptionId,
system_data,
type,
vmName
FROM azure.automanage.vw_reports
WHERE configurationProfileAssignmentName = '{{ configurationProfileAssignmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmName = '{{ vmName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.automanage.reports
WHERE configurationProfileAssignmentName = '{{ configurationProfileAssignmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmName = '{{ vmName }}';
```
</TabItem></Tabs>

