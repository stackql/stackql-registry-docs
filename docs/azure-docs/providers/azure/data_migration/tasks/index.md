---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.tasks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tasks', value: 'view', },
        { label: 'tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="client_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="commands" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | HTTP strong entity tag value. This is ignored if submitted. |
| <CopyableCode code="groupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="taskName" /> | `text` | field from the `properties` object |
| <CopyableCode code="task_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | HTTP strong entity tag value. This is ignored if submitted. |
| <CopyableCode code="properties" /> | `object` | Base class for all types of DMS (classic) task properties. If task is not supported by current client, this object is returned. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId, taskName" /> | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The GET method retrieves information about a task. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId, taskName" /> | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PUT method creates a new task or updates an existing one, although since tasks have no mutable custom properties, there is little reason to update an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId, taskName" /> | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The DELETE method deletes a task, canceling it first if it's running. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId, taskName" /> | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PATCH method updates an existing task, but since tasks have no mutable custom properties, there is little reason to do so. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId, taskName" /> | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. This method cancels a task if it's currently queued or running. |
| <CopyableCode code="command" /> | `EXEC` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId, taskName, data__commandType" /> | The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. This method executes a command on a running task. |

## `SELECT` examples

The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tasks', value: 'view', },
        { label: 'tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
client_data,
commands,
errors,
etag,
groupName,
projectName,
serviceName,
state,
subscriptionId,
system_data,
taskName,
task_type,
type
FROM azure.data_migration.vw_tasks
WHERE groupName = '{{ groupName }}'
AND projectName = '{{ projectName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.data_migration.tasks
WHERE groupName = '{{ groupName }}'
AND projectName = '{{ projectName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tasks</code> resource.

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
INSERT INTO azure.data_migration.tasks (
groupName,
projectName,
serviceName,
subscriptionId,
taskName,
etag,
properties
)
SELECT 
'{{ groupName }}',
'{{ projectName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ taskName }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: taskType
          value: string
        - name: errors
          value:
            - - name: code
                value: string
              - name: message
                value: string
              - name: details
                value:
                  - - name: code
                      value: string
                    - name: message
                      value: string
                    - name: details
                      value:
                        - - name: code
                            value: string
                          - name: message
                            value: string
                          - name: details
                            value:
                              - - name: code
                                  value: string
                                - name: message
                                  value: string
                                - name: details
                                  value:
                                    - - name: code
                                        value: string
                                      - name: message
                                        value: string
                                      - name: details
                                        value:
                                          - - name: code
                                              value: string
                                            - name: message
                                              value: string
                                            - name: details
                                              value:
                                                - - name: code
                                                    value: string
                                                  - name: message
                                                    value: string
                                                  - name: details
                                                    value:
                                                      - - name: code
                                                          value: string
                                                        - name: message
                                                          value: string
                                                        - name: details
                                                          value:
                                                            - - name: code
                                                                value: string
                                                              - name: message
                                                                value: string
                                                              - name: details
                                                                value:
                                                                  - []
        - name: state
          value: string
        - name: commands
          value:
            - - name: commandType
                value: string
              - name: errors
                value:
                  - - name: code
                      value: string
                    - name: message
                      value: string
                    - name: details
                      value:
                        - - name: code
                            value: string
                          - name: message
                            value: string
                          - name: details
                            value:
                              - - name: code
                                  value: string
                                - name: message
                                  value: string
                                - name: details
                                  value:
                                    - - name: code
                                        value: string
                                      - name: message
                                        value: string
                                      - name: details
                                        value:
                                          - - name: code
                                              value: string
                                            - name: message
                                              value: string
                                            - name: details
                                              value:
                                                - - name: code
                                                    value: string
                                                  - name: message
                                                    value: string
                                                  - name: details
                                                    value:
                                                      - - name: code
                                                          value: string
                                                        - name: message
                                                          value: string
                                                        - name: details
                                                          value:
                                                            - - name: code
                                                                value: string
                                                              - name: message
                                                                value: string
                                                              - name: details
                                                                value:
                                                                  - []
              - name: state
                value: string
        - name: clientData
          value: object
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tasks</code> resource.

```sql
/*+ update */
UPDATE azure.data_migration.tasks
SET 
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
groupName = '{{ groupName }}'
AND projectName = '{{ projectName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND taskName = '{{ taskName }}';
```

## `DELETE` example

Deletes the specified <code>tasks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_migration.tasks
WHERE groupName = '{{ groupName }}'
AND projectName = '{{ projectName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND taskName = '{{ taskName }}';
```
