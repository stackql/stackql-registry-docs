---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
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

Creates, updates, deletes, gets or lists a <code>virtual_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.virtual_machines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machines', value: 'view', },
        { label: 'virtual_machines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/virtualMachines/{virtualMachineName} |
| <CopyableCode code="name" /> | `text` | {virtualMachineName} |
| <CopyableCode code="amount_of_ram" /> | `text` | field from the `properties` object |
| <CopyableCode code="controllers" /> | `text` | field from the `properties` object |
| <CopyableCode code="customization" /> | `text` | field from the `properties` object |
| <CopyableCode code="disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="dnsname" /> | `text` | field from the `properties` object |
| <CopyableCode code="expose_to_guest_vm" /> | `text` | field from the `properties` object |
| <CopyableCode code="folder" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_os" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure region |
| <CopyableCode code="nics" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_cores" /> | `text` | field from the `properties` object |
| <CopyableCode code="password" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_cloud_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_pool" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags model |
| <CopyableCode code="template_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | {resourceProviderNamespace}/{resourceType} |
| <CopyableCode code="username" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_sphere_networks" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualMachineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmwaretools" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/virtualMachines/{virtualMachineName} |
| <CopyableCode code="name" /> | `string` | {virtualMachineName} |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | Properties of virtual machine |
| <CopyableCode code="tags" /> | `object` | Tags model |
| <CopyableCode code="type" /> | `string` | {resourceProviderNamespace}/{resourceType} |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Get virtual machine |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns list of virtual machine within resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns list virtual machine within subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="Referer, resourceGroupName, subscriptionId, virtualMachineName, data__location" /> | Create Or Update Virtual Machine |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="Referer, resourceGroupName, subscriptionId, virtualMachineName" /> | Delete virtual machine |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Patch virtual machine properties |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="Referer, resourceGroupName, subscriptionId, virtualMachineName" /> | Power on virtual machine |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="Referer, resourceGroupName, subscriptionId, virtualMachineName" /> | Power off virtual machine, options: shutdown, poweroff, and suspend |

## `SELECT` examples

Returns list virtual machine within subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machines', value: 'view', },
        { label: 'virtual_machines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
amount_of_ram,
controllers,
customization,
disks,
dnsname,
expose_to_guest_vm,
folder,
guest_os,
guest_os_type,
location,
nics,
number_of_cores,
password,
private_cloud_id,
provisioning_state,
public_ip,
resourceGroupName,
resource_pool,
status,
subscriptionId,
tags,
template_id,
type,
username,
v_sphere_networks,
virtualMachineName,
vm_id,
vmwaretools
FROM azure_isv.vmware_cloud_simple.vw_virtual_machines
WHERE subscriptionId = '{{ subscriptionId }}';
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
FROM azure_isv.vmware_cloud_simple.virtual_machines
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machines</code> resource.

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
INSERT INTO azure_isv.vmware_cloud_simple.virtual_machines (
Referer,
resourceGroupName,
subscriptionId,
virtualMachineName,
data__location,
location,
properties,
tags
)
SELECT 
'{{ Referer }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualMachineName }}',
'{{ data__location }}',
'{{ location }}',
'{{ properties }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: location
      value: string
    - name: name
      value: string
    - name: properties
      value:
        - name: amountOfRam
          value: integer
        - name: controllers
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: subType
                value: string
              - name: type
                value: string
        - name: customization
          value:
            - name: dnsServers
              value:
                - []
            - name: hostName
              value: string
            - name: password
              value: string
            - name: policyId
              value: string
            - name: username
              value: string
        - name: disks
          value:
            - - name: controllerId
                value: string
              - name: independenceMode
                value: string
              - name: totalSize
                value: integer
              - name: virtualDiskId
                value: string
              - name: virtualDiskName
                value: string
        - name: dnsname
          value: string
        - name: exposeToGuestVM
          value: boolean
        - name: folder
          value: string
        - name: guestOS
          value: string
        - name: guestOSType
          value: string
        - name: nics
          value:
            - - name: customization
                value:
                  - name: allocation
                    value: string
                  - name: dnsServers
                    value:
                      - []
                  - name: gateway
                    value:
                      - []
                  - name: ipAddress
                    value: []
              - name: ipAddresses
                value:
                  - string
              - name: macAddress
                value: string
              - name: network
                value:
                  - name: assignable
                    value: boolean
                  - name: id
                    value: string
                  - name: location
                    value: string
                  - name: name
                    value: string
                  - name: properties
                    value:
                      - name: privateCloudId
                        value: string
                  - name: type
                    value: string
              - name: nicType
                value: string
              - name: powerOnBoot
                value: boolean
              - name: virtualNicId
                value: string
              - name: virtualNicName
                value: string
        - name: numberOfCores
          value: integer
        - name: password
          value: string
        - name: privateCloudId
          value: string
        - name: provisioningState
          value: string
        - name: publicIP
          value: string
        - name: resourcePool
          value:
            - name: id
              value: string
            - name: location
              value: string
            - name: name
              value: string
            - name: privateCloudId
              value: string
            - name: properties
              value:
                - name: fullName
                  value: string
            - name: type
              value: string
        - name: status
          value: string
        - name: templateId
          value: string
        - name: username
          value: string
        - name: vSphereNetworks
          value:
            - string
        - name: vmId
          value: string
        - name: vmwaretools
          value: string
    - name: tags
      value: []
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machines</code> resource.

```sql
/*+ update */
UPDATE azure_isv.vmware_cloud_simple.virtual_machines
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machines</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.vmware_cloud_simple.virtual_machines
WHERE Referer = '{{ Referer }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```
