---
title: metric_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_alerts
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

Creates, updates, deletes, gets or lists a <code>metric_alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.metric_alerts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_metric_alerts', value: 'view', },
        { label: 'metric_alerts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_mitigate" /> | `text` | field from the `properties` object |
| <CopyableCode code="criteria" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="evaluation_frequency" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_migrated" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="target_resource_region" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
| <CopyableCode code="window_size" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | An alert rule. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> | Retrieve an alert rule definition. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieve alert rule definitions in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieve alert rule definitions in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId, data__properties" /> | Create or update an metric alert definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> | Delete an alert rule definition. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> | Update an metric alert definition. |

## `SELECT` examples

Retrieve alert rule definitions in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_metric_alerts', value: 'view', },
        { label: 'metric_alerts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
actions,
auto_mitigate,
criteria,
enabled,
evaluation_frequency,
is_migrated,
last_updated_time,
location,
resourceGroupName,
ruleName,
scopes,
severity,
subscriptionId,
system_data,
tags,
target_resource_region,
target_resource_type,
type,
window_size
FROM azure.monitor.vw_metric_alerts
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
systemData,
tags,
type
FROM azure.monitor.metric_alerts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metric_alerts</code> resource.

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
INSERT INTO azure.monitor.metric_alerts (
resourceGroupName,
ruleName,
subscriptionId,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ ruleName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: description
          value: string
        - name: severity
          value: integer
        - name: enabled
          value: boolean
        - name: scopes
          value:
            - string
        - name: evaluationFrequency
          value: string
        - name: windowSize
          value: string
        - name: targetResourceType
          value: string
        - name: targetResourceRegion
          value: string
        - name: criteria
          value:
            - name: odata.type
              value: string
        - name: autoMitigate
          value: boolean
        - name: actions
          value:
            - - name: actionGroupId
                value: string
              - name: webHookProperties
                value: object
        - name: lastUpdatedTime
          value: string
        - name: isMigrated
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>metric_alerts</code> resource.

```sql
/*+ update */
UPDATE azure.monitor.metric_alerts
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND ruleName = '{{ ruleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>metric_alerts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.metric_alerts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND ruleName = '{{ ruleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
