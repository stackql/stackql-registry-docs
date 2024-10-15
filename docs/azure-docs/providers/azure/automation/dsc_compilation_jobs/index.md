---
title: dsc_compilation_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_compilation_jobs
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

Creates, updates, deletes, gets or lists a <code>dsc_compilation_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dsc_compilation_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.dsc_compilation_jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dsc_compilation_jobs', value: 'view', },
        { label: 'dsc_compilation_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="compilationJobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="exception" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_status_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="started_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Definition of Dsc Compilation job properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, compilationJobName, resourceGroupName, subscriptionId" /> | Retrieve the Dsc configuration compilation job identified by job id. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of dsc compilation jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, compilationJobName, resourceGroupName, subscriptionId, data__properties" /> | Creates the Dsc compilation job of the configuration. |

## `SELECT` examples

Retrieve a list of dsc compilation jobs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dsc_compilation_jobs', value: 'view', },
        { label: 'dsc_compilation_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
automationAccountName,
compilationJobName,
configuration,
creation_time,
end_time,
exception,
job_id,
last_modified_time,
last_status_modified_time,
parameters,
provisioning_state,
resourceGroupName,
run_on,
start_time,
started_by,
status,
status_details,
subscriptionId
FROM azure.automation.vw_dsc_compilation_jobs
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.automation.dsc_compilation_jobs
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dsc_compilation_jobs</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.automation.dsc_compilation_jobs (
automationAccountName,
compilationJobName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
name,
location,
tags
)
SELECT 
'{{ automationAccountName }}',
'{{ compilationJobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ name }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: configuration
          value:
            - name: name
              value: string
        - name: parameters
          value: object
        - name: incrementNodeConfigurationBuild
          value: boolean
    - name: name
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>
