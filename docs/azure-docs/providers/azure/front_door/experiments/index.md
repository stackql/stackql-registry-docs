---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
  - front_door
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

Creates, updates, deletes, gets or lists a <code>experiments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.front_door.experiments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_experiments', value: 'view', },
        { label: 'experiments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointa" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointb" /> | `text` | field from the `properties` object |
| <CopyableCode code="experimentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="script_file_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Defines the properties of an experiment |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="experimentName, profileName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="experimentName, profileName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="experimentName, profileName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="experimentName, profileName, resourceGroupName, subscriptionId" /> | Updates an Experiment |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_experiments', value: 'view', },
        { label: 'experiments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
enabled_state,
endpointa,
endpointb,
experimentName,
location,
profileName,
resourceGroupName,
resource_state,
script_file_uri,
status,
subscriptionId,
tags,
type
FROM azure.front_door.vw_experiments
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.front_door.experiments
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>experiments</code> resource.

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
INSERT INTO azure.front_door.experiments (
experimentName,
profileName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ experimentName }}',
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: properties
      value:
        - name: description
          value: string
        - name: endpointA
          value:
            - name: name
              value: string
            - name: endpoint
              value: string
        - name: enabledState
          value: string
        - name: resourceState
          value: []
        - name: status
          value: string
        - name: scriptFileUri
          value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>experiments</code> resource.

```sql
/*+ update */
UPDATE azure.front_door.experiments
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
experimentName = '{{ experimentName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>experiments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.front_door.experiments
WHERE experimentName = '{{ experimentName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
