---
title: build_service_build_results
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_build_results
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

Creates, updates, deletes, gets or lists a <code>build_service_build_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build_service_build_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_service_build_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_build_service_build_results', value: 'view', },
        { label: 'build_service_build_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildName" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildResultName" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="build_pod_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="build_stages" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="image" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Build result resource properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildName, buildResultName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Get a KPack build result. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | List KPack build results. |

## `SELECT` examples

List KPack build results.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_build_service_build_results', value: 'view', },
        { label: 'build_service_build_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
buildName,
buildResultName,
buildServiceName,
build_pod_name,
build_stages,
error,
image,
provisioning_state,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.spring_apps.vw_build_service_build_results
WHERE buildName = '{{ buildName }}'
AND buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.build_service_build_results
WHERE buildName = '{{ buildName }}'
AND buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

