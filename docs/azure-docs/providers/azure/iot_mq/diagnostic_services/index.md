---
title: diagnostic_services
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_services
  - iot_mq
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

Creates, updates, deletes, gets or lists a <code>diagnostic_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>diagnostic_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.diagnostic_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostic_services', value: 'view', },
        { label: 'diagnostic_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data_export_frequency_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnosticServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="image" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="log_format" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_data_storage_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="metrics_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="mqName" /> | `text` | field from the `properties` object |
| <CopyableCode code="open_telemetry_traces_collector_addr" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="stale_data_timeout_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | MQ Diagnostic Services Resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diagnosticServiceName, mqName, resourceGroupName, subscriptionId" /> | Get a DiagnosticServiceResource |
| <CopyableCode code="list_by_mq_resource" /> | `SELECT` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List DiagnosticServiceResource resources by MqResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diagnosticServiceName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a DiagnosticServiceResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diagnosticServiceName, mqName, resourceGroupName, subscriptionId" /> | Delete a DiagnosticServiceResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="diagnosticServiceName, mqName, resourceGroupName, subscriptionId" /> | Update a DiagnosticServiceResource |

## `SELECT` examples

List DiagnosticServiceResource resources by MqResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostic_services', value: 'view', },
        { label: 'diagnostic_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
data_export_frequency_seconds,
diagnosticServiceName,
extended_location,
image,
location,
log_format,
log_level,
max_data_storage_size,
metrics_port,
mqName,
open_telemetry_traces_collector_addr,
provisioning_state,
resourceGroupName,
stale_data_timeout_seconds,
subscriptionId,
tags
FROM azure.iot_mq.vw_diagnostic_services
WHERE mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.iot_mq.diagnostic_services
WHERE mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>diagnostic_services</code> resource.

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
INSERT INTO azure.iot_mq.diagnostic_services (
diagnosticServiceName,
mqName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ diagnosticServiceName }}',
'{{ mqName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: dataExportFrequencySeconds
          value: integer
        - name: image
          value:
            - name: pullPolicy
              value: string
            - name: pullSecrets
              value: string
            - name: repository
              value: string
            - name: tag
              value: string
        - name: logFormat
          value: string
        - name: logLevel
          value: string
        - name: maxDataStorageSize
          value: integer
        - name: metricsPort
          value: integer
        - name: openTelemetryTracesCollectorAddr
          value: string
        - name: provisioningState
          value: []
        - name: staleDataTimeoutSeconds
          value: integer
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>diagnostic_services</code> resource.

```sql
/*+ update */
UPDATE azure.iot_mq.diagnostic_services
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
diagnosticServiceName = '{{ diagnosticServiceName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>diagnostic_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_mq.diagnostic_services
WHERE diagnosticServiceName = '{{ diagnosticServiceName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
