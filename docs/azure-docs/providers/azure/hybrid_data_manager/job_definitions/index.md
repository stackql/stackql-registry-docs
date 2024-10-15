---
title: job_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_definitions
  - hybrid_data_manager
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

Creates, updates, deletes, gets or lists a <code>job_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.job_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_definitions', value: 'view', },
        { label: 'job_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the object. |
| <CopyableCode code="name" /> | `text` | Name of the object. |
| <CopyableCode code="customer_secrets" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_service_input" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_sink_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedules" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the object. |
| <CopyableCode code="user_confirmation" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="properties" /> | `object` | Job Definition |
| <CopyableCode code="type" /> | `string` | Type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId" /> | This method gets job definition object by name. |
| <CopyableCode code="list_by_data_manager" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | This method gets all the job definitions of the given data manager resource. |
| <CopyableCode code="list_by_data_service" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, resourceGroupName, subscriptionId" /> | This method gets all the job definitions of the given data service name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a job definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId" /> | This method deletes the given job definition. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId" /> | This method runs a job instance of the given job definition. |

## `SELECT` examples

This method gets all the job definitions of the given data manager resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_definitions', value: 'view', },
        { label: 'job_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
customer_secrets,
dataManagerName,
dataServiceName,
data_service_input,
data_sink_id,
data_source_id,
jobDefinitionName,
last_modified_time,
resourceGroupName,
run_location,
schedules,
state,
subscriptionId,
type,
user_confirmation
FROM azure.hybrid_data_manager.vw_job_definitions
WHERE dataManagerName = '{{ dataManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.hybrid_data_manager.job_definitions
WHERE dataManagerName = '{{ dataManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_definitions</code> resource.

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
INSERT INTO azure.hybrid_data_manager.job_definitions (
dataManagerName,
dataServiceName,
jobDefinitionName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ dataManagerName }}',
'{{ dataServiceName }}',
'{{ jobDefinitionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: dataSourceId
          value: string
        - name: dataSinkId
          value: string
        - name: schedules
          value:
            - - name: name
                value: string
              - name: policyList
                value:
                  - string
        - name: state
          value: string
        - name: lastModifiedTime
          value: string
        - name: runLocation
          value: string
        - name: userConfirmation
          value: string
        - name: dataServiceInput
          value: object
        - name: customerSecrets
          value:
            - - name: keyIdentifier
                value: string
              - name: keyValue
                value: string
              - name: algorithm
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>job_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_data_manager.job_definitions
WHERE dataManagerName = '{{ dataManagerName }}'
AND dataServiceName = '{{ dataServiceName }}'
AND jobDefinitionName = '{{ jobDefinitionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
