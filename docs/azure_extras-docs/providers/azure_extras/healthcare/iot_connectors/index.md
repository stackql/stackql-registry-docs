---
title: iot_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_connectors
  - healthcare
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

Creates, updates, deletes, gets or lists a <code>iot_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.iot_connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_connectors', value: 'view', },
        { label: 'iot_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="device_mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="ingestion_endpoint_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="iotConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="properties" /> | `object` | IoT Connector properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the properties of the specified IoT Connector. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all IoT Connectors for the given workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates an IoT Connector resource with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes an IoT Connector. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Patch an IoT Connector. |

## `SELECT` examples

Lists all IoT Connectors for the given workspace

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_connectors', value: 'view', },
        { label: 'iot_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
device_mapping,
identity,
ingestion_endpoint_configuration,
iotConnectorName,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
workspaceName
FROM azure_extras.healthcare.vw_iot_connectors
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
properties,
systemData
FROM azure_extras.healthcare.iot_connectors
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>iot_connectors</code> resource.

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
INSERT INTO azure_extras.healthcare.iot_connectors (
iotConnectorName,
resourceGroupName,
subscriptionId,
workspaceName,
identity,
properties,
systemData
)
SELECT 
'{{ iotConnectorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ identity }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: ingestionEndpointConfiguration
          value:
            - name: eventHubName
              value: string
            - name: consumerGroup
              value: string
            - name: fullyQualifiedEventHubNamespace
              value: string
        - name: deviceMapping
          value:
            - name: content
              value: object
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>iot_connectors</code> resource.

```sql
/*+ update */
UPDATE azure_extras.healthcare.iot_connectors
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
iotConnectorName = '{{ iotConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>iot_connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.healthcare.iot_connectors
WHERE iotConnectorName = '{{ iotConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
