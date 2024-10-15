---
title: fhir_services
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_services
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

Creates, updates, deletes, gets or lists a <code>fhir_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.fhir_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_fhir_services', value: 'view', },
        { label: 'fhir_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="acr_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="cors_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="export_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="fhirServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="implementation_guides_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="import_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind of the service. |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_version_policy_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="kind" /> | `string` | The kind of the service. |
| <CopyableCode code="properties" /> | `object` | Fhir Service properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fhirServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the properties of the specified FHIR Service. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all FHIR Services for the given workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fhirServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a FHIR Service resource with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fhirServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a FHIR Service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fhirServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Patch FHIR Service details. |

## `SELECT` examples

Lists all FHIR Services for the given workspace

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_fhir_services', value: 'view', },
        { label: 'fhir_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
acr_configuration,
authentication_configuration,
cors_configuration,
encryption,
event_state,
export_configuration,
fhirServiceName,
identity,
implementation_guides_configuration,
import_configuration,
kind,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
resource_version_policy_configuration,
subscriptionId,
system_data,
workspaceName
FROM azure_extras.healthcare.vw_fhir_services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
kind,
properties,
systemData
FROM azure_extras.healthcare.fhir_services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>fhir_services</code> resource.

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
INSERT INTO azure_extras.healthcare.fhir_services (
fhirServiceName,
resourceGroupName,
subscriptionId,
workspaceName,
identity,
kind,
properties,
systemData
)
SELECT 
'{{ fhirServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ identity }}',
'{{ kind }}',
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
    - name: kind
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: acrConfiguration
          value:
            - name: loginServers
              value:
                - string
            - name: ociArtifacts
              value:
                - - name: loginServer
                    value: string
                  - name: imageName
                    value: string
                  - name: digest
                    value: string
        - name: authenticationConfiguration
          value:
            - name: authority
              value: string
            - name: audience
              value: string
            - name: smartProxyEnabled
              value: boolean
            - name: smartIdentityProviders
              value:
                - - name: authority
                    value: string
                  - name: applications
                    value:
                      - - name: clientId
                          value: string
                        - name: audience
                          value: string
                        - name: allowedDataActions
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
        - name: exportConfiguration
          value:
            - name: storageAccountName
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
        - name: resourceVersionPolicyConfiguration
          value:
            - name: default
              value: []
            - name: resourceTypeOverrides
              value: object
        - name: importConfiguration
          value:
            - name: integrationDataStore
              value: string
            - name: initialImportMode
              value: boolean
            - name: enabled
              value: boolean
        - name: implementationGuidesConfiguration
          value:
            - name: usCoreMissingData
              value: boolean
        - name: encryption
          value:
            - name: customerManagedKeyEncryption
              value:
                - name: keyEncryptionKeyUrl
                  value: string
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

Updates a <code>fhir_services</code> resource.

```sql
/*+ update */
UPDATE azure_extras.healthcare.fhir_services
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
fhirServiceName = '{{ fhirServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>fhir_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.healthcare.fhir_services
WHERE fhirServiceName = '{{ fhirServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
