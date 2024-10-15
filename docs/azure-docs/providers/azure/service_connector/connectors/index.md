---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - service_connector
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

Creates, updates, deletes, gets or lists a <code>connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_connector.connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connectors', value: 'view', },
        { label: 'connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auth_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_solution" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_store" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_service" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_solution" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the Linker. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId" /> | Returns Connector resource for a given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns list of connector which connects to the resource, which supports to config the target service during the resource provision. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId, data__properties" /> | Create or update Connector resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId" /> | Delete a Connector. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId" /> | Operation to update an existing Connector. |
| <CopyableCode code="generate_configurations" /> | `EXEC` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId" /> | Generate configurations for a Connector. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId" /> | Validate a Connector. |

## `SELECT` examples

Returns list of connector which connects to the resource, which supports to config the target service during the resource provision.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connectors', value: 'view', },
        { label: 'connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auth_info,
client_type,
configuration_info,
connectorName,
location,
provisioning_state,
public_network_solution,
resourceGroupName,
scope,
secret_store,
subscriptionId,
system_data,
target_service,
vnet_solution
FROM azure.service_connector.vw_connectors
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.service_connector.connectors
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connectors</code> resource.

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
INSERT INTO azure.service_connector.connectors (
connectorName,
location,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ connectorName }}',
'{{ location }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: targetService
          value:
            - name: type
              value: []
        - name: authInfo
          value:
            - name: authType
              value: []
            - name: authMode
              value: []
        - name: clientType
          value: []
        - name: provisioningState
          value: string
        - name: vNetSolution
          value:
            - name: type
              value: string
            - name: deleteOrUpdateBehavior
              value: []
        - name: secretStore
          value:
            - name: keyVaultId
              value: string
            - name: keyVaultSecretName
              value: string
        - name: scope
          value: string
        - name: publicNetworkSolution
          value:
            - name: action
              value: []
            - name: firewallRules
              value:
                - name: ipRanges
                  value:
                    - string
                - name: azureServices
                  value: []
        - name: configurationInfo
          value:
            - name: customizedKeys
              value: object
            - name: daprProperties
              value:
                - name: version
                  value: string
                - name: componentType
                  value: string
                - name: secretStoreComponent
                  value: string
                - name: metadata
                  value:
                    - - name: name
                        value: string
                      - name: value
                        value: string
                      - name: secretRef
                        value: string
                      - name: description
                        value: string
                      - name: required
                        value: string
                - name: scopes
                  value:
                    - string
                - name: runtimeVersion
                  value: string
                - name: bindingComponentDirection
                  value: string
            - name: additionalConfigurations
              value: object
            - name: additionalConnectionStringProperties
              value: object
            - name: configurationStore
              value:
                - name: appConfigurationId
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

Updates a <code>connectors</code> resource.

```sql
/*+ update */
UPDATE azure.service_connector.connectors
SET 
properties = '{{ properties }}'
WHERE 
connectorName = '{{ connectorName }}'
AND location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_connector.connectors
WHERE connectorName = '{{ connectorName }}'
AND location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
