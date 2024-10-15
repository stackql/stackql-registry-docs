---
title: rai_blocklist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_blocklist_items
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>rai_blocklist_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rai_blocklist_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.rai_blocklist_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_rai_blocklist_items', value: 'view', },
        { label: 'rai_blocklist_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="is_regex" /> | `text` | field from the `properties` object |
| <CopyableCode code="pattern" /> | `text` | field from the `properties` object |
| <CopyableCode code="raiBlocklistItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="raiBlocklistName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | RAI Custom Blocklist Item properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, raiBlocklistItemName, raiBlocklistName, resourceGroupName, subscriptionId" /> | Gets the specified custom blocklist Item associated with the custom blocklist. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, raiBlocklistName, resourceGroupName, subscriptionId" /> | Gets the blocklist items associated with the custom blocklist. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, raiBlocklistItemName, raiBlocklistName, resourceGroupName, subscriptionId" /> | Update the state of specified blocklist item associated with the Azure OpenAI account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, raiBlocklistItemName, raiBlocklistName, resourceGroupName, subscriptionId" /> | Deletes the specified blocklist Item associated with the custom blocklist. |
| <CopyableCode code="batch_add" /> | `EXEC` | <CopyableCode code="accountName, raiBlocklistName, resourceGroupName, subscriptionId" /> | Batch operation to add blocklist items. |
| <CopyableCode code="batch_delete" /> | `EXEC` | <CopyableCode code="accountName, raiBlocklistName, resourceGroupName, subscriptionId" /> | Batch operation to delete blocklist items. |

## `SELECT` examples

Gets the blocklist items associated with the custom blocklist.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_rai_blocklist_items', value: 'view', },
        { label: 'rai_blocklist_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
etag,
is_regex,
pattern,
raiBlocklistItemName,
raiBlocklistName,
resourceGroupName,
subscriptionId,
system_data,
tags
FROM azure.cognitive_services.vw_rai_blocklist_items
WHERE accountName = '{{ accountName }}'
AND raiBlocklistName = '{{ raiBlocklistName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties,
systemData,
tags
FROM azure.cognitive_services.rai_blocklist_items
WHERE accountName = '{{ accountName }}'
AND raiBlocklistName = '{{ raiBlocklistName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rai_blocklist_items</code> resource.

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
INSERT INTO azure.cognitive_services.rai_blocklist_items (
accountName,
raiBlocklistItemName,
raiBlocklistName,
resourceGroupName,
subscriptionId,
tags,
properties
)
SELECT 
'{{ accountName }}',
'{{ raiBlocklistItemName }}',
'{{ raiBlocklistName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: etag
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: pattern
          value: string
        - name: isRegex
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>rai_blocklist_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cognitive_services.rai_blocklist_items
WHERE accountName = '{{ accountName }}'
AND raiBlocklistItemName = '{{ raiBlocklistItemName }}'
AND raiBlocklistName = '{{ raiBlocklistName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
