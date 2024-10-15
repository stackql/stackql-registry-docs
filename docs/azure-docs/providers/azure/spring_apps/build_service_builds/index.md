---
title: build_service_builds
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_builds
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

Creates, updates, deletes, gets or lists a <code>build_service_builds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build_service_builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_service_builds" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_build_service_builds', value: 'view', },
        { label: 'build_service_builds', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agent_pool" /> | `text` | field from the `properties` object |
| <CopyableCode code="apms" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildName" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="builder" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="env" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="relative_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="triggered_build_result" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Build resource properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Get a KPack build. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | List KPack builds. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Create or update a KPack build. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | delete a KPack build. |

## `SELECT` examples

List KPack builds.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_build_service_builds', value: 'view', },
        { label: 'build_service_builds', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
agent_pool,
apms,
buildName,
buildServiceName,
builder,
certificates,
env,
provisioning_state,
relative_path,
resourceGroupName,
resource_requests,
serviceName,
subscriptionId,
triggered_build_result
FROM azure.spring_apps.vw_build_service_builds
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
FROM azure.spring_apps.build_service_builds
WHERE buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>build_service_builds</code> resource.

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
INSERT INTO azure.spring_apps.build_service_builds (
buildName,
buildServiceName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ buildName }}',
'{{ buildServiceName }}',
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
        - name: relativePath
          value: string
        - name: builder
          value: string
        - name: agentPool
          value: string
        - name: provisioningState
          value: string
        - name: env
          value: object
        - name: apms
          value: []
        - name: certificates
          value: []
        - name: triggeredBuildResult
          value:
            - name: id
              value: string
            - name: provisioningState
              value: string
            - name: image
              value: string
            - name: lastTransitionTime
              value: string
            - name: lastTransitionReason
              value: string
            - name: lastTransitionStatus
              value: string
        - name: resourceRequests
          value:
            - name: cpu
              value: string
            - name: memory
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>build_service_builds</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.build_service_builds
WHERE buildName = '{{ buildName }}'
AND buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
