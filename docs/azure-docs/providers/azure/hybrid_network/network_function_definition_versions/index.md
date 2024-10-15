---
title: network_function_definition_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_function_definition_versions
  - hybrid_network
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

Creates, updates, deletes, gets or lists a <code>network_function_definition_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_function_definition_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.network_function_definition_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_function_definition_versions', value: 'view', },
        { label: 'network_function_definition_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploy_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="networkFunctionDefinitionGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkFunctionDefinitionVersionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_function_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version_state" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network function definition version properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about a network function definition version. |
| <CopyableCode code="list_by_network_function_definition_group" /> | `SELECT` | <CopyableCode code="networkFunctionDefinitionGroupName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about a list of network function definition versions under a network function definition group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a network function definition version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId" /> | Deletes the specified network function definition version. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId" /> | Updates a network function definition version resource. |
| <CopyableCode code="update_state" /> | `EXEC` | <CopyableCode code="networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId" /> | Update network function definition version state. |

## `SELECT` examples

Gets information about a list of network function definition versions under a network function definition group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_function_definition_versions', value: 'view', },
        { label: 'network_function_definition_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
deploy_parameters,
location,
networkFunctionDefinitionGroupName,
networkFunctionDefinitionVersionName,
network_function_type,
provisioning_state,
publisherName,
resourceGroupName,
subscriptionId,
tags,
version_state
FROM azure.hybrid_network.vw_network_function_definition_versions
WHERE networkFunctionDefinitionGroupName = '{{ networkFunctionDefinitionGroupName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.hybrid_network.network_function_definition_versions
WHERE networkFunctionDefinitionGroupName = '{{ networkFunctionDefinitionGroupName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_function_definition_versions</code> resource.

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
INSERT INTO azure.hybrid_network.network_function_definition_versions (
networkFunctionDefinitionGroupName,
networkFunctionDefinitionVersionName,
publisherName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ networkFunctionDefinitionGroupName }}',
'{{ networkFunctionDefinitionVersionName }}',
'{{ publisherName }}',
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
        - name: versionState
          value: []
        - name: description
          value: string
        - name: deployParameters
          value: string
        - name: networkFunctionType
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_function_definition_versions</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_network.network_function_definition_versions
SET 
tags = '{{ tags }}'
WHERE 
networkFunctionDefinitionGroupName = '{{ networkFunctionDefinitionGroupName }}'
AND networkFunctionDefinitionVersionName = '{{ networkFunctionDefinitionVersionName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_function_definition_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_network.network_function_definition_versions
WHERE networkFunctionDefinitionGroupName = '{{ networkFunctionDefinitionGroupName }}'
AND networkFunctionDefinitionVersionName = '{{ networkFunctionDefinitionVersionName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
