---
title: private_endpoint_connection_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection_controllers
  - migrate
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

Creates, updates, deletes, gets or lists a <code>private_endpoint_connection_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_endpoint_connection_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.private_endpoint_connection_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_endpoint_connection_controllers', value: 'view', },
        { label: 'private_endpoint_connection_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="group_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="peConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | PrivateEndpointConnectionProperties V2 |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peConnectionName, resourceGroupName, siteName, subscriptionId" /> | Gets the private link resource. |
| <CopyableCode code="list_by_master_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Gets the private link resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="peConnectionName, resourceGroupName, siteName, subscriptionId" /> | Gets the private link resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peConnectionName, resourceGroupName, siteName, subscriptionId" /> | Deletes the private link resource. |

## `SELECT` examples

Gets the private link resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_endpoint_connection_controllers', value: 'view', },
        { label: 'private_endpoint_connection_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
group_ids,
peConnectionName,
private_endpoint,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
siteName,
subscriptionId
FROM azure.migrate.vw_private_endpoint_connection_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.private_endpoint_connection_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_endpoint_connection_controllers</code> resource.

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
INSERT INTO azure.migrate.private_endpoint_connection_controllers (
peConnectionName,
resourceGroupName,
siteName,
subscriptionId,
properties
)
SELECT 
'{{ peConnectionName }}',
'{{ resourceGroupName }}',
'{{ siteName }}',
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
        - name: provisioningState
          value: []
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_endpoint_connection_controllers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate.private_endpoint_connection_controllers
WHERE peConnectionName = '{{ peConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
