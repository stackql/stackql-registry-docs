---
title: workspace_product_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_product_policies
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

Creates, updates, deletes, gets or lists a <code>workspace_product_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_product_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_product_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_product_policies', value: 'view', },
        { label: 'workspace_product_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="format" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyId" /> | `text` | field from the `properties` object |
| <CopyableCode code="productId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Policy contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyId, productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Get the policy configuration at the Product level. |
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Get the policy configuration at the Product level. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="policyId, productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates or updates policy configuration for the Product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, policyId, productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes the policy configuration at the Product. |

## `SELECT` examples

Get the policy configuration at the Product level.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_product_policies', value: 'view', },
        { label: 'workspace_product_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
format,
policyId,
productId,
resourceGroupName,
serviceName,
subscriptionId,
value,
workspaceId
FROM azure.api_management.vw_workspace_product_policies
WHERE productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.workspace_product_policies
WHERE productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_product_policies</code> resource.

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
INSERT INTO azure.api_management.workspace_product_policies (
policyId,
productId,
resourceGroupName,
serviceName,
subscriptionId,
workspaceId,
properties
)
SELECT 
'{{ policyId }}',
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
        - name: value
          value: string
        - name: format
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>workspace_product_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.workspace_product_policies
WHERE If-Match = '{{ If-Match }}'
AND policyId = '{{ policyId }}'
AND productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
