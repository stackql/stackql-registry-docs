---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - spring_apps
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.services" /></td></tr>
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
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (either system assigned, or none) |
| <CopyableCode code="infra_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The GEO location of the resource. |
| <CopyableCode code="maintenance_schedule_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_environment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Sku of Azure Spring Apps |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags of the service which is a list of key value pairs that describe the resource. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_addons" /> | `text` | field from the `properties` object |
| <CopyableCode code="zone_redundant" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (either system assigned, or none) |
| <CopyableCode code="location" /> | `string` | The GEO location of the resource. |
| <CopyableCode code="properties" /> | `object` | Service properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
| <CopyableCode code="tags" /> | `object` | Tags of the service which is a list of key value pairs that describe the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get a Service and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Handles requests to list all resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Handles requests to list all resources in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Create a new Service or update an exiting Service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Operation to delete a Service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Operation to update an exiting Service. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks that the resource name is valid and is not already in use. |
| <CopyableCode code="disable_apm_globally" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__resourceId" /> | Disable an APM globally. |
| <CopyableCode code="disable_test_endpoint" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Disable test endpoint functionality for a Service. |
| <CopyableCode code="enable_apm_globally" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__resourceId" /> | Enable an APM globally. |
| <CopyableCode code="enable_test_endpoint" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Enable test endpoint functionality for a Service. |
| <CopyableCode code="flush_vnet_dns_setting" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Flush Virtual Network DNS settings for a VNET injected Service. |
| <CopyableCode code="regenerate_test_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__keyType" /> | Regenerate a test key for a Service. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Start a Service. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Stop a Service. |

## `SELECT` examples

Handles requests to list all resources in a subscription.

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
fqdn,
identity,
infra_resource_group,
location,
maintenance_schedule_configuration,
managed_environment_id,
marketplace_resource,
network_profile,
power_state,
provisioning_state,
resourceGroupName,
serviceName,
service_id,
sku,
subscriptionId,
tags,
version,
vnet_addons,
zone_redundant
FROM azure.spring_apps.vw_services
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
FROM azure.spring_apps.services
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
INSERT INTO azure.spring_apps.services (
resourceGroupName,
serviceName,
subscriptionId,
location,
tags,
properties,
identity,
sku
)
SELECT 
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ identity }}',
'{{ sku }}'
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
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: networkProfile
          value:
            - name: serviceRuntimeSubnetId
              value: string
            - name: appSubnetId
              value: string
            - name: serviceCidr
              value: string
            - name: serviceRuntimeNetworkResourceGroup
              value: string
            - name: appNetworkResourceGroup
              value: string
            - name: outboundIPs
              value:
                - name: publicIPs
                  value:
                    - string
            - name: requiredTraffics
              value:
                - - name: protocol
                    value: string
                  - name: port
                    value: integer
                  - name: ips
                    value:
                      - string
                  - name: fqdns
                    value:
                      - string
                  - name: direction
                    value: string
            - name: ingressConfig
              value:
                - name: readTimeoutInSeconds
                  value: integer
            - name: outboundType
              value: string
        - name: vnetAddons
          value:
            - name: logStreamPublicEndpoint
              value: boolean
            - name: dataPlanePublicEndpoint
              value: boolean
            - name: privateStorageAccess
              value: string
            - name: privateDnsZoneId
              value: string
        - name: maintenanceScheduleConfiguration
          value:
            - name: frequency
              value: string
        - name: version
          value: integer
        - name: serviceId
          value: string
        - name: managedEnvironmentId
          value: string
        - name: infraResourceGroup
          value: string
        - name: powerState
          value: string
        - name: zoneRedundant
          value: boolean
        - name: fqdn
          value: string
        - name: marketplaceResource
          value:
            - name: plan
              value: string
            - name: publisher
              value: string
            - name: product
              value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE azure.spring_apps.services
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
