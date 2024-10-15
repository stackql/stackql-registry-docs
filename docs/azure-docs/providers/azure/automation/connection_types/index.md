---
title: connection_types
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_types
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

Creates, updates, deletes, gets or lists a <code>connection_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.connection_types" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connection_types', value: 'view', },
        { label: 'connection_types', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets the id of the resource. |
| <CopyableCode code="name" /> | `text` | Gets the name of the connection type. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionTypeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="field_definitions" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_global" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets the name of the connection type. |
| <CopyableCode code="properties" /> | `object` | Properties of the connection type. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, connectionTypeName, resourceGroupName, subscriptionId" /> | Retrieve the connection type identified by connection type name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of connection types. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, connectionTypeName, resourceGroupName, subscriptionId, data__name, data__properties" /> | Create a connection type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, connectionTypeName, resourceGroupName, subscriptionId" /> | Delete the connection type. |

## `SELECT` examples

Retrieve a list of connection types.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connection_types', value: 'view', },
        { label: 'connection_types', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
automationAccountName,
connectionTypeName,
creation_time,
field_definitions,
is_global,
last_modified_time,
resourceGroupName,
subscriptionId,
type
FROM azure.automation.vw_connection_types
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
properties,
type
FROM azure.automation.connection_types
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connection_types</code> resource.

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
INSERT INTO azure.automation.connection_types (
automationAccountName,
connectionTypeName,
resourceGroupName,
subscriptionId,
data__name,
data__properties,
name,
properties
)
SELECT 
'{{ automationAccountName }}',
'{{ connectionTypeName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__name }}',
'{{ data__properties }}',
'{{ name }}',
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
    - name: properties
      value:
        - name: isGlobal
          value: boolean
        - name: fieldDefinitions
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>connection_types</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.connection_types
WHERE automationAccountName = '{{ automationAccountName }}'
AND connectionTypeName = '{{ connectionTypeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
