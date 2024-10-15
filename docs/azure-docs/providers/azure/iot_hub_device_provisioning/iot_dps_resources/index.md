---
title: iot_dps_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resources
  - iot_hub_device_provisioning
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

Creates, updates, deletes, gets or lists a <code>iot_dps_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_dps_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub_device_provisioning.iot_dps_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_dps_resources', value: 'view', },
        { label: 'iot_dps_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="allocation_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_provisioning_host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_data_residency" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| <CopyableCode code="id_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="iot_hubs" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_filter_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="portal_operations_host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioningServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_operations_host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | List of possible provisioning service SKUs. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="properties" /> | `object` | the service specific properties of a provisioning service, including keys, linked iot hubs, current state, and system generated properties such as hostname and idScope |
| <CopyableCode code="sku" /> | `object` | List of possible provisioning service SKUs. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="provisioningServiceName, resourceGroupName, subscriptionId" /> | Get the metadata of the provisioning service without SAS keys. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of all provisioning services in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the provisioning services for a given subscription id. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="provisioningServiceName, resourceGroupName, subscriptionId, data__properties, data__sku" /> | Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="provisioningServiceName, resourceGroupName, subscriptionId" /> | Deletes the Provisioning Service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="provisioningServiceName, resourceGroupName, subscriptionId" /> | Update an existing provisioning service's tags. to update other fields use the CreateOrUpdate method |
| <CopyableCode code="check_provisioning_service_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Check if a provisioning service name is available. This will validate if the name is syntactically valid and if the name is usable |

## `SELECT` examples

List all the provisioning services for a given subscription id.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_dps_resources', value: 'view', },
        { label: 'iot_dps_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allocation_policy,
authorization_policies,
device_provisioning_host_name,
enable_data_residency,
etag,
id_scope,
identity,
iot_hubs,
ip_filter_rules,
portal_operations_host_name,
private_endpoint_connections,
provisioningServiceName,
provisioning_state,
public_network_access,
resourceGroupName,
service_operations_host_name,
sku,
state,
subscriptionId,
system_data,
type
FROM azure.iot_hub_device_provisioning.vw_iot_dps_resources
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
properties,
sku,
systemData,
type
FROM azure.iot_hub_device_provisioning.iot_dps_resources
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>iot_dps_resources</code> resource.

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
INSERT INTO azure.iot_hub_device_provisioning.iot_dps_resources (
provisioningServiceName,
resourceGroupName,
subscriptionId,
data__properties,
data__sku,
etag,
properties,
sku,
identity
)
SELECT 
'{{ provisioningServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ data__sku }}',
'{{ etag }}',
'{{ properties }}',
'{{ sku }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: state
          value: string
        - name: publicNetworkAccess
          value: string
        - name: ipFilterRules
          value:
            - - name: filterName
                value: string
              - name: action
                value: string
              - name: ipMask
                value: string
              - name: target
                value: string
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
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
        - name: provisioningState
          value: string
        - name: iotHubs
          value:
            - - name: applyAllocationPolicy
                value: boolean
              - name: allocationWeight
                value: integer
              - name: name
                value: string
              - name: connectionString
                value: string
              - name: location
                value: string
        - name: allocationPolicy
          value: string
        - name: serviceOperationsHostName
          value: string
        - name: deviceProvisioningHostName
          value: string
        - name: idScope
          value: string
        - name: authorizationPolicies
          value:
            - - name: keyName
                value: string
              - name: primaryKey
                value: string
              - name: secondaryKey
                value: string
              - name: rights
                value: string
        - name: enableDataResidency
          value: boolean
        - name: portalOperationsHostName
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>iot_dps_resources</code> resource.

```sql
/*+ update */
UPDATE azure.iot_hub_device_provisioning.iot_dps_resources
SET 
tags = '{{ tags }}'
WHERE 
provisioningServiceName = '{{ provisioningServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>iot_dps_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_hub_device_provisioning.iot_dps_resources
WHERE provisioningServiceName = '{{ provisioningServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
