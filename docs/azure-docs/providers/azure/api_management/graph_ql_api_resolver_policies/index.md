---
title: graph_ql_api_resolver_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - graph_ql_api_resolver_policies
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

Creates, updates, deletes, gets or lists a <code>graph_ql_api_resolver_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graph_ql_api_resolver_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.graph_ql_api_resolver_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_graph_ql_api_resolver_policies', value: 'view', },
        { label: 'graph_ql_api_resolver_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="format" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resolverId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Policy contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, policyId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Get the policy configuration at the GraphQL API Resolver level. |
| <CopyableCode code="list_by_resolver" /> | `SELECT` | <CopyableCode code="apiId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Get the list of policy configuration at the GraphQL API Resolver level. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, policyId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates policy configuration for the GraphQL API Resolver level. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, policyId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the policy configuration at the GraphQL Api Resolver. |

## `SELECT` examples

Get the list of policy configuration at the GraphQL API Resolver level.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_graph_ql_api_resolver_policies', value: 'view', },
        { label: 'graph_ql_api_resolver_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiId,
format,
policyId,
resolverId,
resourceGroupName,
serviceName,
subscriptionId,
value
FROM azure.api_management.vw_graph_ql_api_resolver_policies
WHERE apiId = '{{ apiId }}'
AND resolverId = '{{ resolverId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.graph_ql_api_resolver_policies
WHERE apiId = '{{ apiId }}'
AND resolverId = '{{ resolverId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>graph_ql_api_resolver_policies</code> resource.

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
INSERT INTO azure.api_management.graph_ql_api_resolver_policies (
apiId,
policyId,
resolverId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apiId }}',
'{{ policyId }}',
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
        - name: value
          value: string
        - name: format
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>graph_ql_api_resolver_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.graph_ql_api_resolver_policies
WHERE If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND policyId = '{{ policyId }}'
AND resolverId = '{{ resolverId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
