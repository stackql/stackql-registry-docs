---
title: artifact_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_stores
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

Creates, updates, deletes, gets or lists a <code>artifact_stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifact_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.artifact_stores" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_artifact_stores', value: 'view', },
        { label: 'artifact_stores', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="artifactStoreName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backing_resource_public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_resource_group_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_strategy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="store_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Artifact store properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about the specified artifact store. |
| <CopyableCode code="list_by_publisher" /> | `SELECT` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Gets information of the ArtifactStores under publisher. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a artifact store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Deletes the specified artifact store. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Update artifact store resource. |
| <CopyableCode code="add_network_fabric_controller_end_points" /> | `EXEC` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Add network fabric controllers to artifact stores |
| <CopyableCode code="approve_private_end_points" /> | `EXEC` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Approve manual private endpoints on artifact stores |
| <CopyableCode code="remove_private_end_points" /> | `EXEC` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Remove manual private endpoints on artifact stores |

## `SELECT` examples

Gets information of the ArtifactStores under publisher.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_artifact_stores', value: 'view', },
        { label: 'artifact_stores', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
artifactStoreName,
backing_resource_public_network_access,
location,
managed_resource_group_configuration,
provisioning_state,
publisherName,
replication_strategy,
resourceGroupName,
storage_resource_id,
store_type,
subscriptionId,
tags
FROM azure.hybrid_network.vw_artifact_stores
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
FROM azure.hybrid_network.artifact_stores
WHERE publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>artifact_stores</code> resource.

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
INSERT INTO azure.hybrid_network.artifact_stores (
artifactStoreName,
publisherName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ artifactStoreName }}',
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
        - name: storeType
          value: string
        - name: backingResourcePublicNetworkAccess
          value: []
        - name: replicationStrategy
          value: string
        - name: managedResourceGroupConfiguration
          value:
            - name: name
              value: string
            - name: location
              value: string
        - name: storageResourceId
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>artifact_stores</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_network.artifact_stores
SET 
tags = '{{ tags }}'
WHERE 
artifactStoreName = '{{ artifactStoreName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>artifact_stores</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_network.artifact_stores
WHERE artifactStoreName = '{{ artifactStoreName }}'
AND publisherName = '{{ publisherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
