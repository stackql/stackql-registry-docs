---
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
  - connected_vsphere
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.connected_vsphere.virtual_machine_templates" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name. |
| <CopyableCode code="custom_resource_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="firmware_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="folder_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="inventory_item_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="location" /> | `text` | Gets or sets the location. |
| <CopyableCode code="memory_size_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="mo_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="mo_ref_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_interfaces" /> | `text` | field from the `properties` object |
| <CopyableCode code="num_cores_per_socket" /> | `text` | field from the `properties` object |
| <CopyableCode code="num_cp_us" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="statuses" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets the Resource tags. |
| <CopyableCode code="tools_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="tools_version_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets or sets the type of the resource. |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_center_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualMachineTemplateName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="location" /> | `string` | Gets or sets the location. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine Template. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets the Resource tags. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineTemplateName" /> | Implements virtual machine template GET method. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List of virtualMachineTemplates in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List of virtualMachineTemplates in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineTemplateName, data__location, data__properties" /> | Create Or Update virtual machine template. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineTemplateName" /> | Implements virtual machine template DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineTemplateName" /> | API to update certain properties of the virtual machine template resource. |

## `SELECT` examples

List of virtualMachineTemplates in a subscription.

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
custom_resource_name,
disks,
extended_location,
firmware_type,
folder_path,
inventory_item_id,
kind,
location,
memory_size_mb,
mo_name,
mo_ref_id,
network_interfaces,
num_cores_per_socket,
num_cp_us,
os_name,
os_type,
provisioning_state,
resourceGroupName,
statuses,
subscriptionId,
system_data,
tags,
tools_version,
tools_version_status,
type,
uuid,
v_center_id,
virtualMachineTemplateName
FROM azure_isv.connected_vsphere.vw_virtual_machine_templates
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
extendedLocation,
kind,
location,
properties,
systemData,
tags,
type
FROM azure_isv.connected_vsphere.virtual_machine_templates
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machine_templates</code> resource.

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
INSERT INTO azure_isv.connected_vsphere.virtual_machine_templates (
resourceGroupName,
subscriptionId,
virtualMachineTemplateName,
data__location,
data__properties,
properties,
location,
extendedLocation,
systemData,
tags,
kind
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualMachineTemplateName }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ extendedLocation }}',
'{{ systemData }}',
'{{ tags }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: uuid
          value: string
        - name: vCenterId
          value: string
        - name: moRefId
          value: string
        - name: inventoryItemId
          value: string
        - name: moName
          value: string
        - name: memorySizeMB
          value: integer
        - name: numCPUs
          value: integer
        - name: numCoresPerSocket
          value: integer
        - name: osType
          value: []
        - name: osName
          value: string
        - name: folderPath
          value: string
        - name: networkInterfaces
          value:
            - - name: name
                value: string
              - name: label
                value: string
              - name: ipAddresses
                value:
                  - string
              - name: macAddress
                value: string
              - name: networkId
                value: string
              - name: nicType
                value: []
              - name: powerOnBoot
                value: []
              - name: networkMoRefId
                value: string
              - name: networkMoName
                value: string
              - name: deviceKey
                value: integer
              - name: ipSettings
                value:
                  - name: allocationMethod
                    value: []
                  - name: dnsServers
                    value:
                      - string
                  - name: gateway
                    value:
                      - string
                  - name: ipAddress
                    value: string
                  - name: subnetMask
                    value: string
                  - name: primaryWinsServer
                    value: string
                  - name: secondaryWinsServer
                    value: string
                  - name: ipAddressInfo
                    value:
                      - - name: allocationMethod
                          value: string
                        - name: ipAddress
                          value: string
                        - name: subnetMask
                          value: string
        - name: disks
          value:
            - - name: name
                value: string
              - name: label
                value: string
              - name: diskObjectId
                value: string
              - name: diskSizeGB
                value: integer
              - name: deviceKey
                value: integer
              - name: diskMode
                value: []
              - name: controllerKey
                value: integer
              - name: unitNumber
                value: integer
              - name: deviceName
                value: string
              - name: diskType
                value: []
        - name: customResourceName
          value: string
        - name: toolsVersionStatus
          value: string
        - name: toolsVersion
          value: string
        - name: firmwareType
          value: []
        - name: statuses
          value:
            - - name: type
                value: string
              - name: status
                value: string
              - name: reason
                value: string
              - name: message
                value: string
              - name: severity
                value: string
              - name: lastUpdatedAt
                value: string
        - name: provisioningState
          value: []
    - name: location
      value: string
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
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
    - name: tags
      value: object
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machine_templates</code> resource.

```sql
/*+ update */
UPDATE azure_isv.connected_vsphere.virtual_machine_templates
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineTemplateName = '{{ virtualMachineTemplateName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_templates</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.connected_vsphere.virtual_machine_templates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineTemplateName = '{{ virtualMachineTemplateName }}';
```
