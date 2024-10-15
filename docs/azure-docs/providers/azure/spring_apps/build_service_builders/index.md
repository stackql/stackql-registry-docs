---
title: build_service_builders
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_builders
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

Creates, updates, deletes, gets or lists a <code>build_service_builders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build_service_builders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_service_builders" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_build_service_builders', value: 'view', },
        { label: 'build_service_builders', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="buildServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="builderName" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildpack_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="stack" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | KPack Builder properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId" /> | Get a KPack builder. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | List KPack builders result. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId" /> | Create or update a KPack builder. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId" /> | Delete a KPack builder. |

## `SELECT` examples

List KPack builders result.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_build_service_builders', value: 'view', },
        { label: 'build_service_builders', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
buildServiceName,
builderName,
buildpack_groups,
provisioning_state,
resourceGroupName,
serviceName,
stack,
subscriptionId
FROM azure.spring_apps.vw_build_service_builders
WHERE buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.build_service_builders
WHERE buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>build_service_builders</code> resource.

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
INSERT INTO azure.spring_apps.build_service_builders (
buildServiceName,
builderName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ buildServiceName }}',
'{{ builderName }}',
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
        - name: provisioningState
          value: string
        - name: stack
          value:
            - name: id
              value: string
            - name: version
              value: string
        - name: buildpackGroups
          value:
            - - name: name
                value: string
              - name: buildpacks
                value:
                  - - name: id
                      value: string
                    - name: version
                      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>build_service_builders</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.build_service_builders
WHERE buildServiceName = '{{ buildServiceName }}'
AND builderName = '{{ builderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
