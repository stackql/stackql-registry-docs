---
title: configuration_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_stores
  - app_configuration
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

Creates, updates, deletes, gets or lists a <code>configuration_stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.configuration_stores" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_stores', value: 'view', },
        { label: 'configuration_stores', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configStoreName" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_plane_proxy" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_purge_protection" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | An identity that can be associated with a resource. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Describes a configuration store SKU. |
| <CopyableCode code="soft_delete_retention_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | An identity that can be associated with a resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a configuration store. |
| <CopyableCode code="sku" /> | `object` | Describes a configuration store SKU. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified configuration store. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the configuration stores for a given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the configuration stores for a given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId, data__location, data__sku" /> | Creates a configuration store with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Deletes a configuration store. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Updates a configuration store with the specified parameters. |
| <CopyableCode code="purge_deleted" /> | `EXEC` | <CopyableCode code="configStoreName, location, subscriptionId" /> | Permanently deletes the specified configuration store. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Regenerates an access key for the specified configuration store. |

## `SELECT` examples

Lists the configuration stores for a given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_stores', value: 'view', },
        { label: 'configuration_stores', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
configStoreName,
create_mode,
creation_date,
data_plane_proxy,
disable_local_auth,
enable_purge_protection,
encryption,
endpoint,
identity,
location,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
sku,
soft_delete_retention_in_days,
subscriptionId,
system_data,
tags
FROM azure.app_configuration.vw_configuration_stores
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
systemData,
tags
FROM azure.app_configuration.configuration_stores
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_stores</code> resource.

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
INSERT INTO azure.app_configuration.configuration_stores (
configStoreName,
resourceGroupName,
subscriptionId,
data__location,
data__sku,
tags,
location,
identity,
properties,
sku,
systemData
)
SELECT 
'{{ configStoreName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__sku }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
'{{ properties }}',
'{{ sku }}',
'{{ systemData }}'
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
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
        - name: principalId
          value: string
        - name: tenantId
          value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: creationDate
          value: string
        - name: endpoint
          value: string
        - name: encryption
          value:
            - name: keyVaultProperties
              value:
                - name: keyIdentifier
                  value: string
                - name: identityClientId
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
                  - name: provisioningState
                    value: string
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
        - name: publicNetworkAccess
          value: string
        - name: disableLocalAuth
          value: boolean
        - name: softDeleteRetentionInDays
          value: integer
        - name: enablePurgeProtection
          value: boolean
        - name: dataPlaneProxy
          value:
            - name: authenticationMode
              value: string
            - name: privateLinkDelegation
              value: string
        - name: createMode
          value: string
    - name: sku
      value:
        - name: name
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>configuration_stores</code> resource.

```sql
/*+ update */
UPDATE azure.app_configuration.configuration_stores
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
configStoreName = '{{ configStoreName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>configuration_stores</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_configuration.configuration_stores
WHERE configStoreName = '{{ configStoreName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
