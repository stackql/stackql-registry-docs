---
title: mongo_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_clusters
  - mongo_db
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

Creates, updates, deletes, gets or lists a <code>mongo_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mongo_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.mongo_db.mongo_clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mongo_clusters', value: 'view', },
        { label: 'mongo_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrator" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_string" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="high_availability" /> | `text` | field from the `properties` object |
| <CopyableCode code="infrastructure_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mongoClusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="preview_features" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="replica" /> | `text` | field from the `properties` object |
| <CopyableCode code="replica_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="sharding" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a mongo cluster. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | Gets information about a mongo cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the mongo clusters in a given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the mongo clusters in a given resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | Create or update a mongo cluster. Update overwrites all properties for the resource. To only modify some of the properties, use PATCH. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | Deletes a mongo cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | Updates an existing mongo cluster. The request body can contain one to many of the properties present in the normal mongo cluster definition. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Check if mongo cluster name is available for use. |
| <CopyableCode code="promote" /> | `EXEC` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId, data__promoteOption" /> | Promotes a replica mongo cluster to a primary role. |

## `SELECT` examples

List all the mongo clusters in a given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mongo_clusters', value: 'view', },
        { label: 'mongo_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrator,
backup,
cluster_status,
compute,
connection_string,
create_mode,
high_availability,
infrastructure_version,
location,
mongoClusterName,
preview_features,
private_endpoint_connections,
provisioning_state,
public_network_access,
replica,
replica_parameters,
resourceGroupName,
restore_parameters,
server_version,
sharding,
storage,
subscriptionId,
tags
FROM azure_isv.mongo_db.vw_mongo_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_isv.mongo_db.mongo_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mongo_clusters</code> resource.

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
INSERT INTO azure_isv.mongo_db.mongo_clusters (
mongoClusterName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ mongoClusterName }}',
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
        - name: createMode
          value: []
        - name: restoreParameters
          value:
            - name: pointInTimeUTC
              value: string
            - name: sourceResourceId
              value: []
        - name: replicaParameters
          value:
            - name: sourceLocation
              value: []
        - name: administrator
          value:
            - name: userName
              value: string
            - name: password
              value: string
        - name: serverVersion
          value: string
        - name: connectionString
          value: string
        - name: provisioningState
          value: []
        - name: clusterStatus
          value: []
        - name: publicNetworkAccess
          value: []
        - name: highAvailability
          value:
            - name: targetMode
              value: []
        - name: storage
          value:
            - name: sizeGb
              value: integer
        - name: sharding
          value:
            - name: shardCount
              value: integer
        - name: compute
          value:
            - name: tier
              value: string
        - name: backup
          value:
            - name: earliestRestoreTime
              value: string
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: groupIds
                    value:
                      - string
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: []
              - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: systemData
                value:
                  - name: createdBy
                    value: string
                  - name: createdByType
                    value: string
                  - name: createdAt
                    value: string
                  - name: lastModifiedBy
                    value: string
                  - name: lastModifiedByType
                    value: string
                  - name: lastModifiedAt
                    value: string
        - name: previewFeatures
          value:
            - []
        - name: replica
          value:
            - name: role
              value: []
            - name: replicationState
              value: []
        - name: infrastructureVersion
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>mongo_clusters</code> resource.

```sql
/*+ update */
UPDATE azure_isv.mongo_db.mongo_clusters
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
mongoClusterName = '{{ mongoClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>mongo_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.mongo_db.mongo_clusters
WHERE mongoClusterName = '{{ mongoClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
