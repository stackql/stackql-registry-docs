---
title: software_update_configuration_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - software_update_configuration_runs
  - automation
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

Creates, updates, deletes, gets or lists a <code>software_update_configuration_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>software_update_configuration_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.software_update_configuration_runs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_software_update_configuration_runs', value: 'view', },
        { label: 'software_update_configuration_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id of the software update configuration run |
| <CopyableCode code="name" /> | `text` | Name of the software update configuration run. |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="computer_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="configured_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="failed_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="softwareUpdateConfigurationRunId" /> | `text` | field from the `properties` object |
| <CopyableCode code="software_update_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tasks" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id of the software update configuration run |
| <CopyableCode code="name" /> | `string` | Name of the software update configuration run. |
| <CopyableCode code="properties" /> | `object` | Software update configuration properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, softwareUpdateConfigurationRunId, subscriptionId" /> | Get a single software update configuration Run by Id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Return list of software update configuration runs |

## `SELECT` examples

Return list of software update configuration runs

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_software_update_configuration_runs', value: 'view', },
        { label: 'software_update_configuration_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
automationAccountName,
computer_count,
configured_duration,
created_by,
creation_time,
end_time,
failed_count,
last_modified_by,
last_modified_time,
os_type,
resourceGroupName,
softwareUpdateConfigurationRunId,
software_update_configuration,
start_time,
status,
subscriptionId,
tasks
FROM azure.automation.vw_software_update_configuration_runs
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties
FROM azure.automation.software_update_configuration_runs
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

