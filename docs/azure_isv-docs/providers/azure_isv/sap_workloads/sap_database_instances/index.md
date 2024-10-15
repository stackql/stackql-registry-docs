---
title: sap_database_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_database_instances
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

Creates, updates, deletes, gets or lists a <code>sap_database_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sap_database_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.sap_database_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_database_instances', value: 'view', },
        { label: 'sap_database_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_sid" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_address" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Defines the Database properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Gets the SAP Database Instance resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Lists the Database resources associated with a Virtual Instance for SAP solutions resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Creates the Database resource corresponding to the Virtual Instance for SAP solutions resource.   This will be used by service only. PUT by end user will return a Bad Request error. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Deletes the Database resource corresponding to a Virtual Instance for SAP solutions resource.   This will be used by service only. Delete by end user will return a Bad Request error. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Updates the Database resource. |
| <CopyableCode code="start_instance" /> | `EXEC` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Starts the database instance of the SAP system. |
| <CopyableCode code="stop_instance" /> | `EXEC` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Stops the database instance of the SAP system. |

## `SELECT` examples

Lists the Database resources associated with a Virtual Instance for SAP solutions resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_database_instances', value: 'view', },
        { label: 'sap_database_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseInstanceName,
database_sid,
database_type,
errors,
ip_address,
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
FROM azure_isv.sap_workloads.vw_sap_database_instances
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
FROM azure_isv.sap_workloads.sap_database_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sap_database_instances</code> resource.

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
INSERT INTO azure_isv.sap_workloads.sap_database_instances (
databaseInstanceName,
resourceGroupName,
sapVirtualInstanceName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ databaseInstanceName }}',
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
        - name: subnet
          value: string
        - name: databaseSid
          value: string
        - name: databaseType
          value: string
        - name: ipAddress
          value: string
        - name: loadBalancerDetails
          value:
            - name: id
              value: string
        - name: vmDetails
          value:
            - - name: virtualMachineId
                value: string
              - name: status
                value: []
              - name: storageDetails
                value:
                  - - name: id
                      value: string
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

Updates a <code>sap_database_instances</code> resource.

```sql
/*+ update */
UPDATE azure_isv.sap_workloads.sap_database_instances
SET 
tags = '{{ tags }}'
WHERE 
databaseInstanceName = '{{ databaseInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sap_database_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.sap_workloads.sap_database_instances
WHERE databaseInstanceName = '{{ databaseInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
