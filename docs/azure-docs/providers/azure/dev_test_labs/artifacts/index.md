---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
  - dev_test_labs
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

Creates, updates, deletes, gets or lists a <code>artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.artifacts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_artifacts', value: 'view', },
        { label: 'artifacts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifactSourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="target_os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an artifact. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifactSourceName, labName, name, resourceGroupName, subscriptionId" /> | Get artifact. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="artifactSourceName, labName, resourceGroupName, subscriptionId" /> | List artifacts in a given artifact source. |
| <CopyableCode code="generate_arm_template" /> | `EXEC` | <CopyableCode code="artifactSourceName, labName, name, resourceGroupName, subscriptionId" /> | Generates an ARM template for the given artifact, uploads the required files to a storage account, and validates the generated artifact. |

## `SELECT` examples

List artifacts in a given artifact source.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_artifacts', value: 'view', },
        { label: 'artifacts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
artifactSourceName,
created_date,
file_path,
icon,
labName,
location,
parameters,
publisher,
resourceGroupName,
subscriptionId,
tags,
target_os_type,
title,
type
FROM azure.dev_test_labs.vw_artifacts
WHERE artifactSourceName = '{{ artifactSourceName }}'
AND labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.dev_test_labs.artifacts
WHERE artifactSourceName = '{{ artifactSourceName }}'
AND labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

