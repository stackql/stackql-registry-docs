---
title: product_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - product_templates
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>product_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.product_templates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_templates', value: 'view', },
        { label: 'product_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="author" /> | `text` | field from the `properties` object |
| <CopyableCode code="categories" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_product_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_schema_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependencies" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="first_publish_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deprecated" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_publish_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="packaged_content" /> | `text` | field from the `properties` object |
| <CopyableCode code="preview_images" /> | `text` | field from the `properties` object |
| <CopyableCode code="preview_images_dark" /> | `text` | field from the `properties` object |
| <CopyableCode code="providers" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support" /> | `text` | field from the `properties` object |
| <CopyableCode code="templateId" /> | `text` | field from the `properties` object |
| <CopyableCode code="threat_analysis_tactics" /> | `text` | field from the `properties` object |
| <CopyableCode code="threat_analysis_techniques" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Template property bag. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, templateId, workspaceName" /> | Gets a template by its identifier. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all templates in the catalog. |

## `SELECT` examples

Gets all templates in the catalog.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_templates', value: 'view', },
        { label: 'product_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
author,
categories,
content_id,
content_kind,
content_product_id,
content_schema_version,
custom_version,
dependencies,
display_name,
etag,
first_publish_date,
icon,
is_deprecated,
last_publish_date,
package_id,
package_kind,
package_name,
package_version,
packaged_content,
preview_images,
preview_images_dark,
providers,
resourceGroupName,
source,
subscriptionId,
support,
templateId,
threat_analysis_tactics,
threat_analysis_techniques,
version,
workspaceName
FROM azure.sentinel.vw_product_templates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.sentinel.product_templates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

