---
title: configuration_group_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_group_schemas
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

Creates, updates, deletes, gets or lists a <code>configuration_group_schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_group_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.configuration_group_schemas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_group_schemas', value: 'view', },
        { label: 'configuration_group_schemas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurationGroupSchemaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema_definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version_state" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Configuration group schema properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about the specified configuration group schema. |
| <CopyableCode code="list_by_publisher" /> | `SELECT` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Gets information of the configuration group schemas under a publisher. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a configuration group schema. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId" /> | Deletes a specified configuration group schema. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId" /> | Updates a configuration group schema resource. |
| <CopyableCode code="update_state" /> | `EXEC` | <CopyableCode code="configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId" /> | Update configuration group schema state. |

## `SELECT` examples

Gets information of the configuration group schemas under a publisher.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_group_schemas', value: 'view', },
        { label: 'configuration_group_schemas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
configurationGroupSchemaName,
location,
provisioning_state,
publisherName,
resourceGroupName,
schema_definition,
subscriptionId,
tags,
version_state
FROM azure.hybrid_network.vw_configuration_group_schemas
WHERE publisherName = '{{ publisherName }}'
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
FROM azure.hybrid_network.configuration_group_schemas
WHERE publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_group_schemas</code> resource.

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
INSERT INTO azure.hybrid_network.configuration_group_schemas (
configurationGroupSchemaName,
publisherName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ configurationGroupSchemaName }}',
'{{ publisherName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: versionState
          value: []
        - name: description
          value: string
        - name: schemaDefinition
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>configuration_group_schemas</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_network.configuration_group_schemas
SET 
tags = '{{ tags }}'
WHERE 
configurationGroupSchemaName = '{{ configurationGroupSchemaName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>configuration_group_schemas</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_network.configuration_group_schemas
WHERE configurationGroupSchemaName = '{{ configurationGroupSchemaName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
