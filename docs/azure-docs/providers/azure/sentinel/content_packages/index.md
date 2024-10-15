---
title: content_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - content_packages
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

Creates, updates, deletes, gets or lists a <code>content_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>content_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.content_packages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_content_packages', value: 'view', },
        { label: 'content_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="author" /> | `text` | field from the `properties` object |
| <CopyableCode code="categories" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_product_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_schema_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependencies" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="first_publish_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deprecated" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_featured" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_new" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_preview" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_publish_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="packageId" /> | `text` | field from the `properties` object |
| <CopyableCode code="providers" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support" /> | `text` | field from the `properties` object |
| <CopyableCode code="threat_analysis_tactics" /> | `text` | field from the `properties` object |
| <CopyableCode code="threat_analysis_techniques" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes package properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packageId, resourceGroupName, subscriptionId, workspaceName" /> | Gets an installed packages by its id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all installed packages. |
| <CopyableCode code="install" /> | `EXEC` | <CopyableCode code="packageId, resourceGroupName, subscriptionId, workspaceName" /> | Install a package to the workspace. |
| <CopyableCode code="uninstall" /> | `EXEC` | <CopyableCode code="packageId, resourceGroupName, subscriptionId, workspaceName" /> | Uninstall a package from the workspace. |

## `SELECT` examples

Gets all installed packages.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_content_packages', value: 'view', },
        { label: 'content_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
author,
categories,
content_id,
content_kind,
content_product_id,
content_schema_version,
dependencies,
display_name,
etag,
first_publish_date,
icon,
is_deprecated,
is_featured,
is_new,
is_preview,
last_publish_date,
packageId,
providers,
publisher_display_name,
resourceGroupName,
source,
subscriptionId,
support,
threat_analysis_tactics,
threat_analysis_techniques,
version,
workspaceName
FROM azure.sentinel.vw_content_packages
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
FROM azure.sentinel.content_packages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

