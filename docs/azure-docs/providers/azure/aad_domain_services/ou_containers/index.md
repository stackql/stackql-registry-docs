---
title: ou_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - ou_containers
  - aad_domain_services
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

Creates, updates, deletes, gets or lists a <code>ou_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ou_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aad_domain_services.ou_containers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ou_containers', value: 'view', },
        { label: 'ou_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="distinguished_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="domainServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="ouContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the OuContainer. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainServiceName, ouContainerName, resourceGroupName, subscriptionId" /> | Get OuContainer in DomainService instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="domainServiceName, resourceGroupName, subscriptionId" /> | The List of OuContainers in DomainService instance. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="domainServiceName, ouContainerName, resourceGroupName, subscriptionId" /> | The Create OuContainer operation creates a new OuContainer under the specified Domain Service instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainServiceName, ouContainerName, resourceGroupName, subscriptionId" /> | The Delete OuContainer operation deletes specified OuContainer. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="domainServiceName, ouContainerName, resourceGroupName, subscriptionId" /> | The Update OuContainer operation can be used to update the existing OuContainers. |

## `SELECT` examples

The List of OuContainers in DomainService instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ou_containers', value: 'view', },
        { label: 'ou_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accounts,
container_id,
deployment_id,
distinguished_name,
domainServiceName,
domain_name,
ouContainerName,
provisioning_state,
resourceGroupName,
service_status,
subscriptionId,
tenant_id,
type
FROM azure.aad_domain_services.vw_ou_containers
WHERE domainServiceName = '{{ domainServiceName }}'
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
type
FROM azure.aad_domain_services.ou_containers
WHERE domainServiceName = '{{ domainServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ou_containers</code> resource.

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
INSERT INTO azure.aad_domain_services.ou_containers (
domainServiceName,
ouContainerName,
resourceGroupName,
subscriptionId,
accountName,
spn,
password
)
SELECT 
'{{ domainServiceName }}',
'{{ ouContainerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ accountName }}',
'{{ spn }}',
'{{ password }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: accountName
      value: string
    - name: spn
      value: string
    - name: password
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>ou_containers</code> resource.

```sql
/*+ update */
UPDATE azure.aad_domain_services.ou_containers
SET 
accountName = '{{ accountName }}',
spn = '{{ spn }}',
password = '{{ password }}'
WHERE 
domainServiceName = '{{ domainServiceName }}'
AND ouContainerName = '{{ ouContainerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>ou_containers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.aad_domain_services.ou_containers
WHERE domainServiceName = '{{ domainServiceName }}'
AND ouContainerName = '{{ ouContainerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
