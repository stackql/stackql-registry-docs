---
title: network_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_functions
  - hybrid_network
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

Creates, updates, deletes, gets or lists a <code>network_functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.network_functions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_functions', value: 'view', },
        { label: 'network_functions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allow_software_update" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="networkFunctionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_function_definition_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_function_definition_offering_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_function_definition_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_function_definition_version_resource_reference" /> | `text` | field from the `properties` object |
| <CopyableCode code="nfvi_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="nfvi_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_override_values" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network function properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Gets information about the specified network function resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the network function resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the network functions in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Creates or updates a network function resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Deletes the specified network function resource. |
| <CopyableCode code="execute_request" /> | `EXEC` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId, data__requestMetadata, data__serviceEndpoint" /> | Execute a request to services on a containerized network function. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Updates the tags for the network function resource. |

## `SELECT` examples

Lists all the network functions in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_functions', value: 'view', },
        { label: 'network_functions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allow_software_update,
configuration_type,
etag,
identity,
location,
networkFunctionName,
network_function_definition_group_name,
network_function_definition_offering_location,
network_function_definition_version,
network_function_definition_version_resource_reference,
nfvi_id,
nfvi_type,
provisioning_state,
publisher_name,
publisher_scope,
resourceGroupName,
role_override_values,
subscriptionId,
tags
FROM azure.hybrid_network.vw_network_functions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
location,
properties,
tags
FROM azure.hybrid_network.network_functions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_functions</code> resource.

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
INSERT INTO azure.hybrid_network.network_functions (
networkFunctionName,
resourceGroupName,
subscriptionId,
properties,
etag,
identity,
tags,
location
)
SELECT 
'{{ networkFunctionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ etag }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}'
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
        - name: publisherName
          value: string
        - name: publisherScope
          value: []
        - name: networkFunctionDefinitionGroupName
          value: string
        - name: networkFunctionDefinitionVersion
          value: string
        - name: networkFunctionDefinitionOfferingLocation
          value: string
        - name: networkFunctionDefinitionVersionResourceReference
          value:
            - name: idType
              value: []
        - name: nfviType
          value: []
        - name: nfviId
          value: string
        - name: allowSoftwareUpdate
          value: boolean
        - name: configurationType
          value: []
        - name: roleOverrideValues
          value:
            - []
    - name: etag
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
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>network_functions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_network.network_functions
WHERE networkFunctionName = '{{ networkFunctionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
