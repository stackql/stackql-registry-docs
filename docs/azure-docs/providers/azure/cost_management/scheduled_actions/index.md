---
title: scheduled_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>scheduled_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.scheduled_actions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scheduled_actions', value: 'view', },
        { label: 'scheduled_actions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of the scheduled action. |
| <CopyableCode code="notification" /> | `text` | field from the `properties` object |
| <CopyableCode code="notification_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="view_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | Resource Etag. For update calls, eTag is optional and can be specified to achieve optimistic concurrency. Fetch the resource's eTag by doing a 'GET' call first and then including the latest eTag as part of the request body or 'If-Match' header while performing the update. For create calls, eTag is not required. |
| <CopyableCode code="kind" /> | `string` | Kind of the scheduled action. |
| <CopyableCode code="properties" /> | `object` | The properties of the scheduled action. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> | Get the private scheduled action by name. |
| <CopyableCode code="get_by_scope" /> | `SELECT` | <CopyableCode code="name, scope" /> | Get the shared scheduled action from the given scope by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | List all private scheduled actions. |
| <CopyableCode code="list_by_scope" /> | `SELECT` | <CopyableCode code="scope" /> | List all shared scheduled actions within the given scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name" /> | Create or update a private scheduled action. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name" /> | Delete a private scheduled action. |
| <CopyableCode code="delete_by_scope" /> | `DELETE` | <CopyableCode code="name, scope" /> | Delete a scheduled action within the given scope. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="" /> | Checks availability and correctness of the name for a scheduled action. |
| <CopyableCode code="check_name_availability_by_scope" /> | `EXEC` | <CopyableCode code="scope" /> | Checks availability and correctness of the name for a scheduled action within the given scope. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="name" /> | Processes a private scheduled action. |
| <CopyableCode code="run_by_scope" /> | `EXEC` | <CopyableCode code="name, scope" /> | Runs a shared scheduled action within the given scope. |

## `SELECT` examples

List all private scheduled actions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scheduled_actions', value: 'view', },
        { label: 'scheduled_actions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
display_name,
e_tag,
file_destination,
kind,
notification,
notification_email,
schedule,
scope,
status,
system_data,
view_id
FROM azure.cost_management.vw_scheduled_actions
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
eTag,
kind,
properties,
systemData
FROM azure.cost_management.scheduled_actions
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scheduled_actions</code> resource.

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
INSERT INTO azure.cost_management.scheduled_actions (
name,
kind,
systemData,
properties
)
SELECT 
'{{ name }}',
'{{ kind }}',
'{{ systemData }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: eTag
      value: string
    - name: kind
      value: []
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
    - name: properties
      value:
        - name: displayName
          value: string
        - name: fileDestination
          value:
            - name: fileFormats
              value:
                - []
        - name: notification
          value:
            - name: to
              value:
                - string
            - name: language
              value: []
            - name: message
              value: string
            - name: regionalFormat
              value: []
            - name: subject
              value: string
        - name: notificationEmail
          value: []
        - name: schedule
          value:
            - name: frequency
              value: []
            - name: hourOfDay
              value: integer
            - name: daysOfWeek
              value:
                - []
            - name: weeksOfMonth
              value:
                - []
            - name: dayOfMonth
              value: integer
            - name: startDate
              value: string
            - name: endDate
              value: string
        - name: scope
          value: string
        - name: status
          value: []
        - name: viewId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>scheduled_actions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cost_management.scheduled_actions
WHERE name = '{{ name }}';
```
