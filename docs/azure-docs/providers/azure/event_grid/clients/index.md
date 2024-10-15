---
title: clients
hide_title: false
hide_table_of_contents: false
keywords:
  - clients
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>clients</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.clients" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clients', value: 'view', },
        { label: 'clients', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="attributes" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="clientName" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_certificate_authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="namespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of client. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clientName, namespaceName, resourceGroupName, subscriptionId" /> | Get properties of a client. |
| <CopyableCode code="list_by_namespace" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Get all the permission bindings under a namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clientName, namespaceName, resourceGroupName, subscriptionId" /> | Create or update a client with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clientName, namespaceName, resourceGroupName, subscriptionId" /> | Delete an existing client. |

## `SELECT` examples

Get all the permission bindings under a namespace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clients', value: 'view', },
        { label: 'clients', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
attributes,
authentication_name,
clientName,
client_certificate_authentication,
namespaceName,
provisioning_state,
resourceGroupName,
state,
subscriptionId,
system_data,
type
FROM azure.event_grid.vw_clients
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.event_grid.clients
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clients</code> resource.

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
INSERT INTO azure.event_grid.clients (
clientName,
namespaceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ clientName }}',
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: description
          value: string
        - name: authenticationName
          value: string
        - name: clientCertificateAuthentication
          value:
            - name: validationScheme
              value: string
            - name: allowedThumbprints
              value:
                - string
        - name: state
          value: string
        - name: attributes
          value: object
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>clients</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_grid.clients
WHERE clientName = '{{ clientName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
