---
title: edge_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_devices
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>edge_devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>edge_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.edge_devices" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_edge_devices', value: 'view', },
        { label: 'edge_devices', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="device_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="edgeDeviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Edge Device properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="edgeDeviceName, resourceUri" /> | Get a EdgeDevice |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List EdgeDevice resources by parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="edgeDeviceName, resourceUri" /> | Create a EdgeDevice |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="edgeDeviceName, resourceUri" /> | Delete a EdgeDevice |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="edgeDeviceName, resourceUri, data__edgeDeviceIds" /> | A long-running resource action. |

## `SELECT` examples

List EdgeDevice resources by parent

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_edge_devices', value: 'view', },
        { label: 'edge_devices', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
device_configuration,
edgeDeviceName,
provisioning_state,
resourceUri
FROM azure_stack.azure_stack_hci.vw_edge_devices
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_stack.azure_stack_hci.edge_devices
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>edge_devices</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.edge_devices (
edgeDeviceName,
resourceUri,
properties
)
SELECT 
'{{ edgeDeviceName }}',
'{{ resourceUri }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: deviceConfiguration
          value:
            - name: nicDetails
              value:
                - - name: adapterName
                    value: string
                  - name: interfaceDescription
                    value: string
                  - name: componentId
                    value: string
                  - name: driverVersion
                    value: string
                  - name: ip4Address
                    value: string
                  - name: subnetMask
                    value: string
                  - name: defaultGateway
                    value: string
                  - name: dnsServers
                    value:
                      - string
                  - name: defaultIsolationId
                    value: string
            - name: deviceMetadata
              value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>edge_devices</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.edge_devices
WHERE edgeDeviceName = '{{ edgeDeviceName }}'
AND resourceUri = '{{ resourceUri }}';
```
