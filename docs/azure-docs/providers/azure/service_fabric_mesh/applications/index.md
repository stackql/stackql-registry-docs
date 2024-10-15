---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - service_fabric_mesh
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

Creates, updates, deletes, gets or lists a <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.applications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applications', value: 'view', },
        { label: 'applications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="debug_params" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="services" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="unhealthy_evaluation" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | This type describes properties of an application resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationResourceName, resourceGroupName, subscriptionId" /> | Gets the information about the application resource with the given name. The information include the description and other properties of the application. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the information about all application resources in a given resource group. The information include the description and other properties of the Application. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the information about all application resources in a given resource group. The information include the description and other properties of the application. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="applicationResourceName, resourceGroupName, subscriptionId, data__properties" /> | Creates an application resource with the specified name, description and properties. If an application resource with the same name exists, then it is updated with the specified description and properties. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationResourceName, resourceGroupName, subscriptionId" /> | Deletes the application resource identified by the name. |

## `SELECT` examples

Gets the information about all application resources in a given resource group. The information include the description and other properties of the application.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applications', value: 'view', },
        { label: 'applications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
applicationResourceName,
debug_params,
diagnostics,
health_state,
location,
provisioning_state,
resourceGroupName,
service_names,
services,
status,
status_details,
subscriptionId,
tags,
unhealthy_evaluation
FROM azure.service_fabric_mesh.vw_applications
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.service_fabric_mesh.applications
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>applications</code> resource.

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
INSERT INTO azure.service_fabric_mesh.applications (
applicationResourceName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ applicationResourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: description
          value: string
        - name: services
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: provisioningState
                    value: string
                  - name: osType
                    value: []
                  - name: codePackages
                    value:
                      - - name: name
                          value: string
                        - name: image
                          value: string
                        - name: imageRegistryCredential
                          value:
                            - name: server
                              value: string
                            - name: username
                              value: string
                            - name: password
                              value: string
                        - name: entrypoint
                          value: string
                        - name: commands
                          value:
                            - string
                        - name: environmentVariables
                          value:
                            - - name: name
                                value: string
                              - name: value
                                value: string
                        - name: settings
                          value:
                            - - name: name
                                value: string
                              - name: value
                                value: string
                        - name: labels
                          value:
                            - - name: name
                                value: string
                              - name: value
                                value: string
                        - name: endpoints
                          value:
                            - - name: name
                                value: string
                              - name: port
                                value: integer
                        - name: resources
                          value:
                            - name: requests
                              value:
                                - name: memoryInGB
                                  value: number
                                - name: cpu
                                  value: number
                            - name: limits
                              value:
                                - name: memoryInGB
                                  value: number
                                - name: cpu
                                  value: number
                        - name: volumeRefs
                          value:
                            - - name: name
                                value: string
                              - name: readOnly
                                value: boolean
                              - name: destinationPath
                                value: string
                        - name: volumes
                          value:
                            - - name: name
                                value: string
                              - name: readOnly
                                value: boolean
                              - name: destinationPath
                                value: string
                              - name: creationParameters
                                value:
                                  - name: kind
                                    value: []
                                  - name: description
                                    value: string
                        - name: diagnostics
                          value:
                            - name: enabled
                              value: boolean
                            - name: sinkRefs
                              value:
                                - string
                        - name: reliableCollectionsRefs
                          value:
                            - - name: name
                                value: string
                              - name: doNotPersistState
                                value: boolean
                        - name: instanceView
                          value:
                            - name: restartCount
                              value: integer
                            - name: currentState
                              value:
                                - name: state
                                  value: string
                                - name: startTime
                                  value: string
                                - name: exitCode
                                  value: string
                                - name: finishTime
                                  value: string
                                - name: detailStatus
                                  value: string
                            - name: events
                              value:
                                - - name: name
                                    value: string
                                  - name: count
                                    value: integer
                                  - name: firstTimestamp
                                    value: string
                                  - name: lastTimestamp
                                    value: string
                                  - name: message
                                    value: string
                                  - name: type
                                    value: string
                  - name: networkRefs
                    value:
                      - - name: name
                          value: string
                        - name: endpointRefs
                          value:
                            - - name: name
                                value: string
                  - name: description
                    value: string
                  - name: replicaCount
                    value: integer
                  - name: autoScalingPolicies
                    value:
                      - - name: name
                          value: string
                        - name: trigger
                          value:
                            - name: kind
                              value: []
                        - name: mechanism
                          value:
                            - name: kind
                              value: []
                  - name: status
                    value: []
                  - name: statusDetails
                    value: string
                  - name: healthState
                    value: []
                  - name: unhealthyEvaluation
                    value: string
        - name: diagnostics
          value:
            - name: sinks
              value:
                - - name: kind
                    value: []
                  - name: name
                    value: string
                  - name: description
                    value: string
            - name: enabled
              value: boolean
            - name: defaultSinkRefs
              value:
                - string
        - name: debugParams
          value: string
        - name: serviceNames
          value:
            - string
        - name: statusDetails
          value: string
        - name: unhealthyEvaluation
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>applications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric_mesh.applications
WHERE applicationResourceName = '{{ applicationResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
