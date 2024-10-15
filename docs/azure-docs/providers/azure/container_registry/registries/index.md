---
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
  - container_registry
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.registries" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="admin_user_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="anonymous_pull_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_endpoint_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_endpoint_host_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed identity for the resource. |
| <CopyableCode code="login_server" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata_search" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_rule_bypass_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_rule_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="zone_redundancy" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of a container registry. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified container registry. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the container registries under the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the container registries under the specified resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, data__sku" /> | Creates a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Deletes a container registry. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Updates a container registry with the specified parameters. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks whether the container registry name is available for use. The name must contain only alphanumeric characters, be globally unique, and between 5 and 50 characters in length. |
| <CopyableCode code="generate_credentials" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Generate keys for a token of a specified container registry. |
| <CopyableCode code="import_image" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, data__source" /> | Copies an image to this container registry from the specified container registry. |
| <CopyableCode code="regenerate_credential" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, data__name" /> | Regenerates one of the login credentials for the specified container registry. |
| <CopyableCode code="schedule_run" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, data__type" /> | Schedules a new run based on the request parameters and add it to the run queue. |

## `SELECT` examples

Lists all the container registries under the specified subscription.

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
id,
name,
admin_user_enabled,
anonymous_pull_enabled,
creation_date,
data_endpoint_enabled,
data_endpoint_host_names,
encryption,
identity,
login_server,
metadata_search,
network_rule_bypass_options,
network_rule_set,
policies,
private_endpoint_connections,
provisioning_state,
public_network_access,
registryName,
resourceGroupName,
sku,
status,
subscriptionId,
system_data,
type,
zone_redundancy
FROM azure.container_registry.vw_registries
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
properties,
sku,
systemData,
type
FROM azure.container_registry.registries
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
INSERT INTO azure.container_registry.registries (
registryName,
resourceGroupName,
subscriptionId,
data__sku,
sku,
identity,
properties
)
SELECT 
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__sku }}',
'{{ sku }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
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
        - name: loginServer
          value: string
        - name: creationDate
          value: string
        - name: provisioningState
          value: string
        - name: status
          value:
            - name: displayStatus
              value: string
            - name: message
              value: string
            - name: timestamp
              value: string
        - name: adminUserEnabled
          value: boolean
        - name: networkRuleSet
          value:
            - name: defaultAction
              value: string
            - name: ipRules
              value:
                - - name: action
                    value: string
                  - name: value
                    value: string
        - name: policies
          value:
            - name: quarantinePolicy
              value:
                - name: status
                  value: string
            - name: trustPolicy
              value:
                - name: type
                  value: string
                - name: status
                  value: string
            - name: retentionPolicy
              value:
                - name: days
                  value: integer
                - name: lastUpdatedTime
                  value: string
                - name: status
                  value: string
            - name: exportPolicy
              value:
                - name: status
                  value: string
            - name: azureADAuthenticationAsArmPolicy
              value:
                - name: status
                  value: string
            - name: softDeletePolicy
              value:
                - name: retentionDays
                  value: integer
                - name: lastUpdatedTime
                  value: string
                - name: status
                  value: string
        - name: encryption
          value:
            - name: status
              value: string
            - name: keyVaultProperties
              value:
                - name: keyIdentifier
                  value: string
                - name: identity
                  value: string
        - name: dataEndpointEnabled
          value: boolean
        - name: dataEndpointHostNames
          value:
            - string
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
                  - name: provisioningState
                    value: string
        - name: publicNetworkAccess
          value: string
        - name: networkRuleBypassOptions
          value: string
        - name: zoneRedundancy
          value: string
        - name: anonymousPullEnabled
          value: boolean
        - name: metadataSearch
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>registries</code> resource.

```sql
/*+ update */
UPDATE azure.container_registry.registries
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>registries</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.registries
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
