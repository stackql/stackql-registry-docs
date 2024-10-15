---
title: variables
hide_title: false
hide_table_of_contents: false
keywords:
  - variables
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

Creates, updates, deletes, gets or lists a <code>variables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.variables" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_variables', value: 'view', },
        { label: 'variables', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_encrypted" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
| <CopyableCode code="variableName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Definition of the variable properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, variableName" /> | Retrieve the variable identified by variable name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of variables. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, variableName, data__name, data__properties" /> | Create a variable. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, variableName" /> | Delete the variable. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, variableName" /> | Update a variable. |

## `SELECT` examples

Retrieve a list of variables.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_variables', value: 'view', },
        { label: 'variables', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
automationAccountName,
creation_time,
is_encrypted,
last_modified_time,
resourceGroupName,
subscriptionId,
value,
variableName
FROM azure.automation.vw_variables
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.automation.variables
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>variables</code> resource.

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
INSERT INTO azure.automation.variables (
automationAccountName,
resourceGroupName,
subscriptionId,
variableName,
data__name,
data__properties,
name,
properties
)
SELECT 
'{{ automationAccountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ variableName }}',
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
        - name: value
          value: string
        - name: description
          value: string
        - name: isEncrypted
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>variables</code> resource.

```sql
/*+ update */
UPDATE azure.automation.variables
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND variableName = '{{ variableName }}';
```

## `DELETE` example

Deletes the specified <code>variables</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.variables
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND variableName = '{{ variableName }}';
```
