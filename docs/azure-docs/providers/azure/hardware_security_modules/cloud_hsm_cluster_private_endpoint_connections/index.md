---
title: cloud_hsm_cluster_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_hsm_cluster_private_endpoint_connections
  - hardware_security_modules
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

Creates, updates, deletes, gets or lists a <code>cloud_hsm_cluster_private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_hsm_cluster_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hardware_security_modules.cloud_hsm_cluster_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_hsm_cluster_private_endpoint_connections', value: 'view', },
        { label: 'cloud_hsm_cluster_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="cloudHsmClusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="peConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the private endpoint connection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudHsmClusterName, peConnectionName, resourceGroupName, subscriptionId" /> | Gets the private endpoint connection for the Cloud Hsm Cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="cloudHsmClusterName, peConnectionName, resourceGroupName, subscriptionId" /> | Creates or updates the private endpoint connection for the Cloud Hsm Cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudHsmClusterName, peConnectionName, resourceGroupName, subscriptionId" /> | Deletes the private endpoint connection for the Cloud Hsm Cluster. |

## `SELECT` examples

Gets the private endpoint connection for the Cloud Hsm Cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_hsm_cluster_private_endpoint_connections', value: 'view', },
        { label: 'cloud_hsm_cluster_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cloudHsmClusterName,
group_ids,
peConnectionName,
private_endpoint,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.hardware_security_modules.vw_cloud_hsm_cluster_private_endpoint_connections
WHERE cloudHsmClusterName = '{{ cloudHsmClusterName }}'
AND peConnectionName = '{{ peConnectionName }}'
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
FROM azure.hardware_security_modules.cloud_hsm_cluster_private_endpoint_connections
WHERE cloudHsmClusterName = '{{ cloudHsmClusterName }}'
AND peConnectionName = '{{ peConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_hsm_cluster_private_endpoint_connections</code> resource.

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
INSERT INTO azure.hardware_security_modules.cloud_hsm_cluster_private_endpoint_connections (
cloudHsmClusterName,
peConnectionName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ cloudHsmClusterName }}',
'{{ peConnectionName }}',
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
    - name: properties
      value:
        - name: groupIds
          value:
            - string
        - name: privateEndpoint
          value:
            - name: id
              value: string
        - name: privateLinkServiceConnectionState
          value:
            - name: status
              value: []
            - name: description
              value: string
            - name: actionsRequired
              value: string
        - name: provisioningState
          value: []
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>cloud_hsm_cluster_private_endpoint_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hardware_security_modules.cloud_hsm_cluster_private_endpoint_connections
WHERE cloudHsmClusterName = '{{ cloudHsmClusterName }}'
AND peConnectionName = '{{ peConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
