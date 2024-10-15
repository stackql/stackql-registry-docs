---
title: build_service_supported_buildpacks
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_supported_buildpacks
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

Creates, updates, deletes, gets or lists a <code>build_service_supported_buildpacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build_service_supported_buildpacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_service_supported_buildpacks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_build_service_supported_buildpacks', value: 'view', },
        { label: 'build_service_supported_buildpacks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="buildServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildpackName" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildpack_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Supported buildpack resource properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildServiceName, buildpackName, resourceGroupName, serviceName, subscriptionId" /> | Get the supported buildpack resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Get all supported buildpacks. |

## `SELECT` examples

Get all supported buildpacks.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_build_service_supported_buildpacks', value: 'view', },
        { label: 'build_service_supported_buildpacks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
buildServiceName,
buildpackName,
buildpack_id,
resourceGroupName,
serviceName,
subscriptionId,
version
FROM azure.spring_apps.vw_build_service_supported_buildpacks
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
FROM azure.spring_apps.build_service_supported_buildpacks
WHERE buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

