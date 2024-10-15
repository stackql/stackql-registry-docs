---
title: sql_server_availability_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_availability_groups
  - azure_arc_data
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

Creates, updates, deletes, gets or lists a <code>sql_server_availability_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_server_availability_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.sql_server_availability_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_server_availability_groups', value: 'view', },
        { label: 'sql_server_availability_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availabilityGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="collection_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="databases" /> | `text` | field from the `properties` object |
| <CopyableCode code="info" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="replicas" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlServerInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of Arc Sql Server availability group resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Retrieves an Arc Sql Server availability group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlServerInstanceName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId, data__properties" /> | Creates or replaces an Arc Sql Server Availability Group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Deletes an Arc Sql Server availability group resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Updates an existing Availability Group. |
| <CopyableCode code="detail_view" /> | `EXEC` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Retrieves detailed properties of the Availability Group. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Request manual failover of the availability group to this server. |
| <CopyableCode code="force_failover_allow_data_loss" /> | `EXEC` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Request forced failover of the availability group to this server. |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_server_availability_groups', value: 'view', },
        { label: 'sql_server_availability_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
availabilityGroupName,
availability_group_id,
collection_timestamp,
databases,
info,
instance_name,
location,
provisioning_state,
replicas,
resourceGroupName,
server_name,
sqlServerInstanceName,
subscriptionId,
tags
FROM azure.azure_arc_data.vw_sql_server_availability_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.azure_arc_data.sql_server_availability_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_server_availability_groups</code> resource.

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
INSERT INTO azure.azure_arc_data.sql_server_availability_groups (
availabilityGroupName,
resourceGroupName,
sqlServerInstanceName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ availabilityGroupName }}',
'{{ resourceGroupName }}',
'{{ sqlServerInstanceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: availabilityGroupId
          value: string
        - name: serverName
          value: string
        - name: instanceName
          value: string
        - name: collectionTimestamp
          value: string
        - name: info
          value:
            - name: failureConditionLevel
              value: integer
            - name: healthCheckTimeout
              value: integer
            - name: automatedBackupPreferenceDescription
              value: string
            - name: version
              value: integer
            - name: basicFeatures
              value: boolean
            - name: dtcSupport
              value: boolean
            - name: dbFailover
              value: boolean
            - name: isDistributed
              value: boolean
            - name: clusterTypeDescription
              value: string
            - name: requiredSynchronizedSecondariesToCommit
              value: integer
            - name: isContained
              value: boolean
            - name: primaryReplica
              value: string
            - name: primaryRecoveryHealthDescription
              value: string
            - name: secondaryRecoveryHealthDescription
              value: string
            - name: synchronizationHealthDescription
              value: string
            - name: replicationPartnerType
              value: string
        - name: replicas
          value:
            - name: value
              value:
                - - name: replicaId
                    value: string
                  - name: replicaName
                    value: string
                  - name: configure
                    value:
                      - name: endpointUrl
                        value: string
                      - name: availabilityModeDescription
                        value: string
                      - name: failoverModeDescription
                        value: string
                      - name: sessionTimeout
                        value: integer
                      - name: primaryRoleAllowConnectionsDescription
                        value: string
                      - name: secondaryRoleAllowConnectionsDescription
                        value: string
                      - name: replicaCreateDate
                        value: string
                      - name: replicaModifyDate
                        value: string
                      - name: backupPriority
                        value: integer
                      - name: readOnlyRoutingUrl
                        value: string
                      - name: readWriteRoutingUrl
                        value: string
                      - name: seedingModeDescription
                        value: string
                  - name: state
                    value:
                      - name: availabilityGroupReplicaRole
                        value: string
                      - name: operationalStateDescription
                        value: string
                      - name: recoveryHealthDescription
                        value: string
                      - name: synchronizationHealthDescription
                        value: string
                      - name: connectedStateDescription
                        value: string
                      - name: lastConnectErrorDescription
                        value: string
                      - name: lastConnectErrorTimestamp
                        value: string
            - name: nextLink
              value: string
        - name: databases
          value:
            - name: value
              value:
                - - name: databaseName
                    value: string
                  - name: replicaName
                    value: string
                  - name: isLocal
                    value: boolean
                  - name: isPrimaryReplica
                    value: boolean
                  - name: synchronizationStateDescription
                    value: string
                  - name: isCommitParticipant
                    value: boolean
                  - name: synchronizationHealthDescription
                    value: string
                  - name: databaseStateDescription
                    value: string
                  - name: isSuspended
                    value: boolean
                  - name: suspendReasonDescription
                    value: string
            - name: nextLink
              value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sql_server_availability_groups</code> resource.

```sql
/*+ update */
UPDATE azure.azure_arc_data.sql_server_availability_groups
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
availabilityGroupName = '{{ availabilityGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sql_server_availability_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_arc_data.sql_server_availability_groups
WHERE availabilityGroupName = '{{ availabilityGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
