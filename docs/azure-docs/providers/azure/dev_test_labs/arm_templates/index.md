---
title: arm_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - arm_templates
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

Creates, updates, deletes, gets or lists a <code>arm_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>arm_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.arm_templates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_arm_templates', value: 'view', },
        { label: 'arm_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifactSourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="contents" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="parameters_value_files_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an Azure Resource Manager template. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifactSourceName, labName, name, resourceGroupName, subscriptionId" /> | Get azure resource manager template. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="artifactSourceName, labName, resourceGroupName, subscriptionId" /> | List azure resource manager templates in a given artifact source. |

## `SELECT` examples

List azure resource manager templates in a given artifact source.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_arm_templates', value: 'view', },
        { label: 'arm_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
artifactSourceName,
contents,
created_date,
display_name,
enabled,
icon,
labName,
location,
parameters_value_files_info,
publisher,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.dev_test_labs.vw_arm_templates
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
FROM azure.dev_test_labs.arm_templates
WHERE artifactSourceName = '{{ artifactSourceName }}'
AND labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

