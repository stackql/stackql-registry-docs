---
title: configuration_group_values
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_group_values
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

Creates, updates, deletes, gets or lists a <code>configuration_group_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_group_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.configuration_group_values" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_group_values', value: 'view', },
        { label: 'configuration_group_values', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configurationGroupValueName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_group_schema_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_group_schema_offering_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_group_schema_resource_reference" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Hybrid configuration group value properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationGroupValueName, resourceGroupName, subscriptionId" /> | Gets information about the specified hybrid configuration group values. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the hybrid network configurationGroupValues in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all sites in the configuration group value in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationGroupValueName, resourceGroupName, subscriptionId" /> | Creates or updates a hybrid configuration group value. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationGroupValueName, resourceGroupName, subscriptionId" /> | Deletes the specified hybrid configuration group value. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="configurationGroupValueName, resourceGroupName, subscriptionId" /> | Updates a hybrid configuration group tags. |

## `SELECT` examples

Lists all sites in the configuration group value in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_group_values', value: 'view', },
        { label: 'configuration_group_values', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
configurationGroupValueName,
configuration_group_schema_name,
configuration_group_schema_offering_location,
configuration_group_schema_resource_reference,
configuration_type,
location,
provisioning_state,
publisher_name,
publisher_scope,
resourceGroupName,
subscriptionId,
tags
FROM azure.hybrid_network.vw_configuration_group_values
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.hybrid_network.configuration_group_values
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_group_values</code> resource.

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
INSERT INTO azure.hybrid_network.configuration_group_values (
configurationGroupValueName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ configurationGroupValueName }}',
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
        - name: publisherName
          value: string
        - name: publisherScope
          value: []
        - name: configurationGroupSchemaName
          value: string
        - name: configurationGroupSchemaOfferingLocation
          value: string
        - name: configurationGroupSchemaResourceReference
          value:
            - name: idType
              value: []
        - name: configurationType
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>configuration_group_values</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_network.configuration_group_values
WHERE configurationGroupValueName = '{{ configurationGroupValueName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
