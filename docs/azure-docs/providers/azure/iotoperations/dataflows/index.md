---
title: dataflows
hide_title: false
hide_table_of_contents: false
keywords:
  - dataflows
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

Creates, updates, deletes, gets or lists a <code>dataflows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotoperations.dataflows" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dataflows', value: 'view', },
        { label: 'dataflows', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dataflowName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataflowProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="operations" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| <CopyableCode code="properties" /> | `object` | Dataflow Resource properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataflowName, dataflowProfileName, instanceName, resourceGroupName, subscriptionId" /> | Get a DataflowResource |
| <CopyableCode code="list_by_profile_resource" /> | `SELECT` | <CopyableCode code="dataflowProfileName, instanceName, resourceGroupName, subscriptionId" /> | List DataflowResource resources by DataflowProfileResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataflowName, dataflowProfileName, instanceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a DataflowResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataflowName, dataflowProfileName, instanceName, resourceGroupName, subscriptionId" /> | Delete a DataflowResource |

## `SELECT` examples

List DataflowResource resources by DataflowProfileResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dataflows', value: 'view', },
        { label: 'dataflows', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dataflowName,
dataflowProfileName,
extended_location,
instanceName,
mode,
operations,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.iotoperations.vw_dataflows
WHERE dataflowProfileName = '{{ dataflowProfileName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
properties
FROM azure.iotoperations.dataflows
WHERE dataflowProfileName = '{{ dataflowProfileName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dataflows</code> resource.

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
INSERT INTO azure.iotoperations.dataflows (
dataflowName,
dataflowProfileName,
instanceName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation
)
SELECT 
'{{ dataflowName }}',
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
        - name: mode
          value: string
        - name: operations
          value:
            - - name: operationType
                value: []
              - name: name
                value: string
              - name: sourceSettings
                value:
                  - name: endpointRef
                    value: string
                  - name: assetRef
                    value: string
                  - name: serializationFormat
                    value: string
                  - name: schemaRef
                    value: string
                  - name: dataSources
                    value:
                      - string
              - name: builtInTransformationSettings
                value:
                  - name: serializationFormat
                    value: string
                  - name: schemaRef
                    value: string
                  - name: datasets
                    value:
                      - - name: key
                          value: string
                        - name: description
                          value: string
                        - name: schemaRef
                          value: string
                        - name: inputs
                          value:
                            - string
                        - name: expression
                          value: string
                  - name: filter
                    value:
                      - - name: type
                          value: string
                        - name: description
                          value: string
                        - name: inputs
                          value:
                            - string
                        - name: expression
                          value: string
                  - name: map
                    value:
                      - - name: type
                          value: []
                        - name: description
                          value: string
                        - name: inputs
                          value:
                            - string
                        - name: expression
                          value: string
                        - name: output
                          value: string
              - name: destinationSettings
                value:
                  - name: endpointRef
                    value: string
                  - name: dataDestination
                    value: string
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

Deletes the specified <code>dataflows</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iotoperations.dataflows
WHERE dataflowName = '{{ dataflowName }}'
AND dataflowProfileName = '{{ dataflowProfileName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
