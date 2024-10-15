---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - mysql
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

Creates, updates, deletes, gets or lists a <code>servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers', value: 'view', },
        { label: 'servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrator_login" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrator_login_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="fully_qualified_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="high_availability" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Properties to configure Identity for Bring your Own Keys |
| <CopyableCode code="import_source_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="maintenance_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="maintenance_window" /> | `text` | field from the `properties` object |
| <CopyableCode code="network" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="replica_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_in_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Billing information related properties of a server. |
| <CopyableCode code="source_server_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Properties to configure Identity for Bring your Own Keys |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a server. |
| <CopyableCode code="sku" /> | `object` | Billing information related properties of a server. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets information about a server. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the servers in a given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the servers in a given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Creates a new server or updates an existing server. The update action will overwrite the existing server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Deletes a server. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Updates an existing server. The request body can contain one to many of the properties present in the normal server definition. |
| <CopyableCode code="detach_v_net" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Detach VNet on a server. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Manual failover a server. |
| <CopyableCode code="reset_gtid" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Resets GTID on a server. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Restarts a server. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Starts a server. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Stops a server. |
| <CopyableCode code="validate_estimate_high_availability" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Validate a deployment of high availability. |

## `SELECT` examples

List all the servers in a given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers', value: 'view', },
        { label: 'servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrator_login,
administrator_login_password,
availability_zone,
backup,
create_mode,
data_encryption,
database_port,
fully_qualified_domain_name,
high_availability,
identity,
import_source_properties,
location,
maintenance_policy,
maintenance_window,
network,
private_endpoint_connections,
replica_capacity,
replication_role,
resourceGroupName,
restore_point_in_time,
serverName,
sku,
source_server_resource_id,
state,
storage,
subscriptionId,
tags,
version
FROM azure.mysql.vw_servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
sku,
tags
FROM azure.mysql.servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>servers</code> resource.

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
INSERT INTO azure.mysql.servers (
resourceGroupName,
serverName,
subscriptionId,
identity,
sku,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ identity }}',
'{{ sku }}',
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
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
    - name: properties
      value:
        - name: administratorLogin
          value: string
        - name: administratorLoginPassword
          value: string
        - name: version
          value: []
        - name: availabilityZone
          value: string
        - name: createMode
          value: string
        - name: sourceServerResourceId
          value: string
        - name: restorePointInTime
          value: string
        - name: replicationRole
          value: []
        - name: replicaCapacity
          value: integer
        - name: dataEncryption
          value:
            - name: primaryUserAssignedIdentityId
              value: string
            - name: primaryKeyURI
              value: string
            - name: geoBackupUserAssignedIdentityId
              value: string
            - name: geoBackupKeyURI
              value: string
            - name: type
              value: string
        - name: state
          value: string
        - name: fullyQualifiedDomainName
          value: string
        - name: databasePort
          value: integer
        - name: storage
          value:
            - name: storageSizeGB
              value: integer
            - name: iops
              value: integer
            - name: autoGrow
              value: []
            - name: storageSku
              value: string
            - name: storageRedundancy
              value: []
        - name: backup
          value:
            - name: backupRetentionDays
              value: integer
            - name: backupIntervalHours
              value: integer
            - name: earliestRestoreDate
              value: string
        - name: highAvailability
          value:
            - name: mode
              value: string
            - name: state
              value: string
            - name: standbyAvailabilityZone
              value: string
        - name: network
          value:
            - name: delegatedSubnetResourceId
              value: string
            - name: privateDnsZoneResourceId
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
        - name: maintenancePolicy
          value:
            - name: patchStrategy
              value: []
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
        - name: importSourceProperties
          value:
            - name: storageType
              value: string
            - name: storageUrl
              value: string
            - name: sasToken
              value: string
            - name: dataDirPath
              value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>servers</code> resource.

```sql
/*+ update */
UPDATE azure.mysql.servers
SET 
identity = '{{ identity }}',
sku = '{{ sku }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mysql.servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
