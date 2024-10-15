---
title: virtual_appliance_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_appliance_sites
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

Creates, updates, deletes, gets or lists a <code>virtual_appliance_sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_appliance_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_appliance_sites" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_appliance_sites', value: 'view', },
        { label: 'virtual_appliance_sites', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Name of the virtual appliance site. |
| <CopyableCode code="address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="networkVirtualApplianceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="o365_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Site type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the virtual appliance site. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the rule group. |
| <CopyableCode code="type" /> | `string` | Site type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, siteName, subscriptionId" /> | Gets the specified Virtual Appliance Site. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Lists all Network Virtual Appliance Sites in a Network Virtual Appliance resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, siteName, subscriptionId" /> | Creates or updates the specified Network Virtual Appliance Site. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, siteName, subscriptionId" /> | Deletes the specified site from a Virtual Appliance. |

## `SELECT` examples

Lists all Network Virtual Appliance Sites in a Network Virtual Appliance resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_appliance_sites', value: 'view', },
        { label: 'virtual_appliance_sites', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
address_prefix,
etag,
networkVirtualApplianceName,
o365_policy,
provisioning_state,
resourceGroupName,
siteName,
subscriptionId,
type
FROM azure.network.vw_virtual_appliance_sites
WHERE networkVirtualApplianceName = '{{ networkVirtualApplianceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.network.virtual_appliance_sites
WHERE networkVirtualApplianceName = '{{ networkVirtualApplianceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_appliance_sites</code> resource.

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
INSERT INTO azure.network.virtual_appliance_sites (
networkVirtualApplianceName,
resourceGroupName,
siteName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ networkVirtualApplianceName }}',
'{{ resourceGroupName }}',
'{{ siteName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: addressPrefix
          value: string
        - name: o365Policy
          value:
            - name: breakOutCategories
              value:
                - name: allow
                  value: boolean
                - name: optimize
                  value: boolean
                - name: default
                  value: boolean
        - name: provisioningState
          value: []
    - name: name
      value: string
    - name: etag
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_appliance_sites</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_appliance_sites
WHERE networkVirtualApplianceName = '{{ networkVirtualApplianceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
