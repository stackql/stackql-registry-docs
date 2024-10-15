---
title: software_update_configuration_machine_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - software_update_configuration_machine_runs
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

Creates, updates, deletes, gets or lists a <code>software_update_configuration_machine_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>software_update_configuration_machine_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.software_update_configuration_machine_runs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_software_update_configuration_machine_runs', value: 'view', },
        { label: 'software_update_configuration_machine_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id of the software update configuration machine run |
| <CopyableCode code="name" /> | `text` | Name of the software update configuration machine run |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configured_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="job" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="softwareUpdateConfigurationMachineRunId" /> | `text` | field from the `properties` object |
| <CopyableCode code="software_update_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_computer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_computer" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_computer_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id of the software update configuration machine run |
| <CopyableCode code="name" /> | `string` | Name of the software update configuration machine run |
| <CopyableCode code="properties" /> | `object` | Software update configuration machine run properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, softwareUpdateConfigurationMachineRunId, subscriptionId" /> | Get a single software update configuration machine run by Id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Return list of software update configuration machine runs |

## `SELECT` examples

Return list of software update configuration machine runs

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_software_update_configuration_machine_runs', value: 'view', },
        { label: 'software_update_configuration_machine_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
automationAccountName,
configured_duration,
correlation_id,
created_by,
creation_time,
end_time,
error,
job,
last_modified_by,
last_modified_time,
os_type,
resourceGroupName,
softwareUpdateConfigurationMachineRunId,
software_update_configuration,
source_computer_id,
start_time,
status,
subscriptionId,
target_computer,
target_computer_type
FROM azure.automation.vw_software_update_configuration_machine_runs
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
FROM azure.automation.software_update_configuration_machine_runs
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

