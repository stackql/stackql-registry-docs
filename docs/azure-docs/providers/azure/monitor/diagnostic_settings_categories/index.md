---
title: diagnostic_settings_categories
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_settings_categories
  - monitor
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

Creates, updates, deletes, gets or lists a <code>diagnostic_settings_categories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>diagnostic_settings_categories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.diagnostic_settings_categories" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostic_settings_categories', value: 'view', },
        { label: 'diagnostic_settings_categories', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="category_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="category_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The diagnostic settings Category. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceUri" /> | Gets the diagnostic settings category for the specified resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Lists the diagnostic settings categories for the specified resource. |

## `SELECT` examples

Lists the diagnostic settings categories for the specified resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostic_settings_categories', value: 'view', },
        { label: 'diagnostic_settings_categories', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
category_groups,
category_type,
location,
resourceUri,
system_data,
tags,
type
FROM azure.monitor.vw_diagnostic_settings_categories
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
tags,
type
FROM azure.monitor.diagnostic_settings_categories
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>

