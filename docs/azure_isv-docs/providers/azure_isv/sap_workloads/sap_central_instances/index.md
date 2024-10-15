---
title: sap_central_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_central_instances
  - sap_workloads
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

Creates, updates, deletes, gets or lists a <code>sap_central_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sap_central_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.sap_central_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_central_instances', value: 'view', },
        { label: 'sap_central_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="centralInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enqueue_replication_server_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="enqueue_server_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_server_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="health" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_no" /> | `text` | field from the `properties` object |
| <CopyableCode code="kernel_patch" /> | `text` | field from the `properties` object |
| <CopyableCode code="kernel_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancer_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="message_server_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sapVirtualInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="vm_details" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the SAP Central Services Instance properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="centralInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Gets the SAP Central Services Instance resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Lists the SAP Central Services Instance resource for the given Virtual Instance for SAP solutions resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="centralInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Creates the SAP Central Services Instance resource. <br><br>This will be used by service only. PUT operation on this resource by end user will return a Bad Request error. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="centralInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Deletes the SAP Central Services Instance resource. <br><br>This will be used by service only. Delete operation on this resource by end user will return a Bad Request error. You can delete the parent resource, which is the Virtual Instance for SAP solutions resource, using the delete operation on it. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="centralInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Updates the SAP Central Services Instance resource. <br><br>This can be used to update tags on the resource. |
| <CopyableCode code="start_instance" /> | `EXEC` | <CopyableCode code="centralInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Starts the SAP Central Services Instance. |
| <CopyableCode code="stop_instance" /> | `EXEC` | <CopyableCode code="centralInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Stops the SAP Central Services Instance. |

## `SELECT` examples

Lists the SAP Central Services Instance resource for the given Virtual Instance for SAP solutions resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_central_instances', value: 'view', },
        { label: 'sap_central_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
centralInstanceName,
enqueue_replication_server_properties,
enqueue_server_properties,
errors,
gateway_server_properties,
health,
instance_no,
kernel_patch,
kernel_version,
load_balancer_details,
location,
message_server_properties,
provisioning_state,
resourceGroupName,
sapVirtualInstanceName,
status,
subnet,
subscriptionId,
tags,
vm_details
FROM azure_isv.sap_workloads.vw_sap_central_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_isv.sap_workloads.sap_central_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sap_central_instances</code> resource.

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
INSERT INTO azure_isv.sap_workloads.sap_central_instances (
centralInstanceName,
resourceGroupName,
sapVirtualInstanceName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ centralInstanceName }}',
'{{ resourceGroupName }}',
'{{ sapVirtualInstanceName }}',
'{{ subscriptionId }}',
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
        - name: instanceNo
          value: string
        - name: subnet
          value: string
        - name: messageServerProperties
          value:
            - name: msPort
              value: integer
            - name: internalMsPort
              value: integer
            - name: httpPort
              value: integer
            - name: httpsPort
              value: integer
            - name: hostname
              value: string
            - name: ipAddress
              value: string
            - name: health
              value: []
        - name: enqueueServerProperties
          value:
            - name: hostname
              value: string
            - name: ipAddress
              value: string
            - name: port
              value: integer
        - name: gatewayServerProperties
          value:
            - name: port
              value: integer
        - name: enqueueReplicationServerProperties
          value:
            - name: ersVersion
              value: []
            - name: instanceNo
              value: string
            - name: hostname
              value: string
            - name: kernelVersion
              value: string
            - name: kernelPatch
              value: string
            - name: ipAddress
              value: string
        - name: kernelVersion
          value: string
        - name: kernelPatch
          value: string
        - name: loadBalancerDetails
          value:
            - name: id
              value: string
        - name: vmDetails
          value:
            - - name: type
                value: []
              - name: virtualMachineId
                value: string
              - name: storageDetails
                value:
                  - - name: id
                      value: string
        - name: status
          value: []
        - name: provisioningState
          value: []
        - name: errors
          value:
            - name: properties
              value:
                - name: code
                  value: string
                - name: message
                  value: string
                - name: details
                  value:
                    - - name: code
                        value: string
                      - name: message
                        value: string
                      - name: details
                        value:
                          - - name: code
                              value: string
                            - name: message
                              value: string
                            - name: details
                              value:
                                - - name: code
                                    value: string
                                  - name: message
                                    value: string
                                  - name: details
                                    value:
                                      - - name: code
                                          value: string
                                        - name: message
                                          value: string
                                        - name: details
                                          value:
                                            - - name: code
                                                value: string
                                              - name: message
                                                value: string
                                              - name: details
                                                value:
                                                  - - name: code
                                                      value: string
                                                    - name: message
                                                      value: string
                                                    - name: details
                                                      value:
                                                        - - name: code
                                                            value: string
                                                          - name: message
                                                            value: string
                                                          - name: details
                                                            value:
                                                              - []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sap_central_instances</code> resource.

```sql
/*+ update */
UPDATE azure_isv.sap_workloads.sap_central_instances
SET 
tags = '{{ tags }}'
WHERE 
centralInstanceName = '{{ centralInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sap_central_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.sap_workloads.sap_central_instances
WHERE centralInstanceName = '{{ centralInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
