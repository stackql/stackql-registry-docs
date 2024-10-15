---
title: bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - bindings
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

Creates, updates, deletes, gets or lists a <code>bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.bindings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bindings', value: 'view', },
        { label: 'bindings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appName" /> | `text` | field from the `properties` object |
| <CopyableCode code="bindingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="binding_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="generated_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="key" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_at" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Binding resource properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, bindingName, resourceGroupName, serviceName, subscriptionId" /> | Get a Binding and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in an App. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="appName, bindingName, resourceGroupName, serviceName, subscriptionId" /> | Create a new Binding or update an exiting Binding. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, bindingName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete a Binding. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="appName, bindingName, resourceGroupName, serviceName, subscriptionId" /> | Operation to update an exiting Binding. |

## `SELECT` examples

Handles requests to list all resources in an App.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bindings', value: 'view', },
        { label: 'bindings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
appName,
bindingName,
binding_parameters,
created_at,
generated_properties,
key,
resourceGroupName,
resource_id,
resource_name,
resource_type,
serviceName,
subscriptionId,
updated_at
FROM azure.spring_apps.vw_bindings
WHERE appName = '{{ appName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.bindings
WHERE appName = '{{ appName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bindings</code> resource.

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
INSERT INTO azure.spring_apps.bindings (
appName,
bindingName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ appName }}',
'{{ bindingName }}',
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
        - name: resourceName
          value: string
        - name: resourceType
          value: string
        - name: resourceId
          value: string
        - name: key
          value: string
        - name: bindingParameters
          value: object
        - name: generatedProperties
          value: string
        - name: createdAt
          value: string
        - name: updatedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>bindings</code> resource.

```sql
/*+ update */
UPDATE azure.spring_apps.bindings
SET 
properties = '{{ properties }}'
WHERE 
appName = '{{ appName }}'
AND bindingName = '{{ bindingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>bindings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.bindings
WHERE appName = '{{ appName }}'
AND bindingName = '{{ bindingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
