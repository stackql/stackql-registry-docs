---
title: managers
hide_title: false
hide_table_of_contents: false
keywords:
  - managers
  - network
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

Creates, updates, deletes, gets or lists a <code>managers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.managers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managers', value: 'view', },
        { label: 'managers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="networkManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_manager_scope_accesses" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_manager_scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of Managed Network |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Gets the specified Network Manager. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List network managers in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all network managers in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Creates or updates a Network Manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Deletes a network manager. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Patch NetworkManager. |

## `SELECT` examples

List all network managers in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managers', value: 'view', },
        { label: 'managers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
etag,
location,
networkManagerName,
network_manager_scope_accesses,
network_manager_scopes,
provisioning_state,
resourceGroupName,
resource_guid,
subscriptionId,
system_data,
tags,
type
FROM azure.network.vw_managers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
systemData,
tags,
type
FROM azure.network.managers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managers</code> resource.

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
INSERT INTO azure.network.managers (
networkManagerName,
resourceGroupName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ networkManagerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ id }}',
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
        - name: description
          value: string
        - name: networkManagerScopes
          value:
            - name: managementGroups
              value:
                - string
            - name: subscriptions
              value:
                - string
            - name: crossTenantScopes
              value:
                - - name: tenantId
                    value: string
                  - name: managementGroups
                    value:
                      - string
                  - name: subscriptions
                    value:
                      - string
        - name: networkManagerScopeAccesses
          value:
            - []
        - name: provisioningState
          value: []
        - name: resourceGuid
          value: string
    - name: etag
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

Updates a <code>managers</code> resource.

```sql
/*+ update */
UPDATE azure.network.managers
SET 
tags = '{{ tags }}'
WHERE 
networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.managers
WHERE networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
