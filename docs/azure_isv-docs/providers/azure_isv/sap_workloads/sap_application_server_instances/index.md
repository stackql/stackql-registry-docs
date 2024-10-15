---
title: sap_application_server_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_application_server_instances
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

Creates, updates, deletes, gets or lists a <code>sap_application_server_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sap_application_server_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.sap_application_server_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_application_server_instances', value: 'view', },
        { label: 'sap_application_server_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="applicationInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="health" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostname" /> | `text` | field from the `properties` object |
| <CopyableCode code="icm_http_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="icm_https_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_no" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="kernel_patch" /> | `text` | field from the `properties` object |
| <CopyableCode code="kernel_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancer_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
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
| <CopyableCode code="properties" /> | `object` | Defines the SAP Application Server instance properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Gets the SAP Application Server Instance corresponding to the Virtual Instance for SAP solutions resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Lists the SAP Application Server Instance resources for a given Virtual Instance for SAP solutions resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Puts the SAP Application Server Instance resource. <br><br>This will be used by service only. PUT by end user will return a Bad Request error. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Deletes the SAP Application Server Instance resource. <br><br>This operation will be used by service only. Delete by end user will return a Bad Request error. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Puts the SAP Application Server Instance resource. |
| <CopyableCode code="start_instance" /> | `EXEC` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Starts the SAP Application Server Instance. |
| <CopyableCode code="stop_instance" /> | `EXEC` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Stops the SAP Application Server Instance. |

## `SELECT` examples

Lists the SAP Application Server Instance resources for a given Virtual Instance for SAP solutions resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_application_server_instances', value: 'view', },
        { label: 'sap_application_server_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
applicationInstanceName,
errors,
gateway_port,
health,
hostname,
icm_http_port,
icm_https_port,
instance_no,
ip_address,
kernel_patch,
kernel_version,
load_balancer_details,
location,
provisioning_state,
resourceGroupName,
sapVirtualInstanceName,
status,
subnet,
subscriptionId,
tags,
vm_details
FROM azure_isv.sap_workloads.vw_sap_application_server_instances
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
FROM azure_isv.sap_workloads.sap_application_server_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sap_application_server_instances</code> resource.

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
INSERT INTO azure_isv.sap_workloads.sap_application_server_instances (
applicationInstanceName,
resourceGroupName,
sapVirtualInstanceName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ applicationInstanceName }}',
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
        - name: hostname
          value: string
        - name: kernelVersion
          value: string
        - name: kernelPatch
          value: string
        - name: ipAddress
          value: string
        - name: gatewayPort
          value: integer
        - name: icmHttpPort
          value: integer
        - name: icmHttpsPort
          value: integer
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
        - name: health
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

Updates a <code>sap_application_server_instances</code> resource.

```sql
/*+ update */
UPDATE azure_isv.sap_workloads.sap_application_server_instances
SET 
tags = '{{ tags }}'
WHERE 
applicationInstanceName = '{{ applicationInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sap_application_server_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.sap_workloads.sap_application_server_instances
WHERE applicationInstanceName = '{{ applicationInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
