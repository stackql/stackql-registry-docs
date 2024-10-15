---
title: workflow_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_versions
  - app_service
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

Creates, updates, deletes, gets or lists a <code>workflow_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.workflow_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_versions', value: 'view', },
        { label: 'workflow_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="access_control" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="changed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="integration_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="versionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workflowName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The workflow version properties. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, versionId, workflowName" /> | Gets a workflow version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, workflowName" /> | Gets a list of workflow versions. |

## `SELECT` examples

Gets a list of workflow versions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflow_versions', value: 'view', },
        { label: 'workflow_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
access_control,
access_endpoint,
changed_time,
created_time,
definition,
endpoints_configuration,
integration_account,
location,
parameters,
provisioning_state,
resourceGroupName,
sku,
state,
subscriptionId,
tags,
type,
version,
versionId,
workflowName
FROM azure.app_service.vw_workflow_versions
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.app_service.workflow_versions
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```
</TabItem></Tabs>

