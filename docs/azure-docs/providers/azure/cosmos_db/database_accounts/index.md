---
title: database_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - database_accounts
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>database_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.database_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_accounts', value: 'view', },
        { label: 'database_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `text` | The name of the ARM resource. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="analytical_storage_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_mode_change_transition_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="connector_offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="consistency_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="cors" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_managed_key_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_account_offer_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_priority_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostic_log_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_key_based_metadata_write_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="document_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_analytical_storage" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_automatic_failover" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_burst_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_cassandra_connector" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_free_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_materialized_views" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_multiple_write_locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_partition_merge" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_per_region_per_partition_autoscale" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_priority_based_execution" /> | `text` | field from the `properties` object |
| <CopyableCode code="failover_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_virtual_network_filter_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_key_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="keys_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Indicates the type of database account. This can only be set at database account creation. |
| <CopyableCode code="location" /> | `text` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="minimal_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_acl_bypass" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_acl_bypass_resource_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="read_locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
| <CopyableCode code="virtual_network_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="write_locations" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | Indicates the type of database account. This can only be set at database account creation. |
| <CopyableCode code="location" /> | `string` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="properties" /> | `object` | Properties for the database account. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves the properties of an existing Azure Cosmos DB database account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the Azure Cosmos DB database accounts available under the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the Azure Cosmos DB database accounts available under the given resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an Azure Cosmos DB database account. The "Update" method is preferred when performing updates on an account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Deletes an existing Azure Cosmos DB database account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing Azure Cosmos DB database account. |
| <CopyableCode code="failover_priority_change" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__failoverPolicies" /> | Changes the failover priority for the Azure Cosmos DB database account. A failover priority of 0 indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. |
| <CopyableCode code="offline_region" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__region" /> | Offline the specified region for the specified Azure Cosmos DB database account. |
| <CopyableCode code="online_region" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__region" /> | Online the specified region for the specified Azure Cosmos DB database account. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__keyKind" /> | Regenerates an access key for the specified Azure Cosmos DB database account. |

## `SELECT` examples

Lists all the Azure Cosmos DB database accounts available under the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_accounts', value: 'view', },
        { label: 'database_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
analytical_storage_configuration,
api_properties,
backup_policy,
capabilities,
capacity,
capacity_mode,
capacity_mode_change_transition_state,
connector_offer,
consistency_policy,
cors,
create_mode,
customer_managed_key_status,
database_account_offer_type,
default_identity,
default_priority_level,
diagnostic_log_settings,
disable_key_based_metadata_write_access,
disable_local_auth,
document_endpoint,
enable_analytical_storage,
enable_automatic_failover,
enable_burst_capacity,
enable_cassandra_connector,
enable_free_tier,
enable_materialized_views,
enable_multiple_write_locations,
enable_partition_merge,
enable_per_region_per_partition_autoscale,
enable_priority_based_execution,
failover_policies,
identity,
instance_id,
ip_rules,
is_virtual_network_filter_enabled,
key_vault_key_uri,
keys_metadata,
kind,
location,
locations,
minimal_tls_version,
network_acl_bypass,
network_acl_bypass_resource_ids,
private_endpoint_connections,
provisioning_state,
public_network_access,
read_locations,
resourceGroupName,
restore_parameters,
subscriptionId,
system_data,
tags,
type,
virtual_network_rules,
write_locations
FROM azure.cosmos_db.vw_database_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
kind,
location,
properties,
systemData,
tags,
type
FROM azure.cosmos_db.database_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_accounts</code> resource.

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
INSERT INTO azure.cosmos_db.database_accounts (
accountName,
resourceGroupName,
subscriptionId,
data__properties,
kind,
identity,
properties,
location,
tags
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ kind }}',
'{{ identity }}',
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
    - name: kind
      value: string
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
    - name: properties
      value:
        - name: consistencyPolicy
          value:
            - name: defaultConsistencyLevel
              value: string
            - name: maxStalenessPrefix
              value: integer
            - name: maxIntervalInSeconds
              value: integer
        - name: locations
          value:
            - - name: id
                value: string
              - name: locationName
                value: string
              - name: documentEndpoint
                value: string
              - name: provisioningState
                value: []
              - name: failoverPriority
                value: integer
              - name: isZoneRedundant
                value: boolean
        - name: databaseAccountOfferType
          value: []
        - name: ipRules
          value: []
        - name: isVirtualNetworkFilterEnabled
          value: boolean
        - name: enableAutomaticFailover
          value: boolean
        - name: capabilities
          value:
            - - name: name
                value: string
        - name: virtualNetworkRules
          value:
            - - name: id
                value: string
              - name: ignoreMissingVNetServiceEndpoint
                value: boolean
        - name: enableMultipleWriteLocations
          value: boolean
        - name: enableCassandraConnector
          value: boolean
        - name: connectorOffer
          value: []
        - name: disableKeyBasedMetadataWriteAccess
          value: boolean
        - name: keyVaultKeyUri
          value: string
        - name: defaultIdentity
          value: string
        - name: publicNetworkAccess
          value: []
        - name: enableFreeTier
          value: boolean
        - name: apiProperties
          value:
            - name: serverVersion
              value: string
        - name: enableAnalyticalStorage
          value: boolean
        - name: analyticalStorageConfiguration
          value:
            - name: schemaType
              value: []
        - name: createMode
          value: []
        - name: backupPolicy
          value:
            - name: type
              value: []
            - name: migrationState
              value:
                - name: status
                  value: []
                - name: startTime
                  value: string
        - name: cors
          value:
            - - name: allowedOrigins
                value: string
              - name: allowedMethods
                value: string
              - name: allowedHeaders
                value: string
              - name: exposedHeaders
                value: string
              - name: maxAgeInSeconds
                value: integer
        - name: networkAclBypass
          value: []
        - name: networkAclBypassResourceIds
          value:
            - string
        - name: diagnosticLogSettings
          value:
            - name: enableFullTextQuery
              value: string
        - name: disableLocalAuth
          value: boolean
        - name: restoreParameters
          value:
            - name: restoreMode
              value: string
            - name: restoreSource
              value: string
            - name: restoreTimestampInUtc
              value: string
            - name: databasesToRestore
              value:
                - - name: databaseName
                    value: string
                  - name: collectionNames
                    value:
                      - []
            - name: gremlinDatabasesToRestore
              value:
                - - name: databaseName
                    value: string
                  - name: graphNames
                    value:
                      - []
            - name: tablesToRestore
              value:
                - []
            - name: sourceBackupLocation
              value: string
            - name: restoreWithTtlDisabled
              value: boolean
        - name: capacity
          value:
            - name: totalThroughputLimit
              value: integer
        - name: capacityMode
          value: []
        - name: enableMaterializedViews
          value: boolean
        - name: keysMetadata
          value:
            - name: primaryMasterKey
              value:
                - name: generationTime
                  value: string
        - name: enablePartitionMerge
          value: boolean
        - name: enableBurstCapacity
          value: boolean
        - name: minimalTlsVersion
          value: []
        - name: customerManagedKeyStatus
          value: string
        - name: enablePriorityBasedExecution
          value: boolean
        - name: defaultPriorityLevel
          value: []
        - name: enablePerRegionPerPartitionAutoscale
          value: boolean
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>database_accounts</code> resource.

```sql
/*+ update */
UPDATE azure.cosmos_db.database_accounts
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>database_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.database_accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
