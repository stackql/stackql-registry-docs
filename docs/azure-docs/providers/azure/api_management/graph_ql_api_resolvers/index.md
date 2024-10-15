---
title: graph_ql_api_resolvers
hide_title: false
hide_table_of_contents: false
keywords:
  - graph_ql_api_resolvers
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

Creates, updates, deletes, gets or lists a <code>graph_ql_api_resolvers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graph_ql_api_resolvers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.graph_ql_api_resolvers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_graph_ql_api_resolvers', value: 'view', },
        { label: 'graph_ql_api_resolvers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="path" /> | `text` | field from the `properties` object |
| <CopyableCode code="resolverId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | GraphQL API Resolver Entity Base Contract details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the GraphQL API Resolver specified by its identifier. |
| <CopyableCode code="list_by_api" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of the resolvers for the specified GraphQL API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new resolver in the GraphQL API or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified resolver in the GraphQL API. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, apiId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the resolver in the GraphQL API specified by its identifier. |

## `SELECT` examples

Lists a collection of the resolvers for the specified GraphQL API.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_graph_ql_api_resolvers', value: 'view', },
        { label: 'graph_ql_api_resolvers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
apiId,
display_name,
path,
resolverId,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.api_management.vw_graph_ql_api_resolvers
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.graph_ql_api_resolvers
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>graph_ql_api_resolvers</code> resource.

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
INSERT INTO azure.api_management.graph_ql_api_resolvers (
apiId,
resolverId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apiId }}',
'{{ resolverId }}',
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
        - name: displayName
          value: string
        - name: path
          value: string
        - name: description
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>graph_ql_api_resolvers</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.graph_ql_api_resolvers
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND resolverId = '{{ resolverId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>graph_ql_api_resolvers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.graph_ql_api_resolvers
WHERE If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND resolverId = '{{ resolverId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
