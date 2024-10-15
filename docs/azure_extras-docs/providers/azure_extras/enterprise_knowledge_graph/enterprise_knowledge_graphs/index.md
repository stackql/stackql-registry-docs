---
title: enterprise_knowledge_graphs
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprise_knowledge_graphs
  - enterprise_knowledge_graph
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

Creates, updates, deletes, gets or lists a <code>enterprise_knowledge_graphs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enterprise_knowledge_graphs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.enterprise_knowledge_graph.enterprise_knowledge_graphs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_enterprise_knowledge_graphs', value: 'view', },
        { label: 'enterprise_knowledge_graphs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `text` | Specifies the name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Specifies the location of the resource. |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The SKU of the EnterpriseKnowledgeGraph service account. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="type" /> | `text` | Specifies the type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `string` | Specifies the name of the resource. |
| <CopyableCode code="location" /> | `string` | Specifies the location of the resource. |
| <CopyableCode code="properties" /> | `object` | The parameters to provide for the EnterpriseKnowledgeGraph. |
| <CopyableCode code="sku" /> | `object` | The SKU of the EnterpriseKnowledgeGraph service account. |
| <CopyableCode code="tags" /> | `object` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns a EnterpriseKnowledgeGraph service specified by the parameters. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all the resources of a particular type belonging to a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all the resources of a particular type belonging to a resource group |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Creates a EnterpriseKnowledgeGraph Service. EnterpriseKnowledgeGraph Service is a resource group wide resource type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes a EnterpriseKnowledgeGraph Service from the resource group.  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a EnterpriseKnowledgeGraph Service |

## `SELECT` examples

Returns all the resources of a particular type belonging to a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_enterprise_knowledge_graphs', value: 'view', },
        { label: 'enterprise_knowledge_graphs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
location,
metadata,
provisioning_state,
resourceGroupName,
resourceName,
sku,
subscriptionId,
tags,
type
FROM azure_extras.enterprise_knowledge_graph.vw_enterprise_knowledge_graphs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
sku,
tags,
type
FROM azure_extras.enterprise_knowledge_graph.enterprise_knowledge_graphs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>enterprise_knowledge_graphs</code> resource.

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
INSERT INTO azure_extras.enterprise_knowledge_graph.enterprise_knowledge_graphs (
resourceGroupName,
resourceName,
subscriptionId,
location,
tags,
sku,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: []
    - name: properties
      value:
        - name: description
          value: string
        - name: metadata
          value: object
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>enterprise_knowledge_graphs</code> resource.

```sql
/*+ update */
UPDATE azure_extras.enterprise_knowledge_graph.enterprise_knowledge_graphs
SET 
location = '{{ location }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>enterprise_knowledge_graphs</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.enterprise_knowledge_graph.enterprise_knowledge_graphs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
