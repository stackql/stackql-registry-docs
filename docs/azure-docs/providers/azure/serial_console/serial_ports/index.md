---
title: serial_ports
hide_title: false
hide_table_of_contents: false
keywords:
  - serial_ports
  - serial_console
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

Creates, updates, deletes, gets or lists a <code>serial_ports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serial_ports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.serial_console.serial_ports" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_serial_ports', value: 'view', },
        { label: 'serial_ports', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="parentResource" /> | `text` | field from the `properties` object |
| <CopyableCode code="parentResourceType" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceProviderNamespace" /> | `text` | field from the `properties` object |
| <CopyableCode code="serialPort" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the serial port. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, serialPort, subscriptionId" /> | Gets the configured settings for a serial port |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, subscriptionId" /> | Lists all of the configured serial ports for a parent resource  |
| <CopyableCode code="list_by_subscriptions" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Handles requests to list all SerialPort resources in a subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, serialPort, subscriptionId" /> | Creates or updates a serial port |
| <CopyableCode code="connect" /> | `EXEC` | <CopyableCode code="parentResource, parentResourceType, resourceGroupName, resourceProviderNamespace, serialPort, subscriptionId" /> | Connect to serial port of the target resource |

## `SELECT` examples

Handles requests to list all SerialPort resources in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_serial_ports', value: 'view', },
        { label: 'serial_ports', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connection_state,
parentResource,
parentResourceType,
resourceGroupName,
resourceProviderNamespace,
serialPort,
state,
subscriptionId
FROM azure.serial_console.vw_serial_ports
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.serial_console.serial_ports
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>serial_ports</code> resource.

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
INSERT INTO azure.serial_console.serial_ports (
parentResource,
parentResourceType,
resourceGroupName,
resourceProviderNamespace,
serialPort,
subscriptionId,
properties
)
SELECT 
'{{ parentResource }}',
'{{ parentResourceType }}',
'{{ resourceGroupName }}',
'{{ resourceProviderNamespace }}',
'{{ serialPort }}',
'{{ subscriptionId }}',
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
        - name: state
          value: string
        - name: connectionState
          value: string

```
</TabItem>
</Tabs>
