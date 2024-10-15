---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - api_management
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="additional_locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_version_constraint" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_api" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="developer_portal_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="developer_portal_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_gateway" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_client_certificate" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | ETag of the resource. |
| <CopyableCode code="gateway_regional_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostname_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity properties of the Api Management service resource. |
| <CopyableCode code="legacy_portal_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="management_api_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="nat_gateway_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="notification_sender_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="outbound_public_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="platform_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="portal_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_address_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore" /> | `text` | field from the `properties` object |
| <CopyableCode code="scm_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | API Management service resource SKU properties. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="target_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type for API Management resource is set to Microsoft.ApiManagement. |
| <CopyableCode code="virtual_network_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | A list of availability zones denoting where the resource needs to come from. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="identity" /> | `object` | Identity properties of the Api Management service resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of an API Management service resource description. |
| <CopyableCode code="sku" /> | `object` | API Management service resource SKU properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type for API Management resource is set to Microsoft.ApiManagement. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting where the resource needs to come from. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets an API Management service resource description. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all API Management services within an Azure subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all API Management services within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__location, data__properties, data__sku" /> | Creates or updates an API Management service. This is long running operation and could take several minutes to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Deletes an existing API Management service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Updates an existing API Management service. |
| <CopyableCode code="apply_network_configuration_updates" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Updates the Microsoft.ApiManagement resource running in the Virtual network to pick the updated DNS changes. |
| <CopyableCode code="backup" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__backupName, data__containerName, data__storageAccount" /> | Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Checks availability and correctness of a name for an API Management service. |
| <CopyableCode code="migrate_to_stv2" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Upgrades an API Management service to the Stv2 platform. For details refer to https://aka.ms/apim-migrate-stv2. This change is not reversible. This is long running operation and could take several minutes to complete. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__backupName, data__containerName, data__storageAccount" /> | Restores a backup of an API Management service created using the ApiManagementService_Backup operation on the current service. This is a long running operation and could take several minutes to complete. |

## `SELECT` examples

Lists all API Management services within an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_locations,
api_version_constraint,
certificates,
configuration_api,
created_at_utc,
custom_properties,
developer_portal_status,
developer_portal_url,
disable_gateway,
enable_client_certificate,
etag,
gateway_regional_url,
gateway_url,
hostname_configurations,
identity,
legacy_portal_status,
location,
management_api_url,
nat_gateway_state,
notification_sender_email,
outbound_public_ip_addresses,
platform_version,
portal_url,
private_endpoint_connections,
private_ip_addresses,
provisioning_state,
public_ip_address_id,
public_ip_addresses,
public_network_access,
publisher_email,
publisher_name,
resourceGroupName,
restore,
scm_url,
serviceName,
sku,
subscriptionId,
system_data,
tags,
target_provisioning_state,
type,
virtual_network_configuration,
virtual_network_type,
zones
FROM azure.api_management.vw_services
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
location,
properties,
sku,
systemData,
tags,
type,
zones
FROM azure.api_management.services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services</code> resource.

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
INSERT INTO azure.api_management.services (
resourceGroupName,
serviceName,
subscriptionId,
data__location,
data__properties,
data__sku,
properties,
sku,
identity,
location,
zones,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ data__sku }}',
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
'{{ location }}',
'{{ zones }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: publisherEmail
          value: string
        - name: publisherName
          value: string
        - name: notificationSenderEmail
          value: string
        - name: provisioningState
          value: string
        - name: targetProvisioningState
          value: string
        - name: createdAtUtc
          value: string
        - name: gatewayUrl
          value: string
        - name: gatewayRegionalUrl
          value: string
        - name: portalUrl
          value: string
        - name: managementApiUrl
          value: string
        - name: scmUrl
          value: string
        - name: developerPortalUrl
          value: string
        - name: hostnameConfigurations
          value:
            - - name: type
                value: string
              - name: hostName
                value: string
              - name: keyVaultId
                value: string
              - name: identityClientId
                value: string
              - name: encodedCertificate
                value: string
              - name: certificatePassword
                value: string
              - name: defaultSslBinding
                value: boolean
              - name: negotiateClientCertificate
                value: boolean
              - name: certificate
                value:
                  - name: expiry
                    value: string
                  - name: thumbprint
                    value: string
                  - name: subject
                    value: string
              - name: certificateSource
                value: string
              - name: certificateStatus
                value: string
        - name: publicIPAddresses
          value:
            - string
        - name: privateIPAddresses
          value:
            - string
        - name: publicIpAddressId
          value: string
        - name: publicNetworkAccess
          value: string
        - name: configurationApi
          value:
            - name: legacyApi
              value: string
        - name: virtualNetworkConfiguration
          value:
            - name: vnetid
              value: string
            - name: subnetname
              value: string
            - name: subnetResourceId
              value: string
        - name: additionalLocations
          value:
            - - name: location
                value: string
              - name: sku
                value:
                  - name: name
                    value: string
                  - name: capacity
                    value: integer
              - name: zones
                value:
                  - string
              - name: publicIPAddresses
                value:
                  - string
              - name: privateIPAddresses
                value:
                  - string
              - name: publicIpAddressId
                value: string
              - name: gatewayRegionalUrl
                value: string
              - name: natGatewayState
                value: string
              - name: outboundPublicIPAddresses
                value:
                  - string
              - name: disableGateway
                value: boolean
              - name: platformVersion
                value: string
        - name: customProperties
          value: object
        - name: certificates
          value:
            - - name: encodedCertificate
                value: string
              - name: certificatePassword
                value: string
              - name: storeName
                value: string
        - name: enableClientCertificate
          value: boolean
        - name: natGatewayState
          value: string
        - name: outboundPublicIPAddresses
          value:
            - string
        - name: disableGateway
          value: boolean
        - name: virtualNetworkType
          value: string
        - name: apiVersionConstraint
          value:
            - name: minApiVersion
              value: string
        - name: restore
          value: boolean
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
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: string
                  - name: groupIds
                    value:
                      - string
        - name: platformVersion
          value: string
        - name: legacyPortalStatus
          value: string
        - name: developerPortalStatus
          value: string
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: object
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
    - name: location
      value: string
    - name: etag
      value: string
    - name: zones
      value:
        - string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.services
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
zones = '{{ zones }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
