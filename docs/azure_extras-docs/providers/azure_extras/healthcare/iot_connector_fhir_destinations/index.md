---
title: iot_connector_fhir_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_connector_fhir_destinations
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

Creates, updates, deletes, gets or lists a <code>iot_connector_fhir_destinations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_connector_fhir_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.iot_connector_fhir_destinations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_connector_fhir_destinations', value: 'view', },
        { label: 'iot_connector_fhir_destinations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="fhirDestinationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fhir_mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="fhir_service_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="iotConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_identity_resolution_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | IoT Connector destination properties for an Azure FHIR service. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fhirDestinationName, iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the properties of the specified Iot Connector FHIR destination. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fhirDestinationName, iotConnectorName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Creates or updates an IoT Connector FHIR destination resource with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fhirDestinationName, iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes an IoT Connector FHIR destination. |

## `SELECT` examples

Gets the properties of the specified Iot Connector FHIR destination.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_connector_fhir_destinations', value: 'view', },
        { label: 'iot_connector_fhir_destinations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
fhirDestinationName,
fhir_mapping,
fhir_service_resource_id,
iotConnectorName,
location,
provisioning_state,
resourceGroupName,
resource_identity_resolution_type,
subscriptionId,
system_data,
workspaceName
FROM azure_extras.healthcare.vw_iot_connector_fhir_destinations
WHERE fhirDestinationName = '{{ fhirDestinationName }}'
AND iotConnectorName = '{{ iotConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData
FROM azure_extras.healthcare.iot_connector_fhir_destinations
WHERE fhirDestinationName = '{{ fhirDestinationName }}'
AND iotConnectorName = '{{ iotConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>iot_connector_fhir_destinations</code> resource.

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
INSERT INTO azure_extras.healthcare.iot_connector_fhir_destinations (
fhirDestinationName,
iotConnectorName,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
location,
properties,
systemData
)
SELECT 
'{{ fhirDestinationName }}',
'{{ iotConnectorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ location }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: resourceIdentityResolutionType
          value: []
        - name: fhirServiceResourceId
          value: string
        - name: fhirMapping
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

## `DELETE` example

Deletes the specified <code>iot_connector_fhir_destinations</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.healthcare.iot_connector_fhir_destinations
WHERE fhirDestinationName = '{{ fhirDestinationName }}'
AND iotConnectorName = '{{ iotConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
