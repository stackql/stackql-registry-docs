---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - iot_data_processor
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

Creates, updates, deletes, gets or lists a <code>datasets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_data_processor.datasets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_datasets', value: 'view', },
        { label: 'datasets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="datasetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="payload" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="ttl" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a Dataset resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetName, instanceName, resourceGroupName, subscriptionId" /> | Get a Dataset |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="datasetName, instanceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a Dataset |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetName, instanceName, resourceGroupName, subscriptionId" /> | Delete a Dataset |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="datasetName, instanceName, resourceGroupName, subscriptionId" /> | Update a Dataset |

## `SELECT` examples

Get a Dataset

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_datasets', value: 'view', },
        { label: 'datasets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
datasetName,
extended_location,
instanceName,
keys,
location,
payload,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
timestamp,
ttl
FROM azure.iot_data_processor.vw_datasets
WHERE datasetName = '{{ datasetName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.iot_data_processor.datasets
WHERE datasetName = '{{ datasetName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>datasets</code> resource.

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
INSERT INTO azure.iot_data_processor.datasets (
datasetName,
instanceName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ datasetName }}',
'{{ instanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}',
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
        - name: description
          value: string
        - name: payload
          value: string
        - name: timestamp
          value: string
        - name: ttl
          value: string
        - name: keys
          value: object
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>datasets</code> resource.

```sql
/*+ update */
UPDATE azure.iot_data_processor.datasets
SET 
tags = '{{ tags }}'
WHERE 
datasetName = '{{ datasetName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>datasets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_data_processor.datasets
WHERE datasetName = '{{ datasetName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
