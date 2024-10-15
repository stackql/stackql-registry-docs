---
title: dataflow_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - dataflow_profiles
  - iotoperations
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

Creates, updates, deletes, gets or lists a <code>dataflow_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataflow_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotoperations.dataflow_profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dataflow_profiles', value: 'view', },
        { label: 'dataflow_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dataflowProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| <CopyableCode code="properties" /> | `object` | DataflowProfile Resource properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataflowProfileName, instanceName, resourceGroupName, subscriptionId" /> | Get a DataflowProfileResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | List DataflowProfileResource resources by InstanceResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataflowProfileName, instanceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a DataflowProfileResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataflowProfileName, instanceName, resourceGroupName, subscriptionId" /> | Delete a DataflowProfileResource |

## `SELECT` examples

List DataflowProfileResource resources by InstanceResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dataflow_profiles', value: 'view', },
        { label: 'dataflow_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dataflowProfileName,
diagnostics,
extended_location,
instanceName,
instance_count,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.iotoperations.vw_dataflow_profiles
WHERE instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
properties
FROM azure.iotoperations.dataflow_profiles
WHERE instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dataflow_profiles</code> resource.

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
INSERT INTO azure.iotoperations.dataflow_profiles (
dataflowProfileName,
instanceName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation
)
SELECT 
'{{ dataflowProfileName }}',
'{{ instanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: diagnostics
          value:
            - name: logs
              value:
                - name: opentelemetryExportConfig
                  value:
                    - name: otlpGrpcEndpoint
                      value: string
                    - name: intervalSeconds
                      value: integer
                    - name: level
                      value: string
                - name: level
                  value: string
            - name: metrics
              value:
                - name: opentelemetryExportConfig
                  value:
                    - name: otlpGrpcEndpoint
                      value: string
                    - name: intervalSeconds
                      value: integer
                - name: prometheusPort
                  value: integer
        - name: instanceCount
          value: integer
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dataflow_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iotoperations.dataflow_profiles
WHERE dataflowProfileName = '{{ dataflowProfileName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
