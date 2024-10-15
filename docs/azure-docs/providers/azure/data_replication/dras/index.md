---
title: dras
hide_title: false
hide_table_of_contents: false
keywords:
  - dras
  - data_replication
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

Creates, updates, deletes, gets or lists a <code>dras</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dras</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.dras" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dras', value: 'view', },
        { label: 'dras', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name of the resource. |
| <CopyableCode code="authentication_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricAgentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_responsive" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_heartbeat" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_access_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets or sets the type of the resource. |
| <CopyableCode code="version_number" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the resource. |
| <CopyableCode code="properties" /> | `object` | Dra model properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricAgentName, fabricName, resourceGroupName, subscriptionId" /> | Gets the details of the fabric agent. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, subscriptionId" /> | Gets the list of fabric agents in the given fabric. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricAgentName, fabricName, resourceGroupName, subscriptionId, data__properties" /> | Creates the fabric agent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricAgentName, fabricName, resourceGroupName, subscriptionId" /> | Deletes the fabric agent. |

## `SELECT` examples

Gets the list of fabric agents in the given fabric.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dras', value: 'view', },
        { label: 'dras', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
authentication_identity,
correlation_id,
custom_properties,
fabricAgentName,
fabricName,
health_errors,
is_responsive,
last_heartbeat,
machine_id,
machine_name,
provisioning_state,
resourceGroupName,
resource_access_identity,
subscriptionId,
system_data,
type,
version_number
FROM azure.data_replication.vw_dras
WHERE fabricName = '{{ fabricName }}'
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
systemData,
type
FROM azure.data_replication.dras
WHERE fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dras</code> resource.

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
INSERT INTO azure.data_replication.dras (
fabricAgentName,
fabricName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ fabricAgentName }}',
'{{ fabricName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: correlationId
          value: string
        - name: machineId
          value: string
        - name: machineName
          value: string
        - name: authenticationIdentity
          value:
            - name: tenantId
              value: string
            - name: applicationId
              value: string
            - name: objectId
              value: string
            - name: audience
              value: string
            - name: aadAuthority
              value: string
        - name: isResponsive
          value: boolean
        - name: lastHeartbeat
          value: string
        - name: versionNumber
          value: string
        - name: provisioningState
          value: string
        - name: healthErrors
          value:
            - - name: affectedResourceType
                value: string
              - name: affectedResourceCorrelationIds
                value:
                  - string
              - name: childErrors
                value:
                  - - name: code
                      value: string
                    - name: healthCategory
                      value: string
                    - name: category
                      value: string
                    - name: severity
                      value: string
                    - name: source
                      value: string
                    - name: creationTime
                      value: string
                    - name: isCustomerResolvable
                      value: boolean
                    - name: summary
                      value: string
                    - name: message
                      value: string
                    - name: causes
                      value: string
                    - name: recommendation
                      value: string
              - name: code
                value: string
              - name: healthCategory
                value: string
              - name: category
                value: string
              - name: severity
                value: string
              - name: source
                value: string
              - name: creationTime
                value: string
              - name: isCustomerResolvable
                value: boolean
              - name: summary
                value: string
              - name: message
                value: string
              - name: causes
                value: string
              - name: recommendation
                value: string
        - name: customProperties
          value:
            - name: instanceType
              value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dras</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_replication.dras
WHERE fabricAgentName = '{{ fabricAgentName }}'
AND fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
