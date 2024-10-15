---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - app_compliance_automation
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.snapshots" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshots', value: 'view', },
        { label: 'snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="compliance_results" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reportName" /> | `text` | field from the `properties` object |
| <CopyableCode code="report_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="report_system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshotName" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshot_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Snapshot's properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reportName, snapshotName" /> | Get the AppComplianceAutomation snapshot and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reportName" /> | Get the AppComplianceAutomation snapshot list. |
| <CopyableCode code="download" /> | `EXEC` | <CopyableCode code="reportName, snapshotName, data__downloadType" /> | Download compliance needs from snapshot, like: Compliance Report, Resource List. |

## `SELECT` examples

Get the AppComplianceAutomation snapshot list.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshots', value: 'view', },
        { label: 'snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
compliance_results,
created_at,
provisioning_state,
reportName,
report_properties,
report_system_data,
snapshotName,
snapshot_name
FROM azure_extras.app_compliance_automation.vw_snapshots
WHERE reportName = '{{ reportName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.app_compliance_automation.snapshots
WHERE reportName = '{{ reportName }}';
```
</TabItem></Tabs>

