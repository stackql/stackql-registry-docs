---
title: data_manager_for_agriculture_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - data_manager_for_agriculture_extensions
  - ag_food_platform
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

Creates, updates, deletes, gets or lists a <code>data_manager_for_agriculture_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_manager_for_agriculture_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.ag_food_platform.data_manager_for_agriculture_extensions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_manager_for_agriculture_extensions', value: 'view', },
        { label: 'data_manager_for_agriculture_extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataManagerForAgricultureExtensionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_api_docs_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_auth_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="farm_beats_extension_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="farm_beats_extension_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="farm_beats_extension_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | DataManagerForAgricultureExtension properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureExtensionId" /> | Get Data Manager For Agriculture extension. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get list of Data Manager For Agriculture extension. |

## `SELECT` examples

Get list of Data Manager For Agriculture extension.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_manager_for_agriculture_extensions', value: 'view', },
        { label: 'data_manager_for_agriculture_extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
dataManagerForAgricultureExtensionId,
detailed_information,
extension_api_docs_link,
extension_auth_link,
extension_category,
farm_beats_extension_id,
farm_beats_extension_name,
farm_beats_extension_version,
publisher_id,
system_data,
target_resource_type
FROM azure_extras.ag_food_platform.vw_data_manager_for_agriculture_extensions
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure_extras.ag_food_platform.data_manager_for_agriculture_extensions
;
```
</TabItem></Tabs>

