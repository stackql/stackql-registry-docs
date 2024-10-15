---
title: buildpack_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - buildpack_bindings
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

Creates, updates, deletes, gets or lists a <code>buildpack_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buildpack_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.buildpack_bindings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_buildpack_bindings', value: 'view', },
        { label: 'buildpack_bindings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="binding_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="builderName" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildpackBindingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="launch_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a buildpack binding |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId" /> | Get a buildpack binding by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all buildpack bindings in a builder. |
| <CopyableCode code="list_for_cluster" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get collection of buildpack bindings under all builders. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId" /> | Create or update a buildpack binding. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete a Buildpack Binding |

## `SELECT` examples

Get collection of buildpack bindings under all builders.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_buildpack_bindings', value: 'view', },
        { label: 'buildpack_bindings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
binding_type,
buildServiceName,
builderName,
buildpackBindingName,
launch_properties,
provisioning_state,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.spring_apps.vw_buildpack_bindings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.buildpack_bindings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>buildpack_bindings</code> resource.

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
INSERT INTO azure.spring_apps.buildpack_bindings (
buildServiceName,
builderName,
buildpackBindingName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ buildServiceName }}',
'{{ builderName }}',
'{{ buildpackBindingName }}',
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
        - name: bindingType
          value: string
        - name: provisioningState
          value: string
        - name: launchProperties
          value:
            - name: properties
              value: object
            - name: secrets
              value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>buildpack_bindings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.buildpack_bindings
WHERE buildServiceName = '{{ buildServiceName }}'
AND builderName = '{{ builderName }}'
AND buildpackBindingName = '{{ buildpackBindingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
