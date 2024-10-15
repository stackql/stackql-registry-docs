---
title: activities
hide_title: false
hide_table_of_contents: false
keywords:
  - activities
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

Creates, updates, deletes, gets or lists a <code>activities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.activities" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_activities', value: 'view', },
        { label: 'activities', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the id of the resource. |
| <CopyableCode code="name" /> | `text` | Gets the name of the activity. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="activityName" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="moduleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameter_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets the name of the activity. |
| <CopyableCode code="properties" /> | `object` | Properties of the activity. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activityName, automationAccountName, moduleName, resourceGroupName, subscriptionId" /> | Retrieve the activity in the module identified by module name and activity name. |
| <CopyableCode code="list_by_module" /> | `SELECT` | <CopyableCode code="automationAccountName, moduleName, resourceGroupName, subscriptionId" /> | Retrieve a list of activities in the module identified by module name. |

## `SELECT` examples

Retrieve a list of activities in the module identified by module name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_activities', value: 'view', },
        { label: 'activities', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
activityName,
automationAccountName,
creation_time,
definition,
last_modified_time,
moduleName,
output_types,
parameter_sets,
resourceGroupName,
subscriptionId
FROM azure.automation.vw_activities
WHERE automationAccountName = '{{ automationAccountName }}'
AND moduleName = '{{ moduleName }}'
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
FROM azure.automation.activities
WHERE automationAccountName = '{{ automationAccountName }}'
AND moduleName = '{{ moduleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

