---
title: rai_blocklists
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_blocklists
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

Creates, updates, deletes, gets or lists a <code>rai_blocklists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rai_blocklists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.rai_blocklists" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_rai_blocklists', value: 'view', },
        { label: 'rai_blocklists', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
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
| <CopyableCode code="properties" /> | `object` | RAI Custom Blocklist properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, raiBlocklistName, resourceGroupName, subscriptionId" /> | Gets the specified custom blocklist associated with the Azure OpenAI account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the custom blocklists associated with the Azure OpenAI account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, raiBlocklistName, resourceGroupName, subscriptionId" /> | Update the state of specified blocklist associated with the Azure OpenAI account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, raiBlocklistName, resourceGroupName, subscriptionId" /> | Deletes the specified custom blocklist associated with the Azure OpenAI account. |

## `SELECT` examples

Gets the custom blocklists associated with the Azure OpenAI account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_rai_blocklists', value: 'view', },
        { label: 'rai_blocklists', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accountName,
etag,
raiBlocklistName,
resourceGroupName,
subscriptionId,
system_data,
tags
FROM azure.cognitive_services.vw_rai_blocklists
WHERE accountName = '{{ accountName }}'
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
FROM azure.cognitive_services.rai_blocklists
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rai_blocklists</code> resource.

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
INSERT INTO azure.cognitive_services.rai_blocklists (
accountName,
raiBlocklistName,
resourceGroupName,
subscriptionId,
tags,
properties
)
SELECT 
'{{ accountName }}',
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
        - name: description
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>rai_blocklists</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cognitive_services.rai_blocklists
WHERE accountName = '{{ accountName }}'
AND raiBlocklistName = '{{ raiBlocklistName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
