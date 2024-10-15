---
title: best_practices
hide_title: false
hide_table_of_contents: false
keywords:
  - best_practices
  - automanage
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

Creates, updates, deletes, gets or lists a <code>best_practices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>best_practices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.best_practices" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_best_practices', value: 'view', },
        { label: 'best_practices', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The fully qualified ID for the best practice.  For example, /providers/Microsoft.Automanage/bestPractices/azureBestPracticesProduction |
| <CopyableCode code="name" /> | `text` | The name of the best practice. For example, azureBestPracticesProduction |
| <CopyableCode code="bestPracticeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource.  For example, Microsoft.Automanage/bestPractices |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID for the best practice.  For example, /providers/Microsoft.Automanage/bestPractices/azureBestPracticesProduction |
| <CopyableCode code="name" /> | `string` | The name of the best practice. For example, azureBestPracticesProduction |
| <CopyableCode code="properties" /> | `object` | Automanage configuration profile properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource.  For example, Microsoft.Automanage/bestPractices |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bestPracticeName" /> | Get information about a Automanage best practice |
| <CopyableCode code="list_by_tenant" /> | `SELECT` | <CopyableCode code="" /> | Retrieve a list of Automanage best practices |

## `SELECT` examples

Retrieve a list of Automanage best practices

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_best_practices', value: 'view', },
        { label: 'best_practices', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
bestPracticeName,
configuration,
system_data,
type
FROM azure.automanage.vw_best_practices
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.automanage.best_practices
;
```
</TabItem></Tabs>

