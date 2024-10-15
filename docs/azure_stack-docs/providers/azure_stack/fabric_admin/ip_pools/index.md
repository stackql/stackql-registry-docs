---
title: ip_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_pools
  - fabric_admin
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

Creates, updates, deletes, gets or lists a <code>ip_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.ip_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_pools', value: 'view', },
        { label: 'ip_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipPool" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The region where the resource is located. |
| <CopyableCode code="number_of_allocated_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_ip_addresses_in_transition" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | Properties of an IpPool. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ipPool, location, resourceGroupName, subscriptionId" /> | Return the requested IP pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all IP pools at a certain location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="ipPool, location, resourceGroupName, subscriptionId" /> | Create an IP pool.  Once created an IP pool cannot be deleted. |

## `SELECT` examples

Returns a list of all IP pools at a certain location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_pools', value: 'view', },
        { label: 'ip_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
address_prefix,
end_ip_address,
ipPool,
location,
number_of_allocated_ip_addresses,
number_of_ip_addresses,
number_of_ip_addresses_in_transition,
resourceGroupName,
start_ip_address,
subscriptionId,
tags,
type
FROM azure_stack.fabric_admin.vw_ip_pools
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_stack.fabric_admin.ip_pools
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_pools</code> resource.

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
INSERT INTO azure_stack.fabric_admin.ip_pools (
ipPool,
location,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ ipPool }}',
'{{ location }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: startIpAddress
          value: string
        - name: endIpAddress
          value: string
        - name: addressPrefix
          value: string
        - name: numberOfIpAddresses
          value: integer
        - name: numberOfAllocatedIpAddresses
          value: integer
        - name: numberOfIpAddressesInTransition
          value: integer
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
