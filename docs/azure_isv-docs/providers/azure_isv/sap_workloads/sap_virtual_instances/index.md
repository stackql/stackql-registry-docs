---
title: sap_virtual_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_virtual_instances
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

Creates, updates, deletes, gets or lists a <code>sap_virtual_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sap_virtual_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.sap_virtual_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_virtual_instances', value: 'view', },
        { label: 'sap_virtual_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="health" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_resource_group_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sapVirtualInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sap_product" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the Virtual Instance for SAP solutions resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Gets a Virtual Instance for SAP solutions resource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all Virtual Instances for SAP solutions resources in a Resource Group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all Virtual Instances for SAP solutions resources in a Subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId, data__properties" /> | Creates a Virtual Instance for SAP solutions (VIS) resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Deletes a Virtual Instance for SAP solutions resource and its child resources, that is the associated Central Services Instance, Application Server Instances and Database Instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Updates a Virtual Instance for SAP solutions resource |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Starts the SAP application, that is the Central Services instance and Application server instances. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Stops the SAP Application, that is the Application server instances and Central Services instance. |

## `SELECT` examples

Gets all Virtual Instances for SAP solutions resources in a Subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_virtual_instances', value: 'view', },
        { label: 'sap_virtual_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
configuration,
environment,
errors,
health,
identity,
location,
managed_resource_group_configuration,
provisioning_state,
resourceGroupName,
sapVirtualInstanceName,
sap_product,
state,
status,
subscriptionId,
tags
FROM azure_isv.sap_workloads.vw_sap_virtual_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure_isv.sap_workloads.sap_virtual_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sap_virtual_instances</code> resource.

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
INSERT INTO azure_isv.sap_workloads.sap_virtual_instances (
resourceGroupName,
sapVirtualInstanceName,
subscriptionId,
data__properties,
tags,
location,
identity,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sapVirtualInstanceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
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
    - name: identity
      value:
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: environment
          value: []
        - name: sapProduct
          value: []
        - name: configuration
          value:
            - name: configurationType
              value: []
        - name: managedResourceGroupConfiguration
          value:
            - name: name
              value: string
        - name: status
          value: []
        - name: health
          value: []
        - name: state
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

Updates a <code>sap_virtual_instances</code> resource.

```sql
/*+ update */
UPDATE azure_isv.sap_workloads.sap_virtual_instances
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sap_virtual_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.sap_workloads.sap_virtual_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sapVirtualInstanceName = '{{ sapVirtualInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
