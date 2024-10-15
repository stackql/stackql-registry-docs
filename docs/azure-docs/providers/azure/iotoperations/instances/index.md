---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - iotoperations
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

Creates, updates, deletes, gets or lists a <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotoperations.instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_instances', value: 'view', },
        { label: 'instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="components" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema_registry_namespace" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of the Instance resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Get a InstanceResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List InstanceResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List InstanceResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a InstanceResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Delete a InstanceResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Update a InstanceResource |

## `SELECT` examples

List InstanceResource resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_instances', value: 'view', },
        { label: 'instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
components,
extended_location,
identity,
instanceName,
location,
provisioning_state,
resourceGroupName,
schema_registry_namespace,
subscriptionId,
tags,
version
FROM azure.iotoperations.vw_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
identity,
location,
properties,
tags
FROM azure.iotoperations.instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances</code> resource.

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
INSERT INTO azure.iotoperations.instances (
instanceName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
identity,
tags,
location
)
SELECT 
'{{ instanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}',
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
        - name: description
          value: string
        - name: provisioningState
          value: []
        - name: version
          value: string
        - name: schemaRegistryNamespace
          value: string
        - name: components
          value:
            - name: adr
              value:
                - name: state
                  value: []
            - name: akri
              value: []
            - name: connectors
              value: []
            - name: dataflows
              value: []
            - name: schemaRegistry
              value: []
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
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

## `UPDATE` example

Updates a <code>instances</code> resource.

```sql
/*+ update */
UPDATE azure.iotoperations.instances
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iotoperations.instances
WHERE instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
