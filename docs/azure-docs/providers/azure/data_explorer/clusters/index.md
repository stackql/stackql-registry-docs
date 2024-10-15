---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - data_explorer
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.clusters" /></td></tr>
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
| <CopyableCode code="accepted_audiences" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_fqdn_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_ip_range_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_ingestion_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_auto_stop" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_disk_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_double_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_purge" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_streaming_ingest" /> | `text` | field from the `properties` object |
| <CopyableCode code="engine_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="key_vault_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="language_extensions" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="migration_cluster" /> | `text` | field from the `properties` object |
| <CopyableCode code="optimized_autoscale" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restrict_outbound_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Azure SKU definition. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="state_reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="trusted_external_tenants" /> | `text` | field from the `properties` object |
| <CopyableCode code="uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_cluster_graduation_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | An array represents the availability zones of the cluster. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Class representing the Kusto cluster properties. |
| <CopyableCode code="sku" /> | `object` | Azure SKU definition. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | An array represents the availability zones of the cluster. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets a Kusto cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all Kusto clusters within a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Kusto clusters within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__sku" /> | Create or update a Kusto cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes a Kusto cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Update a Kusto cluster. |
| <CopyableCode code="add_language_extensions" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Add a list of language extensions that can run within KQL queries. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks that the cluster name is valid and is not already in use. |
| <CopyableCode code="detach_follower_databases" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__attachedDatabaseConfigurationName, data__clusterResourceId" /> | Detaches all followers of a database owned by this cluster. |
| <CopyableCode code="diagnose_virtual_network" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Diagnoses network connectivity status for external resources on which the service is dependent on. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__clusterResourceId" /> | Migrate data from a Kusto cluster to another cluster. |
| <CopyableCode code="remove_language_extensions" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Remove a list of language extensions that can run within KQL queries. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Starts a Kusto cluster. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Stops a Kusto cluster. |

## `SELECT` examples

Lists all Kusto clusters within a subscription.

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
accepted_audiences,
allowed_fqdn_list,
allowed_ip_range_list,
clusterName,
data_ingestion_uri,
enable_auto_stop,
enable_disk_encryption,
enable_double_encryption,
enable_purge,
enable_streaming_ingest,
engine_type,
etag,
identity,
key_vault_properties,
language_extensions,
location,
migration_cluster,
optimized_autoscale,
private_endpoint_connections,
provisioning_state,
public_ip_type,
public_network_access,
resourceGroupName,
restrict_outbound_network_access,
sku,
state,
state_reason,
subscriptionId,
system_data,
tags,
trusted_external_tenants,
uri,
virtual_cluster_graduation_properties,
virtual_network_configuration,
zones
FROM azure.data_explorer.vw_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
location,
properties,
sku,
systemData,
tags,
zones
FROM azure.data_explorer.clusters
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
INSERT INTO azure.data_explorer.clusters (
clusterName,
resourceGroupName,
subscriptionId,
data__sku,
sku,
zones,
identity,
properties,
tags,
location
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__sku }}',
'{{ sku }}',
'{{ zones }}',
'{{ identity }}',
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
    - name: sku
      value:
        - name: name
          value: string
        - name: capacity
          value: integer
        - name: tier
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
    - name: zones
      value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: state
          value: string
        - name: provisioningState
          value: []
        - name: uri
          value: string
        - name: dataIngestionUri
          value: string
        - name: stateReason
          value: string
        - name: trustedExternalTenants
          value:
            - - name: value
                value: string
        - name: optimizedAutoscale
          value:
            - name: version
              value: integer
            - name: isEnabled
              value: boolean
            - name: minimum
              value: integer
            - name: maximum
              value: integer
        - name: enableDiskEncryption
          value: boolean
        - name: enableStreamingIngest
          value: boolean
        - name: virtualNetworkConfiguration
          value:
            - name: subnetId
              value: string
            - name: enginePublicIpId
              value: string
            - name: dataManagementPublicIpId
              value: string
            - name: state
              value: string
        - name: keyVaultProperties
          value:
            - name: keyIdentifier
              value: string
            - name: identity
              value: string
        - name: enablePurge
          value: boolean
        - name: languageExtensions
          value:
            - name: value
              value:
                - - name: languageExtensionName
                    value: []
                  - name: languageExtensionImageName
                    value: []
                  - name: languageExtensionCustomImageName
                    value: []
        - name: enableDoubleEncryption
          value: boolean
        - name: publicNetworkAccess
          value: string
        - name: allowedIpRangeList
          value:
            - string
        - name: engineType
          value: string
        - name: acceptedAudiences
          value:
            - - name: value
                value: string
        - name: enableAutoStop
          value: boolean
        - name: restrictOutboundNetworkAccess
          value: string
        - name: allowedFqdnList
          value:
            - string
        - name: publicIPType
          value: string
        - name: virtualClusterGraduationProperties
          value: string
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: string
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: groupId
                    value: string
                  - name: provisioningState
                    value: string
        - name: migrationCluster
          value:
            - name: id
              value: string
            - name: uri
              value: string
            - name: dataIngestionUri
              value: string
            - name: role
              value: string
    - name: etag
      value: string
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
UPDATE azure.data_explorer.clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
zones = '{{ zones }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_explorer.clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
