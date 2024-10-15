---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
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

Creates, updates, deletes, gets or lists a <code>extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.ag_food_platform.extensions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_extensions', value: 'view', },
        { label: 'extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="additional_api_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataManagerForAgricultureResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="extensionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_api_docs_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_auth_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="installed_extension_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | The ETag value to implement optimistic concurrency. |
| <CopyableCode code="properties" /> | `object` | Extension resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureResourceName, extensionId, resourceGroupName, subscriptionId" /> | Get installed extension details by extension id. |
| <CopyableCode code="list_by_data_manager_for_agriculture" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Get installed extensions details. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataManagerForAgricultureResourceName, extensionId, resourceGroupName, subscriptionId" /> | Install or Update extension. Additional Api Properties are merged patch and if the extension is updated to a new version then the obsolete entries will be auto deleted from Additional Api Properties. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataManagerForAgricultureResourceName, extensionId, resourceGroupName, subscriptionId" /> | Uninstall extension. |

## `SELECT` examples

Get installed extensions details.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_extensions', value: 'view', },
        { label: 'extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
additional_api_properties,
dataManagerForAgricultureResourceName,
e_tag,
extensionId,
extension_api_docs_link,
extension_auth_link,
extension_category,
extension_id,
installed_extension_version,
resourceGroupName,
subscriptionId,
system_data
FROM azure_extras.ag_food_platform.vw_extensions
WHERE dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
eTag,
properties,
systemData
FROM azure_extras.ag_food_platform.extensions
WHERE dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>extensions</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure_extras.ag_food_platform.extensions (
dataManagerForAgricultureResourceName,
extensionId,
resourceGroupName,
subscriptionId,
extensionVersion,
additionalApiProperties
)
SELECT 
'{{ dataManagerForAgricultureResourceName }}',
'{{ extensionId }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ extensionVersion }}',
'{{ additionalApiProperties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: extensionVersion
      value: string
    - name: additionalApiProperties
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>extensions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.ag_food_platform.extensions
WHERE dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND extensionId = '{{ extensionId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
