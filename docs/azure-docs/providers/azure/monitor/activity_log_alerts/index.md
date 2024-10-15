---
title: activity_log_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - activity_log_alerts
  - monitor
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

Creates, updates, deletes, gets or lists a <code>activity_log_alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>activity_log_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.activity_log_alerts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_activity_log_alerts', value: 'view', },
        { label: 'activity_log_alerts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource Id. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="activityLogAlertName" /> | `text` | field from the `properties` object |
| <CopyableCode code="condition" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. Azure Activity Log Alert rules are supported on Global, West Europe and North Europe regions. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource Id. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. Azure Activity Log Alert rules are supported on Global, West Europe and North Europe regions. |
| <CopyableCode code="properties" /> | `object` | An Azure Activity Log Alert rule. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activityLogAlertName, resourceGroupName, subscriptionId" /> | Get an Activity Log Alert rule. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of all Activity Log Alert rules in a resource group. |
| <CopyableCode code="list_by_subscription_id" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of all Activity Log Alert rules in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="activityLogAlertName, resourceGroupName, subscriptionId" /> | Create a new Activity Log Alert rule or update an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="activityLogAlertName, resourceGroupName, subscriptionId" /> | Delete an Activity Log Alert rule. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="activityLogAlertName, resourceGroupName, subscriptionId" /> | Updates 'tags' and 'enabled' fields in an existing Alert rule. This method is used to update the Alert rule tags, and to enable or disable the Alert rule. To update other fields use CreateOrUpdate operation. |

## `SELECT` examples

Get a list of all Activity Log Alert rules in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_activity_log_alerts', value: 'view', },
        { label: 'activity_log_alerts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
actions,
activityLogAlertName,
condition,
enabled,
location,
resourceGroupName,
scopes,
subscriptionId,
tags,
type
FROM azure.monitor.vw_activity_log_alerts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.monitor.activity_log_alerts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>activity_log_alerts</code> resource.

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
INSERT INTO azure.monitor.activity_log_alerts (
activityLogAlertName,
resourceGroupName,
subscriptionId,
location,
tags,
properties
)
SELECT 
'{{ activityLogAlertName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: scopes
          value:
            - string
        - name: condition
          value:
            - name: allOf
              value:
                - - name: field
                    value: string
                  - name: equals
                    value: string
                  - name: containsAny
                    value:
                      - string
                  - name: anyOf
                    value:
                      - - name: field
                          value: string
                        - name: equals
                          value: string
                        - name: containsAny
                          value:
                            - string
        - name: actions
          value:
            - name: actionGroups
              value:
                - - name: actionGroupId
                    value: string
                  - name: webhookProperties
                    value: string
        - name: enabled
          value: boolean
        - name: description
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>activity_log_alerts</code> resource.

```sql
/*+ update */
UPDATE azure.monitor.activity_log_alerts
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
activityLogAlertName = '{{ activityLogAlertName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>activity_log_alerts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.activity_log_alerts
WHERE activityLogAlertName = '{{ activityLogAlertName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
