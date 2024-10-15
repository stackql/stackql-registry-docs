---
title: managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instances
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instances', value: 'view', },
        { label: 'managed_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrator_login" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrator_login_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrators" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="collation" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_backup_storage_redundancy" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_format" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_zone_partner" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_governance_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="fully_qualified_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybrid_secondary_usage" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybrid_secondary_usage_detected" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="instance_pool_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_general_purpose_v2" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="maintenance_configuration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_instance_create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="minimal_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="pricing_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_user_assigned_identity_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="proxy_override" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_data_endpoint_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="requested_backup_storage_redundancy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_in_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_principal" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | An ARM Resource SKU. |
| <CopyableCode code="source_managed_instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_i_ops" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_size_in_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_throughput_mbps" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="timezone_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_cores" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="zone_redundant" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of a managed instance. |
| <CopyableCode code="sku" /> | `object` | An ARM Resource SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a managed instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all managed instances in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of managed instances in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates a managed instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes a managed instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Updates a managed instance. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Failovers a managed instance. |
| <CopyableCode code="refresh_status" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Refresh external governance enablement status. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Starts the managed instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Stops the managed instance. |

## `SELECT` examples

Gets a list of all managed instances in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instances', value: 'view', },
        { label: 'managed_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrator_login,
administrator_login_password,
administrators,
authentication_metadata,
collation,
create_time,
current_backup_storage_redundancy,
database_format,
dns_zone,
dns_zone_partner,
external_governance_status,
fully_qualified_domain_name,
hybrid_secondary_usage,
hybrid_secondary_usage_detected,
identity,
instance_pool_id,
is_general_purpose_v2,
key_id,
license_type,
location,
maintenance_configuration_id,
managedInstanceName,
managed_instance_create_mode,
minimal_tls_version,
pricing_model,
primary_user_assigned_identity_id,
private_endpoint_connections,
provisioning_state,
proxy_override,
public_data_endpoint_enabled,
requested_backup_storage_redundancy,
resourceGroupName,
restore_point_in_time,
service_principal,
sku,
source_managed_instance_id,
state,
storage_i_ops,
storage_size_in_gb,
storage_throughput_mbps,
subnet_id,
subscriptionId,
tags,
timezone_id,
v_cores,
virtual_cluster_id,
zone_redundant
FROM azure.sql.vw_managed_instances
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
FROM azure.sql.managed_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_instances</code> resource.

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
INSERT INTO azure.sql.managed_instances (
managedInstanceName,
resourceGroupName,
subscriptionId,
data__location,
location,
tags,
identity,
sku,
properties
)
SELECT 
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ sku }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: identity
      value:
        - name: principalId
          value: string
        - name: type
          value: string
        - name: tenantId
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: managedInstanceCreateMode
          value: string
        - name: fullyQualifiedDomainName
          value: string
        - name: isGeneralPurposeV2
          value: boolean
        - name: administratorLogin
          value: string
        - name: administratorLoginPassword
          value: string
        - name: subnetId
          value: string
        - name: state
          value: string
        - name: licenseType
          value: string
        - name: hybridSecondaryUsage
          value: string
        - name: hybridSecondaryUsageDetected
          value: string
        - name: vCores
          value: integer
        - name: storageSizeInGB
          value: integer
        - name: storageIOps
          value: integer
        - name: storageThroughputMBps
          value: integer
        - name: collation
          value: string
        - name: dnsZone
          value: string
        - name: dnsZonePartner
          value: string
        - name: publicDataEndpointEnabled
          value: boolean
        - name: sourceManagedInstanceId
          value: string
        - name: restorePointInTime
          value: string
        - name: proxyOverride
          value: string
        - name: timezoneId
          value: string
        - name: instancePoolId
          value: string
        - name: maintenanceConfigurationId
          value: string
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: properties
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
                  - name: provisioningState
                    value: string
        - name: minimalTlsVersion
          value: string
        - name: currentBackupStorageRedundancy
          value: string
        - name: requestedBackupStorageRedundancy
          value: string
        - name: zoneRedundant
          value: boolean
        - name: primaryUserAssignedIdentityId
          value: string
        - name: keyId
          value: string
        - name: administrators
          value:
            - name: administratorType
              value: string
            - name: principalType
              value: string
            - name: login
              value: string
            - name: sid
              value: string
            - name: tenantId
              value: string
            - name: azureADOnlyAuthentication
              value: boolean
        - name: servicePrincipal
          value:
            - name: principalId
              value: string
            - name: clientId
              value: string
            - name: tenantId
              value: string
            - name: type
              value: string
        - name: virtualClusterId
          value: string
        - name: externalGovernanceStatus
          value: string
        - name: pricingModel
          value: string
        - name: createTime
          value: string
        - name: authenticationMetadata
          value: string
        - name: databaseFormat
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_instances</code> resource.

```sql
/*+ update */
UPDATE azure.sql.managed_instances
SET 
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managed_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.managed_instances
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
