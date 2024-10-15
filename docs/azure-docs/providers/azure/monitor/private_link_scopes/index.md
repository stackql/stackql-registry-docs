---
title: private_link_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_scopes
  - monitor
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

Creates, updates, deletes, gets or lists a <code>private_link_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.private_link_scopes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_scopes', value: 'view', },
        { label: 'private_link_scopes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="access_mode_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties that define a Azure Monitor PrivateLinkScope resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId" /> | Returns a Azure Monitor PrivateLinkScope. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all Azure Monitor PrivateLinkScopes within a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Azure Monitor PrivateLinkScopes within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId, data__properties" /> | Creates (or updates) a Azure Monitor PrivateLinkScope. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId" /> | Deletes a Azure Monitor PrivateLinkScope. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId" /> | Updates an existing PrivateLinkScope's tags. To update other fields use the CreateOrUpdate method. |

## `SELECT` examples

Gets a list of all Azure Monitor PrivateLinkScopes within a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_scopes', value: 'view', },
        { label: 'private_link_scopes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
access_mode_settings,
location,
private_endpoint_connections,
provisioning_state,
resourceGroupName,
scopeName,
subscriptionId,
system_data,
tags
FROM azure.monitor.vw_private_link_scopes
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.monitor.private_link_scopes
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_link_scopes</code> resource.

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
INSERT INTO azure.monitor.private_link_scopes (
resourceGroupName,
scopeName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ scopeName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
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
          value: string
        - name: privateEndpointConnections
          value:
            - - name: properties
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
              - name: location
                value: string
              - name: tags
                value: object
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
        - name: accessModeSettings
          value:
            - name: queryAccessMode
              value: []
            - name: exclusions
              value:
                - - name: privateEndpointConnectionName
                    value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_link_scopes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.private_link_scopes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND scopeName = '{{ scopeName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
