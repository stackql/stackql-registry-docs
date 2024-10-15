---
title: documentations
hide_title: false
hide_table_of_contents: false
keywords:
  - documentations
  - api_management
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

Creates, updates, deletes, gets or lists a <code>documentations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documentations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.documentations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_documentations', value: 'view', },
        { label: 'documentations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="documentationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Markdown documentation details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="documentationId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Documentation specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists all Documentations of the API Management service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="documentationId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new Documentation or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, documentationId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified Documentation from an API. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, documentationId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the Documentation for an API specified by its identifier. |

## `SELECT` examples

Lists all Documentations of the API Management service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_documentations', value: 'view', },
        { label: 'documentations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
content,
documentationId,
resourceGroupName,
serviceName,
subscriptionId,
title
FROM azure.api_management.vw_documentations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.documentations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>documentations</code> resource.

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
INSERT INTO azure.api_management.documentations (
documentationId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ documentationId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: title
          value: string
        - name: content
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>documentations</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.documentations
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND documentationId = '{{ documentationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>documentations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.documentations
WHERE If-Match = '{{ If-Match }}'
AND documentationId = '{{ documentationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
