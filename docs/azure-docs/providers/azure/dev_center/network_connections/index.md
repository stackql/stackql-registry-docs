---
title: network_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - network_connections
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

Creates, updates, deletes, gets or lists a <code>network_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.network_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_connections', value: 'view', },
        { label: 'network_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="domain_join_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_username" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_check_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="networkConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="networking_resource_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="organization_unit" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkConnectionName, resourceGroupName, subscriptionId" /> | Gets a network connection resource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists network connections in a resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists network connections in a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkConnectionName, resourceGroupName, subscriptionId" /> | Creates or updates a Network Connections resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkConnectionName, resourceGroupName, subscriptionId" /> | Deletes a Network Connections resource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkConnectionName, resourceGroupName, subscriptionId" /> | Partially updates a Network Connection |
| <CopyableCode code="run_health_checks" /> | `EXEC` | <CopyableCode code="networkConnectionName, resourceGroupName, subscriptionId" /> | Triggers a new health check run. The execution and health check result can be tracked via the network Connection health check details |

## `SELECT` examples

Lists network connections in a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_connections', value: 'view', },
        { label: 'network_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
domain_join_type,
domain_name,
domain_password,
domain_username,
health_check_status,
location,
networkConnectionName,
networking_resource_group_name,
organization_unit,
provisioning_state,
resourceGroupName,
subnet_id,
subscriptionId,
tags
FROM azure.dev_center.vw_network_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.dev_center.network_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_connections</code> resource.

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
INSERT INTO azure.dev_center.network_connections (
networkConnectionName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ networkConnectionName }}',
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
        - name: subnetId
          value: string
        - name: domainName
          value: string
        - name: organizationUnit
          value: string
        - name: domainUsername
          value: string
        - name: domainPassword
          value: string
        - name: provisioningState
          value: []
        - name: healthCheckStatus
          value: []
        - name: networkingResourceGroupName
          value: string
        - name: domainJoinType
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_connections</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.network_connections
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
networkConnectionName = '{{ networkConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.network_connections
WHERE networkConnectionName = '{{ networkConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
