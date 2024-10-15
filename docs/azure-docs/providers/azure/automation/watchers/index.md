---
title: watchers
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers
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

Creates, updates, deletes, gets or lists a <code>watchers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.watchers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_watchers', value: 'view', },
        { label: 'watchers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Gets or sets the etag of the resource. |
| <CopyableCode code="execution_frequency_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="script_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="script_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="script_run_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="watcherName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `string` | Gets or sets the etag of the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Definition of the watcher properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Retrieve the watcher identified by watcher name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of watchers. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Create the watcher identified by watcher name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Delete the watcher by name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Update the watcher identified by watcher name. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Resume the watcher identified by watcher name. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, watcherName" /> | Resume the watcher identified by watcher name. |

## `SELECT` examples

Retrieve a list of watchers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_watchers', value: 'view', },
        { label: 'watchers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
automationAccountName,
creation_time,
etag,
execution_frequency_in_seconds,
last_modified_by,
last_modified_time,
location,
resourceGroupName,
script_name,
script_parameters,
script_run_on,
status,
subscriptionId,
system_data,
tags,
type,
watcherName
FROM azure.automation.vw_watchers
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
etag,
location,
properties,
systemData,
tags,
type
FROM azure.automation.watchers
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>watchers</code> resource.

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
INSERT INTO azure.automation.watchers (
automationAccountName,
resourceGroupName,
subscriptionId,
watcherName,
properties,
etag,
tags,
location
)
SELECT 
'{{ automationAccountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ watcherName }}',
'{{ properties }}',
'{{ etag }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: executionFrequencyInSeconds
          value: integer
        - name: scriptName
          value: string
        - name: scriptParameters
          value: object
        - name: scriptRunOn
          value: string
        - name: status
          value: string
        - name: creationTime
          value: string
        - name: lastModifiedTime
          value: string
        - name: lastModifiedBy
          value: string
        - name: description
          value: string
    - name: etag
      value: string
    - name: tags
      value: object
    - name: location
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>watchers</code> resource.

```sql
/*+ update */
UPDATE azure.automation.watchers
SET 
properties = '{{ properties }}',
name = '{{ name }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```

## `DELETE` example

Deletes the specified <code>watchers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.watchers
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```
