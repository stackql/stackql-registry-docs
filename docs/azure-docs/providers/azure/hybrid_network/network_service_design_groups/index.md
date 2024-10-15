---
title: network_service_design_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - network_service_design_groups
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

Creates, updates, deletes, gets or lists a <code>network_service_design_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_service_design_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.network_service_design_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_service_design_groups', value: 'view', },
        { label: 'network_service_design_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="networkServiceDesignGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | network service design group properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about the specified networkServiceDesign group. |
| <CopyableCode code="list_by_publisher" /> | `SELECT` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Gets information of the network service design groups under a publisher. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a network service design group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId" /> | Deletes a specified network service design group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId" /> | Updates a network service design groups resource. |

## `SELECT` examples

Gets information of the network service design groups under a publisher.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_service_design_groups', value: 'view', },
        { label: 'network_service_design_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
location,
networkServiceDesignGroupName,
provisioning_state,
publisherName,
resourceGroupName,
subscriptionId,
tags
FROM azure.hybrid_network.vw_network_service_design_groups
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
FROM azure.hybrid_network.network_service_design_groups
WHERE publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_service_design_groups</code> resource.

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
INSERT INTO azure.hybrid_network.network_service_design_groups (
networkServiceDesignGroupName,
publisherName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ networkServiceDesignGroupName }}',
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
        - name: description
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_service_design_groups</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_network.network_service_design_groups
SET 
tags = '{{ tags }}'
WHERE 
networkServiceDesignGroupName = '{{ networkServiceDesignGroupName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_service_design_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_network.network_service_design_groups
WHERE networkServiceDesignGroupName = '{{ networkServiceDesignGroupName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
