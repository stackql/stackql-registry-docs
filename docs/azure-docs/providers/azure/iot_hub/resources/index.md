---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - iot_hub
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

Creates, updates, deletes, gets or lists a <code>resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resources', value: 'view', },
        { label: 'resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="allowed_fqdn_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_to_device" /> | `text` | field from the `properties` object |
| <CopyableCode code="comments" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_device_sas" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_module_sas" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_data_residency" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_file_upload_notifications" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| <CopyableCode code="event_hub_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="features" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_filter_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="messaging_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_rule_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restrict_outbound_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Information about the SKU of the IoT hub. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| <CopyableCode code="identity" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of an IoT hub. |
| <CopyableCode code="sku" /> | `object` | Information about the SKU of the IoT hub. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get the non-security related metadata of an IoT hub. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the IoT hubs in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the IoT hubs in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, data__sku" /> | Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub. If certain properties are missing in the JSON, updating IoT Hub may cause these values to fallback to default, which may lead to unexpected behavior. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Delete an IoT hub. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Update an existing IoT Hub tags. to update other fields use the CreateOrUpdate method |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Check if an IoT hub name is available. |
| <CopyableCode code="export_devices" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, data__excludeKeys, data__exportBlobContainerUri" /> | Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities. |
| <CopyableCode code="import_devices" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, data__inputBlobContainerUri, data__outputBlobContainerUri" /> | Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities. |
| <CopyableCode code="test_all_routes" /> | `EXEC` | <CopyableCode code="iotHubName, resourceGroupName, subscriptionId" /> | Test all routes configured in this Iot Hub |
| <CopyableCode code="test_route" /> | `EXEC` | <CopyableCode code="iotHubName, resourceGroupName, subscriptionId, data__route" /> | Test the new route for this Iot Hub |

## `SELECT` examples

Get all the IoT hubs in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resources', value: 'view', },
        { label: 'resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allowed_fqdn_list,
authorization_policies,
cloud_to_device,
comments,
disable_device_sas,
disable_local_auth,
disable_module_sas,
enable_data_residency,
enable_file_upload_notifications,
etag,
event_hub_endpoints,
features,
host_name,
identity,
ip_filter_rules,
location,
locations,
messaging_endpoints,
min_tls_version,
network_rule_sets,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
resourceName,
restrict_outbound_network_access,
routing,
sku,
state,
storage_endpoints,
subscriptionId,
system_data,
tags,
type
FROM azure.iot_hub.vw_resources
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
type
FROM azure.iot_hub.resources
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resources</code> resource.

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
INSERT INTO azure.iot_hub.resources (
resourceGroupName,
resourceName,
subscriptionId,
data__sku,
etag,
properties,
sku,
identity,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ data__sku }}',
'{{ etag }}',
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
'{{ location }}',
'{{ tags }}'
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
        - name: disableLocalAuth
          value: boolean
        - name: disableDeviceSAS
          value: boolean
        - name: disableModuleSAS
          value: boolean
        - name: restrictOutboundNetworkAccess
          value: boolean
        - name: allowedFqdnList
          value:
            - string
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
        - name: networkRuleSets
          value:
            - name: defaultAction
              value: string
            - name: applyToBuiltInEventHubEndpoint
              value: boolean
            - name: ipRules
              value:
                - - name: filterName
                    value: string
                  - name: action
                    value: string
                  - name: ipMask
                    value: string
        - name: minTlsVersion
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
        - name: provisioningState
          value: string
        - name: state
          value: string
        - name: hostName
          value: string
        - name: eventHubEndpoints
          value: object
        - name: routing
          value:
            - name: endpoints
              value:
                - name: serviceBusQueues
                  value:
                    - - name: id
                        value: string
                      - name: connectionString
                        value: string
                      - name: endpointUri
                        value: string
                      - name: entityPath
                        value: string
                      - name: authenticationType
                        value: string
                      - name: identity
                        value:
                          - name: userAssignedIdentity
                            value: string
                      - name: name
                        value: string
                      - name: subscriptionId
                        value: string
                      - name: resourceGroup
                        value: string
                - name: serviceBusTopics
                  value:
                    - - name: id
                        value: string
                      - name: connectionString
                        value: string
                      - name: endpointUri
                        value: string
                      - name: entityPath
                        value: string
                      - name: authenticationType
                        value: string
                      - name: name
                        value: string
                      - name: subscriptionId
                        value: string
                      - name: resourceGroup
                        value: string
                - name: eventHubs
                  value:
                    - - name: id
                        value: string
                      - name: connectionString
                        value: string
                      - name: endpointUri
                        value: string
                      - name: entityPath
                        value: string
                      - name: authenticationType
                        value: string
                      - name: name
                        value: string
                      - name: subscriptionId
                        value: string
                      - name: resourceGroup
                        value: string
                - name: storageContainers
                  value:
                    - - name: id
                        value: string
                      - name: connectionString
                        value: string
                      - name: endpointUri
                        value: string
                      - name: authenticationType
                        value: string
                      - name: name
                        value: string
                      - name: subscriptionId
                        value: string
                      - name: resourceGroup
                        value: string
                      - name: containerName
                        value: string
                      - name: fileNameFormat
                        value: string
                      - name: batchFrequencyInSeconds
                        value: integer
                      - name: maxChunkSizeInBytes
                        value: integer
                      - name: encoding
                        value: string
                - name: cosmosDBSqlContainers
                  value:
                    - - name: name
                        value: string
                      - name: id
                        value: string
                      - name: subscriptionId
                        value: string
                      - name: resourceGroup
                        value: string
                      - name: endpointUri
                        value: string
                      - name: authenticationType
                        value: string
                      - name: primaryKey
                        value: string
                      - name: secondaryKey
                        value: string
                      - name: databaseName
                        value: string
                      - name: containerName
                        value: string
                      - name: partitionKeyName
                        value: string
                      - name: partitionKeyTemplate
                        value: string
            - name: routes
              value:
                - - name: name
                    value: string
                  - name: source
                    value: string
                  - name: condition
                    value: string
                  - name: endpointNames
                    value:
                      - string
                  - name: isEnabled
                    value: boolean
            - name: fallbackRoute
              value:
                - name: name
                  value: string
                - name: source
                  value: string
                - name: condition
                  value: string
                - name: endpointNames
                  value:
                    - string
                - name: isEnabled
                  value: boolean
            - name: enrichments
              value:
                - - name: key
                    value: string
                  - name: value
                    value: string
                  - name: endpointNames
                    value:
                      - string
        - name: storageEndpoints
          value: object
        - name: messagingEndpoints
          value: object
        - name: enableFileUploadNotifications
          value: boolean
        - name: cloudToDevice
          value:
            - name: maxDeliveryCount
              value: integer
            - name: defaultTtlAsIso8601
              value: string
            - name: feedback
              value:
                - name: lockDurationAsIso8601
                  value: string
                - name: ttlAsIso8601
                  value: string
                - name: maxDeliveryCount
                  value: integer
        - name: comments
          value: string
        - name: features
          value: string
        - name: locations
          value:
            - - name: location
                value: string
              - name: role
                value: string
        - name: enableDataResidency
          value: boolean
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>resources</code> resource.

```sql
/*+ update */
UPDATE azure.iot_hub.resources
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_hub.resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
