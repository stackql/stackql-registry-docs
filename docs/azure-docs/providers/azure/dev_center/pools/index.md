---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pools', value: 'view', },
        { label: 'pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dev_box_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="dev_box_definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="dev_box_definition_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="dev_box_definition_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_administrator" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_virtual_network_regions" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_connection_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="single_sign_on_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="stop_on_disconnect" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="virtual_network_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a Pool |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="poolName, projectName, resourceGroupName, subscriptionId" /> | Gets a machine pool |
| <CopyableCode code="list_by_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Lists pools for a project |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="poolName, projectName, resourceGroupName, subscriptionId" /> | Creates or updates a machine pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="poolName, projectName, resourceGroupName, subscriptionId" /> | Deletes a machine pool |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="poolName, projectName, resourceGroupName, subscriptionId" /> | Partially updates a machine pool |
| <CopyableCode code="run_health_checks" /> | `EXEC` | <CopyableCode code="poolName, projectName, resourceGroupName, subscriptionId" /> | Triggers a refresh of the pool status. |

## `SELECT` examples

Lists pools for a project

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pools', value: 'view', },
        { label: 'pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dev_box_count,
dev_box_definition,
dev_box_definition_name,
dev_box_definition_type,
display_name,
health_status,
health_status_details,
license_type,
local_administrator,
location,
managed_virtual_network_regions,
network_connection_name,
poolName,
projectName,
provisioning_state,
resourceGroupName,
single_sign_on_status,
stop_on_disconnect,
subscriptionId,
tags,
virtual_network_type
FROM azure.dev_center.vw_pools
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.dev_center.pools
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pools</code> resource.

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
INSERT INTO azure.dev_center.pools (
poolName,
projectName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ poolName }}',
'{{ projectName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: devBoxDefinitionType
          value: []
        - name: devBoxDefinitionName
          value: string
        - name: devBoxDefinition
          value:
            - name: imageReference
              value:
                - name: id
                  value: string
                - name: exactVersion
                  value: string
            - name: sku
              value:
                - name: name
                  value: string
                - name: tier
                  value: []
                - name: size
                  value: string
                - name: family
                  value: string
                - name: capacity
                  value: integer
        - name: networkConnectionName
          value: string
        - name: licenseType
          value: []
        - name: localAdministrator
          value: []
        - name: stopOnDisconnect
          value:
            - name: status
              value: []
            - name: gracePeriodMinutes
              value: integer
        - name: singleSignOnStatus
          value: []
        - name: displayName
          value: string
        - name: virtualNetworkType
          value: []
        - name: managedVirtualNetworkRegions
          value:
            - string
        - name: healthStatus
          value: []
        - name: healthStatusDetails
          value:
            - - name: code
                value: string
              - name: message
                value: string
        - name: devBoxCount
          value: integer
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pools</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
poolName = '{{ poolName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.pools
WHERE poolName = '{{ poolName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
