---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - postgresql_hsc
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_hsc.clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aad_auth_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrator_login" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrator_login_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="auth_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="citus_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="coordinator_enable_public_ip_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="coordinator_server_edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="coordinator_storage_quota_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="coordinator_vcores" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="earliest_restore_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_geo_backup" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_ha" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_shards_on_coordinator" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Describes the identity of the cluster. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="maintenance_window" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_enable_public_ip_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_server_edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_storage_quota_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_vcores" /> | `text` | field from the `properties` object |
| <CopyableCode code="password_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="point_in_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="postgresql_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="preferred_primary_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="read_replicas" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Describes the identity of the cluster. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the cluster. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets information about a cluster such as compute and storage configuration and cluster lifecycle metadata such as cluster creation date and time. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all clusters in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all clusters in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Creates a new cluster with servers. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes a cluster together with servers in it. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Updates an existing cluster. The request body can contain one or several properties from the cluster definition. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks availability of a cluster name. Cluster names should be globally unique; at least 3 characters and at most 40 characters long; they must only contain lowercase letters, numbers, and hyphens; and must not start or end with a hyphen. |
| <CopyableCode code="promote_read_replica" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Promotes read replica cluster to an independent read-write cluster. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Restarts all nodes in the cluster. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Starts stopped compute on all cluster nodes. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Stops compute on all cluster nodes. |

## `SELECT` examples

Lists all clusters in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aad_auth_enabled,
administrator_login,
administrator_login_password,
auth_config,
citus_version,
clusterName,
coordinator_enable_public_ip_access,
coordinator_server_edition,
coordinator_storage_quota_in_mb,
coordinator_vcores,
data_encryption,
database_name,
earliest_restore_time,
enable_geo_backup,
enable_ha,
enable_shards_on_coordinator,
identity,
location,
maintenance_window,
node_count,
node_enable_public_ip_access,
node_server_edition,
node_storage_quota_in_mb,
node_vcores,
password_enabled,
point_in_time_utc,
postgresql_version,
preferred_primary_zone,
private_endpoint_connections,
provisioning_state,
read_replicas,
resourceGroupName,
server_names,
source_location,
source_resource_id,
state,
subscriptionId,
tags
FROM azure.postgresql_hsc.vw_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.postgresql_hsc.clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

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
INSERT INTO azure.postgresql_hsc.clusters (
clusterName,
resourceGroupName,
subscriptionId,
properties,
identity,
tags,
location
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: aadAuthEnabled
          value: string
        - name: administratorLogin
          value: string
        - name: administratorLoginPassword
          value: string
        - name: dataEncryption
          value:
            - name: primaryKeyUri
              value: string
            - name: primaryUserAssignedIdentityId
              value: string
            - name: type
              value: string
        - name: provisioningState
          value: string
        - name: state
          value: string
        - name: postgresqlVersion
          value: string
        - name: citusVersion
          value: string
        - name: maintenanceWindow
          value:
            - name: customWindow
              value: string
            - name: startHour
              value: integer
            - name: startMinute
              value: integer
            - name: dayOfWeek
              value: integer
        - name: preferredPrimaryZone
          value: string
        - name: enableShardsOnCoordinator
          value: boolean
        - name: enableHa
          value: boolean
        - name: coordinatorServerEdition
          value: string
        - name: coordinatorStorageQuotaInMb
          value: integer
        - name: coordinatorVCores
          value: integer
        - name: coordinatorEnablePublicIpAccess
          value: boolean
        - name: nodeServerEdition
          value: string
        - name: nodeCount
          value: integer
        - name: nodeStorageQuotaInMb
          value: integer
        - name: nodeVCores
          value: integer
        - name: nodeEnablePublicIpAccess
          value: boolean
        - name: serverNames
          value:
            - - name: name
                value: string
              - name: fullyQualifiedDomainName
                value: string
        - name: sourceResourceId
          value: string
        - name: sourceLocation
          value: string
        - name: passwordEnabled
          value: string
        - name: pointInTimeUTC
          value: string
        - name: readReplicas
          value:
            - string
        - name: earliestRestoreTime
          value: string
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: groupIds
                    value:
                      - string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
        - name: databaseName
          value: string
        - name: enableGeoBackup
          value: boolean
        - name: authConfig
          value:
            - name: activeDirectoryAuth
              value: string
            - name: passwordAuth
              value: string
    - name: identity
      value:
        - name: type
          value: string
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
UPDATE azure.postgresql_hsc.clusters
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.postgresql_hsc.clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
