---
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
  - vmware_cloud_simple
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.virtual_machine_templates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_templates', value: 'view', },
        { label: 'virtual_machine_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | virtual machine template id (privateCloudId:vsphereId) |
| <CopyableCode code="name" /> | `text` | {virtualMachineTemplateName} |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="amount_of_ram" /> | `text` | field from the `properties` object |
| <CopyableCode code="controllers" /> | `text` | field from the `properties` object |
| <CopyableCode code="disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="expose_to_guest_vm" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_os" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure region |
| <CopyableCode code="nics" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_cores" /> | `text` | field from the `properties` object |
| <CopyableCode code="path" /> | `text` | field from the `properties` object |
| <CopyableCode code="pcName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_cloud_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="regionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourcePoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | {resourceProviderNamespace}/{resourceType} |
| <CopyableCode code="v_sphere_networks" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_sphere_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualMachineTemplateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmwaretools" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | virtual machine template id (privateCloudId:vsphereId) |
| <CopyableCode code="name" /> | `string` | {virtualMachineTemplateName} |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | Properties of virtual machine template |
| <CopyableCode code="type" /> | `string` | {resourceProviderNamespace}/{resourceType} |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pcName, regionId, subscriptionId, virtualMachineTemplateName" /> | Returns virtual machine templates by its name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="pcName, regionId, resourcePoolName, subscriptionId" /> | Returns list of virtual machine templates in region for private cloud |

## `SELECT` examples

Returns list of virtual machine templates in region for private cloud

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_templates', value: 'view', },
        { label: 'virtual_machine_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
amount_of_ram,
controllers,
disks,
expose_to_guest_vm,
guest_os,
guest_os_type,
location,
nics,
number_of_cores,
path,
pcName,
private_cloud_id,
regionId,
resourcePoolName,
subscriptionId,
type,
v_sphere_networks,
v_sphere_tags,
virtualMachineTemplateName,
vmwaretools
FROM azure_isv.vmware_cloud_simple.vw_virtual_machine_templates
WHERE pcName = '{{ pcName }}'
AND regionId = '{{ regionId }}'
AND resourcePoolName = '{{ resourcePoolName }}'
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
type
FROM azure_isv.vmware_cloud_simple.virtual_machine_templates
WHERE pcName = '{{ pcName }}'
AND regionId = '{{ regionId }}'
AND resourcePoolName = '{{ resourcePoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

