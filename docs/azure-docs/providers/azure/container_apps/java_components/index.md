---
title: java_components
hide_title: false
hide_table_of_contents: false
keywords:
  - java_components
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>java_components</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>java_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.java_components" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_java_components', value: 'view', },
        { label: 'java_components', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="component_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="environmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_binds" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Java Component common properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Creates or updates a Java Component in a Managed Environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Delete a Java Component. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Patches a Java Component using JSON Merge Patch |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_java_components', value: 'view', },
        { label: 'java_components', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
component_type,
configurations,
environmentName,
provisioning_state,
resourceGroupName,
service_binds,
subscriptionId
FROM azure.container_apps.vw_java_components
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_apps.java_components
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>java_components</code> resource.

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
INSERT INTO azure.container_apps.java_components (
environmentName,
name,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ environmentName }}',
'{{ name }}',
'{{ resourceGroupName }}',
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
        - name: componentType
          value: string
        - name: provisioningState
          value: string
        - name: configurations
          value:
            - - name: propertyName
                value: string
              - name: value
                value: string
        - name: serviceBinds
          value:
            - - name: name
                value: string
              - name: serviceId
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>java_components</code> resource.

```sql
/*+ update */
UPDATE azure.container_apps.java_components
SET 
properties = '{{ properties }}'
WHERE 
environmentName = '{{ environmentName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>java_components</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.java_components
WHERE environmentName = '{{ environmentName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
