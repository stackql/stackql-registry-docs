---
title: ip_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_groups
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

Creates, updates, deletes, gets or lists a <code>ip_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.ip_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_groups', value: 'view', },
        { label: 'ip_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="firewall_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewalls" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipGroupsName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | The IpGroups property information. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ipGroupsName, resourceGroupName, subscriptionId" /> | Gets the specified ipGroups. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all IpGroups in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all IpGroups in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="ipGroupsName, resourceGroupName, subscriptionId" /> | Creates or updates an ipGroups in a specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ipGroupsName, resourceGroupName, subscriptionId" /> | Deletes the specified ipGroups. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="ipGroupsName, resourceGroupName, subscriptionId" /> | Updates tags of an IpGroups resource. |

## `SELECT` examples

Gets all IpGroups in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_groups', value: 'view', },
        { label: 'ip_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
firewall_policies,
firewalls,
ipGroupsName,
ip_addresses,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.network.vw_ip_groups
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
tags,
type
FROM azure.network.ip_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_groups</code> resource.

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
INSERT INTO azure.network.ip_groups (
ipGroupsName,
resourceGroupName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ ipGroupsName }}',
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
        - name: provisioningState
          value: []
        - name: ipAddresses
          value:
            - string
        - name: firewalls
          value:
            - - name: id
                value: string
        - name: firewallPolicies
          value:
            - - name: id
                value: string
    - name: etag
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

Updates a <code>ip_groups</code> resource.

```sql
/*+ update */
UPDATE azure.network.ip_groups
SET 
tags = '{{ tags }}'
WHERE 
ipGroupsName = '{{ ipGroupsName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>ip_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.ip_groups
WHERE ipGroupsName = '{{ ipGroupsName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
