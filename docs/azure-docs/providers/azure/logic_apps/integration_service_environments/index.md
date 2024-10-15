---
title: integration_service_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environments
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_service_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_service_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_service_environments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_service_environments', value: 'view', },
        { label: 'integration_service_environments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="encryption_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity properties. |
| <CopyableCode code="integrationServiceEnvironmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="integration_service_environment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="network_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroup" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The integration service environment sku. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="identity" /> | `object` | Managed service identity properties. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration service environment properties. |
| <CopyableCode code="sku" /> | `object` | The integration service environment sku. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Gets an integration service environment. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroup, subscriptionId" /> | Gets a list of integration service environments by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of integration service environments by subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Creates or updates an integration service environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Deletes an integration service environment. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Updates an integration service environment. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Restarts an integration service environment. |

## `SELECT` examples

Gets a list of integration service environments by subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_service_environments', value: 'view', },
        { label: 'integration_service_environments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
encryption_configuration,
endpoints_configuration,
identity,
integrationServiceEnvironmentName,
integration_service_environment_id,
location,
network_configuration,
provisioning_state,
resourceGroup,
sku,
state,
subscriptionId,
tags,
type
FROM azure.logic_apps.vw_integration_service_environments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
sku,
tags,
type
FROM azure.logic_apps.integration_service_environments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_service_environments</code> resource.

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
INSERT INTO azure.logic_apps.integration_service_environments (
integrationServiceEnvironmentName,
resourceGroup,
subscriptionId,
properties,
sku,
identity,
location,
tags
)
SELECT 
'{{ integrationServiceEnvironmentName }}',
'{{ resourceGroup }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: state
          value: []
        - name: integrationServiceEnvironmentId
          value: string
        - name: endpointsConfiguration
          value:
            - name: workflow
              value:
                - name: outgoingIpAddresses
                  value:
                    - - name: address
                        value: string
                - name: accessEndpointIpAddresses
                  value:
                    - - name: address
                        value: string
        - name: networkConfiguration
          value:
            - name: virtualNetworkAddressSpace
              value: string
            - name: accessEndpoint
              value:
                - name: type
                  value: []
            - name: subnets
              value:
                - - name: id
                    value: string
                  - name: name
                    value: string
                  - name: type
                    value: string
        - name: encryptionConfiguration
          value:
            - name: encryptionKeyReference
              value:
                - name: keyVault
                  value:
                    - name: id
                      value: string
                    - name: name
                      value: string
                    - name: type
                      value: string
                - name: keyName
                  value: string
                - name: keyVersion
                  value: string
    - name: sku
      value:
        - name: name
          value: []
        - name: capacity
          value: integer
    - name: identity
      value:
        - name: type
          value: string
        - name: tenantId
          value: string
        - name: principalId
          value: string
        - name: userAssignedIdentities
          value: object
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

Updates a <code>integration_service_environments</code> resource.

```sql
/*+ update */
UPDATE azure.logic_apps.integration_service_environments
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
integrationServiceEnvironmentName = '{{ integrationServiceEnvironmentName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>integration_service_environments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.logic_apps.integration_service_environments
WHERE integrationServiceEnvironmentName = '{{ integrationServiceEnvironmentName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
