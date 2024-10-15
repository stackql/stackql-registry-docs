---
title: project_catalog_image_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - project_catalog_image_definitions
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

Creates, updates, deletes, gets or lists a <code>project_catalog_image_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project_catalog_image_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.project_catalog_image_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_project_catalog_image_definitions', value: 'view', },
        { label: 'project_catalog_image_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="imageDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_reference" /> | `text` | field from the `properties` object |
| <CopyableCode code="latest_build" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an Image Definition. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_project_catalog" /> | `SELECT` | <CopyableCode code="catalogName, imageDefinitionName, projectName, resourceGroupName, subscriptionId" /> | Gets an Image Definition from the catalog |
| <CopyableCode code="list_by_project_catalog" /> | `SELECT` | <CopyableCode code="catalogName, projectName, resourceGroupName, subscriptionId" /> | List Image Definitions in the catalog. |
| <CopyableCode code="build_image" /> | `EXEC` | <CopyableCode code="catalogName, imageDefinitionName, projectName, resourceGroupName, subscriptionId" /> | Builds an image for the specified Image Definition. |

## `SELECT` examples

List Image Definitions in the catalog.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_project_catalog_image_definitions', value: 'view', },
        { label: 'project_catalog_image_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
catalogName,
file_url,
imageDefinitionName,
image_reference,
latest_build,
projectName,
resourceGroupName,
subscriptionId
FROM azure.dev_center.vw_project_catalog_image_definitions
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
FROM azure.dev_center.project_catalog_image_definitions
WHERE catalogName = '{{ catalogName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

