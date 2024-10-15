---
title: workspace_products
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_products
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

Creates, updates, deletes, gets or lists a <code>workspace_products</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_products" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_products', value: 'view', },
        { label: 'workspace_products', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="approval_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="productId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptions_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="terms" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Product profile. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the details of the product specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of products in the specified workspace in a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates or Updates a product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Delete product. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Update existing product details. |

## `SELECT` examples

Lists a collection of products in the specified workspace in a service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_products', value: 'view', },
        { label: 'workspace_products', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
approval_required,
display_name,
productId,
resourceGroupName,
serviceName,
state,
subscriptionId,
subscription_required,
subscriptions_limit,
terms,
workspaceId
FROM azure.api_management.vw_workspace_products
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.workspace_products
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_products</code> resource.

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
INSERT INTO azure.api_management.workspace_products (
productId,
resourceGroupName,
serviceName,
subscriptionId,
workspaceId,
properties
)
SELECT 
'{{ productId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ workspaceId }}',
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
        - name: displayName
          value: string
        - name: description
          value: string
        - name: terms
          value: string
        - name: subscriptionRequired
          value: boolean
        - name: approvalRequired
          value: boolean
        - name: subscriptionsLimit
          value: integer
        - name: state
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspace_products</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.workspace_products
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```

## `DELETE` example

Deletes the specified <code>workspace_products</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.workspace_products
WHERE If-Match = '{{ If-Match }}'
AND productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
