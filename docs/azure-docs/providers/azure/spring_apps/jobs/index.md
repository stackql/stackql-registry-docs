---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_component_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="template" /> | `text` | field from the `properties` object |
| <CopyableCode code="trigger_config" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Job resource properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, serviceName, subscriptionId" /> | Get a Job and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get the Azure Spring Apps Jobs in a given service |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, serviceName, subscriptionId" /> | Create a new Job or update an exiting Job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete a Job. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, serviceName, subscriptionId" /> |  |

## `SELECT` examples

Get the Azure Spring Apps Jobs in a given service

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
jobName,
managed_component_references,
provisioning_state,
resourceGroupName,
serviceName,
source,
subscriptionId,
template,
trigger_config
FROM azure.spring_apps.vw_jobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.jobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jobs</code> resource.

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
INSERT INTO azure.spring_apps.jobs (
jobName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: template
          value:
            - name: environmentVariables
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
                  - name: secretValue
                    value: string
            - name: args
              value:
                - string
            - name: resourceRequests
              value:
                - name: cpu
                  value: string
                - name: memory
                  value: string
        - name: source
          value:
            - name: type
              value: string
            - name: version
              value: string
        - name: managedComponentReferences
          value: []
        - name: triggerConfig
          value:
            - name: triggerType
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.jobs
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
