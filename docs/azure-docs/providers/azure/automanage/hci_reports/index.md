---
title: hci_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - hci_reports
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

Creates, updates, deletes, gets or lists a <code>hci_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hci_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.hci_reports" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hci_reports', value: 'view', },
        { label: 'hci_reports', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, configurationProfileAssignmentName, reportName, resourceGroupName, subscriptionId" /> | Get information about a report associated with a configuration profile assignment run |
| <CopyableCode code="list_by_configuration_profile_assignments" /> | `SELECT` | <CopyableCode code="clusterName, configurationProfileAssignmentName, resourceGroupName, subscriptionId" /> | Retrieve a list of reports within a given configuration profile assignment |

## `SELECT` examples

Retrieve a list of reports within a given configuration profile assignment

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hci_reports', value: 'view', },
        { label: 'hci_reports', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
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
type
FROM azure.automanage.vw_hci_reports
WHERE clusterName = '{{ clusterName }}'
AND configurationProfileAssignmentName = '{{ configurationProfileAssignmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.automanage.hci_reports
WHERE clusterName = '{{ clusterName }}'
AND configurationProfileAssignmentName = '{{ configurationProfileAssignmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

