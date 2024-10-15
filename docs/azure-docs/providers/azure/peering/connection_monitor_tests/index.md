---
title: connection_monitor_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_monitor_tests
  - peering
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

Creates, updates, deletes, gets or lists a <code>connection_monitor_tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_monitor_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.connection_monitor_tests" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connection_monitor_tests', value: 'view', },
        { label: 'connection_monitor_tests', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="connectionMonitorTestName" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_test_successful" /> | `text` | field from the `properties` object |
| <CopyableCode code="path" /> | `text` | field from the `properties` object |
| <CopyableCode code="peeringServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_agent" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_frequency_in_sec" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define a Connection Monitor Test. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionMonitorTestName, peeringServiceName, resourceGroupName, subscriptionId" /> | Gets an existing connection monitor test with the specified name under the given subscription, resource group and peering service. |
| <CopyableCode code="list_by_peering_service" /> | `SELECT` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId" /> | Lists all connection monitor tests under the given subscription, resource group and peering service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionMonitorTestName, peeringServiceName, resourceGroupName, subscriptionId" /> | Creates or updates a connection monitor test with the specified name under the given subscription, resource group and peering service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionMonitorTestName, peeringServiceName, resourceGroupName, subscriptionId" /> | Deletes an existing connection monitor test with the specified name under the given subscription, resource group and peering service. |

## `SELECT` examples

Lists all connection monitor tests under the given subscription, resource group and peering service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connection_monitor_tests', value: 'view', },
        { label: 'connection_monitor_tests', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
connectionMonitorTestName,
destination,
destination_port,
is_test_successful,
path,
peeringServiceName,
provisioning_state,
resourceGroupName,
source_agent,
subscriptionId,
test_frequency_in_sec,
type
FROM azure.peering.vw_connection_monitor_tests
WHERE peeringServiceName = '{{ peeringServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.peering.connection_monitor_tests
WHERE peeringServiceName = '{{ peeringServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connection_monitor_tests</code> resource.

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
INSERT INTO azure.peering.connection_monitor_tests (
connectionMonitorTestName,
peeringServiceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ connectionMonitorTestName }}',
'{{ peeringServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: sourceAgent
          value: string
        - name: destination
          value: string
        - name: destinationPort
          value: integer
        - name: testFrequencyInSec
          value: integer
        - name: isTestSuccessful
          value: boolean
        - name: path
          value:
            - string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>connection_monitor_tests</code> resource.

```sql
/*+ delete */
DELETE FROM azure.peering.connection_monitor_tests
WHERE connectionMonitorTestName = '{{ connectionMonitorTestName }}'
AND peeringServiceName = '{{ peeringServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
