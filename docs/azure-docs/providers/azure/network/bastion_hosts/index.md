---
title: bastion_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - bastion_hosts
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

Creates, updates, deletes, gets or lists a <code>bastion_hosts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bastion_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.bastion_hosts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bastion_hosts', value: 'view', },
        { label: 'bastion_hosts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="bastionHostName" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_copy_paste" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_file_copy" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_ip_connect" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_kerberos" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_session_recording" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_shareable_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_tunneling" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="network_acls" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_units" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The sku of this Bastion Host. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | A list of availability zones denoting where the resource needs to come from. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the Bastion Host. |
| <CopyableCode code="sku" /> | `object` | The sku of this Bastion Host. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting where the resource needs to come from. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Gets the specified Bastion Host. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all Bastion Hosts in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Bastion Hosts in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Creates or updates the specified Bastion Host. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Deletes the specified Bastion Host. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Updates Tags for BastionHost resource |

## `SELECT` examples

Lists all Bastion Hosts in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bastion_hosts', value: 'view', },
        { label: 'bastion_hosts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
bastionHostName,
disable_copy_paste,
dns_name,
enable_file_copy,
enable_ip_connect,
enable_kerberos,
enable_session_recording,
enable_shareable_link,
enable_tunneling,
etag,
ip_configurations,
location,
network_acls,
provisioning_state,
resourceGroupName,
scale_units,
sku,
subscriptionId,
tags,
type,
virtual_network,
zones
FROM azure.network.vw_bastion_hosts
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
sku,
tags,
type,
zones
FROM azure.network.bastion_hosts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bastion_hosts</code> resource.

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
INSERT INTO azure.network.bastion_hosts (
bastionHostName,
resourceGroupName,
subscriptionId,
properties,
zones,
sku,
id,
location,
tags
)
SELECT 
'{{ bastionHostName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ zones }}',
'{{ sku }}',
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
        - name: ipConfigurations
          value:
            - - name: properties
                value:
                  - name: subnet
                    value:
                      - name: id
                        value: string
                  - name: provisioningState
                    value: []
                  - name: privateIPAllocationMethod
                    value: []
              - name: name
                value: string
              - name: etag
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: dnsName
          value: string
        - name: networkAcls
          value: string
        - name: scaleUnits
          value: integer
        - name: disableCopyPaste
          value: boolean
        - name: enableFileCopy
          value: boolean
        - name: enableIpConnect
          value: boolean
        - name: enableShareableLink
          value: boolean
        - name: enableTunneling
          value: boolean
        - name: enableKerberos
          value: boolean
        - name: enableSessionRecording
          value: boolean
    - name: zones
      value:
        - string
    - name: etag
      value: string
    - name: sku
      value:
        - name: name
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

## `DELETE` example

Deletes the specified <code>bastion_hosts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.bastion_hosts
WHERE bastionHostName = '{{ bastionHostName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
