---
title: document_processors
hide_title: false
hide_table_of_contents: false
keywords:
  - document_processors
  - syntex
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

Creates, updates, deletes, gets or lists a <code>document_processors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>document_processors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.syntex.document_processors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_document_processors', value: 'view', },
        { label: 'document_processors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="processorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spo_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="spo_tenant_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Document processor properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="processorName, resourceGroupName, subscriptionId" /> | Returns a document processor for a given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns document processors in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns document processors in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="processorName, resourceGroupName, subscriptionId" /> | Creates a document processor resource for a given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="processorName, resourceGroupName, subscriptionId" /> | Deletes document processor resource for a given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="processorName, resourceGroupName, subscriptionId" /> | Updates a document processor resource for a given name. |

## `SELECT` examples

Returns document processors in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_document_processors', value: 'view', },
        { label: 'document_processors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
processorName,
provisioning_state,
resourceGroupName,
spo_tenant_id,
spo_tenant_url,
subscriptionId,
tags
FROM azure_extras.syntex.vw_document_processors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_extras.syntex.document_processors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>document_processors</code> resource.

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
INSERT INTO azure_extras.syntex.document_processors (
processorName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ processorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: spoTenantUrl
          value: string
        - name: spoTenantId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>document_processors</code> resource.

```sql
/*+ update */
UPDATE azure_extras.syntex.document_processors
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
processorName = '{{ processorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>document_processors</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.syntex.document_processors
WHERE processorName = '{{ processorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
