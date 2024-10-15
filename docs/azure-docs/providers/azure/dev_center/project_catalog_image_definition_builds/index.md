---
title: project_catalog_image_definition_builds
hide_title: false
hide_table_of_contents: false
keywords:
  - project_catalog_image_definition_builds
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

Creates, updates, deletes, gets or lists a <code>project_catalog_image_definition_builds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project_catalog_image_definition_builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.project_catalog_image_definition_builds" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_project_catalog_image_definition_builds', value: 'view', },
        { label: 'project_catalog_image_definition_builds', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="buildName" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="imageDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_reference" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an Image Definition Build. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildName, catalogName, imageDefinitionName, projectName, resourceGroupName, subscriptionId" /> | Gets a build for a specified image definition. |
| <CopyableCode code="list_by_image_definition" /> | `SELECT` | <CopyableCode code="catalogName, imageDefinitionName, projectName, resourceGroupName, subscriptionId" /> | Lists builds for a specified image definition. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="buildName, catalogName, imageDefinitionName, projectName, resourceGroupName, subscriptionId" /> | Cancels the specified build for an image definition. |

## `SELECT` examples

Lists builds for a specified image definition.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_project_catalog_image_definition_builds', value: 'view', },
        { label: 'project_catalog_image_definition_builds', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
buildName,
catalogName,
end_time,
error_details,
imageDefinitionName,
image_reference,
projectName,
resourceGroupName,
start_time,
status,
subscriptionId
FROM azure.dev_center.vw_project_catalog_image_definition_builds
WHERE catalogName = '{{ catalogName }}'
AND imageDefinitionName = '{{ imageDefinitionName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.dev_center.project_catalog_image_definition_builds
WHERE catalogName = '{{ catalogName }}'
AND imageDefinitionName = '{{ imageDefinitionName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

