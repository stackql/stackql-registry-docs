---
title: environment_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_definitions
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>environment_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.environment_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_environment_definitions', value: 'view', },
        { label: 'environment_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="environmentDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="template_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="validation_status" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an environment definition. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, devCenterName, environmentDefinitionName, resourceGroupName, subscriptionId" /> | Gets an environment definition from the catalog. |
| <CopyableCode code="get_by_project_catalog" /> | `SELECT` | <CopyableCode code="catalogName, environmentDefinitionName, projectName, resourceGroupName, subscriptionId" /> | Gets an environment definition from the catalog. |
| <CopyableCode code="list_by_catalog" /> | `SELECT` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId" /> | List environment definitions in the catalog. |
| <CopyableCode code="list_by_project_catalog" /> | `SELECT` | <CopyableCode code="catalogName, projectName, resourceGroupName, subscriptionId" /> | Lists the environment definitions in this project catalog. |

## `SELECT` examples

Lists the environment definitions in this project catalog.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_environment_definitions', value: 'view', },
        { label: 'environment_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
catalogName,
devCenterName,
environmentDefinitionName,
parameters,
projectName,
resourceGroupName,
subscriptionId,
template_path,
validation_status
FROM azure.dev_center.vw_environment_definitions
WHERE catalogName = '{{ catalogName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.dev_center.environment_definitions
WHERE catalogName = '{{ catalogName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

