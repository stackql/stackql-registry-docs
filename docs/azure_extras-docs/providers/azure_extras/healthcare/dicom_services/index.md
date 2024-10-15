---
title: dicom_services
hide_title: false
hide_table_of_contents: false
keywords:
  - dicom_services
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

Creates, updates, deletes, gets or lists a <code>dicom_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dicom_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.dicom_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dicom_services', value: 'view', },
        { label: 'dicom_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authentication_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="cors_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="dicomServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_data_partitions" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="properties" /> | `object` | Dicom Service properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dicomServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the properties of the specified DICOM Service. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all DICOM Services for the given workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dicomServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a DICOM Service resource with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dicomServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a DICOM Service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dicomServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Patch DICOM Service details. |

## `SELECT` examples

Lists all DICOM Services for the given workspace

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dicom_services', value: 'view', },
        { label: 'dicom_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authentication_configuration,
cors_configuration,
dicomServiceName,
enable_data_partitions,
encryption,
event_state,
identity,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
service_url,
storage_configuration,
subscriptionId,
system_data,
workspaceName
FROM azure_extras.healthcare.vw_dicom_services
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
FROM azure_extras.healthcare.dicom_services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dicom_services</code> resource.

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
INSERT INTO azure_extras.healthcare.dicom_services (
dicomServiceName,
resourceGroupName,
subscriptionId,
workspaceName,
identity,
properties,
systemData
)
SELECT 
'{{ dicomServiceName }}',
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
        - name: authenticationConfiguration
          value:
            - name: authority
              value: string
            - name: audiences
              value:
                - []
        - name: corsConfiguration
          value:
            - name: origins
              value:
                - []
            - name: headers
              value:
                - []
            - name: methods
              value:
                - []
            - name: maxAge
              value: integer
            - name: allowCredentials
              value: boolean
        - name: serviceUrl
          value: string
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: []
              - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
        - name: publicNetworkAccess
          value: []
        - name: eventState
          value: []
        - name: encryption
          value:
            - name: customerManagedKeyEncryption
              value:
                - name: keyEncryptionKeyUrl
                  value: string
        - name: storageConfiguration
          value:
            - name: storageResourceId
              value: string
            - name: fileSystemName
              value: string
        - name: enableDataPartitions
          value: []
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

Updates a <code>dicom_services</code> resource.

```sql
/*+ update */
UPDATE azure_extras.healthcare.dicom_services
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
dicomServiceName = '{{ dicomServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>dicom_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.healthcare.dicom_services
WHERE dicomServiceName = '{{ dicomServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
