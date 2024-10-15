---
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>registries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.registries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registries', value: 'view', },
        { label: 'registries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="discovery_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="intellectual_property_publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_resource_group_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="ml_flow_registry_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="region_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="registry_private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of the Registry |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, data__location, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="remove_regions" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, data__location, data__properties" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registries', value: 'view', },
        { label: 'registries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
discovery_url,
identity,
intellectual_property_publisher,
kind,
location,
managed_resource_group,
managed_resource_group_settings,
ml_flow_registry_uri,
public_network_access,
region_details,
registryName,
registry_private_endpoint_connections,
resourceGroupName,
sku,
subscriptionId,
tags
FROM azure.ml_services.vw_registries
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
kind,
location,
properties,
sku,
tags
FROM azure.ml_services.registries
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registries</code> resource.

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
INSERT INTO azure.ml_services.registries (
registryName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
tags,
location,
identity,
kind,
properties,
sku
)
SELECT 
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
'{{ kind }}',
'{{ properties }}',
'{{ sku }}'
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
    - name: kind
      value: string
    - name: properties
      value:
        - name: discoveryUrl
          value: string
        - name: intellectualPropertyPublisher
          value: string
        - name: managedResourceGroup
          value:
            - name: resourceId
              value: string
        - name: managedResourceGroupSettings
          value:
            - name: assignedIdentities
              value:
                - - name: principalId
                    value: string
        - name: mlFlowRegistryUri
          value: string
        - name: registryPrivateEndpointConnections
          value:
            - - name: id
                value: string
              - name: location
                value: string
              - name: properties
                value:
                  - name: groupIds
                    value:
                      - string
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                      - name: subnetArmId
                        value: string
                  - name: registryPrivateLinkServiceConnectionState
                    value:
                      - name: actionsRequired
                        value: string
                      - name: description
                        value: string
                      - name: status
                        value: []
                  - name: provisioningState
                    value: string
        - name: publicNetworkAccess
          value: string
        - name: regionDetails
          value:
            - - name: acrDetails
                value:
                  - - name: systemCreatedAcrAccount
                      value:
                        - name: acrAccountName
                          value: string
                        - name: acrAccountSku
                          value: string
                    - name: userCreatedAcrAccount
                      value: []
              - name: location
                value: string
              - name: storageAccountDetails
                value:
                  - - name: systemCreatedStorageAccount
                      value:
                        - name: allowBlobPublicAccess
                          value: boolean
                        - name: storageAccountHnsEnabled
                          value: boolean
                        - name: storageAccountName
                          value: string
                        - name: storageAccountType
                          value: string
                    - name: userCreatedStorageAccount
                      value: []
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>registries</code> resource.

```sql
/*+ update */
UPDATE azure.ml_services.registries
SET 
identity = '{{ identity }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>registries</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.registries
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
