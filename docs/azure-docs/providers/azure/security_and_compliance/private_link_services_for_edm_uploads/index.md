---
title: private_link_services_for_edm_uploads
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_for_edm_uploads
  - security_and_compliance
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

Creates, updates, deletes, gets or lists a <code>private_link_services_for_edm_uploads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_services_for_edm_uploads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_and_compliance.private_link_services_for_edm_uploads" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_services_for_edm_uploads', value: 'view', },
        { label: 'private_link_services_for_edm_uploads', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="access_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="cors_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="cosmos_db_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | An etag associated with the resource, used for optimistic concurrency when editing it. |
| <CopyableCode code="export_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="kind" /> | `text` | The kind of the service. |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | An etag associated with the resource, used for optimistic concurrency when editing it. |
| <CopyableCode code="identity" /> | `object` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="kind" /> | `string` | The kind of the service. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of a service instance. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get the metadata of a privateLinkServicesForEDMUpload resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the privateLinkServicesForEDMUpload instances in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the service instances in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create or update the metadata of a privateLinkServicesForEDMUpload instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Update the metadata of a privateLinkServicesForEDMUpload instance. |

## `SELECT` examples

Get all the privateLinkServicesForEDMUpload instances in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_services_for_edm_uploads', value: 'view', },
        { label: 'private_link_services_for_edm_uploads', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
access_policies,
authentication_configuration,
cors_configuration,
cosmos_db_configuration,
etag,
export_configuration,
identity,
kind,
location,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
resourceName,
subscriptionId,
system_data,
tags,
type
FROM azure.security_and_compliance.vw_private_link_services_for_edm_uploads
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
kind,
location,
properties,
systemData,
tags,
type
FROM azure.security_and_compliance.private_link_services_for_edm_uploads
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_link_services_for_edm_uploads</code> resource.

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
INSERT INTO azure.security_and_compliance.private_link_services_for_edm_uploads (
resourceGroupName,
resourceName,
subscriptionId,
properties,
systemData,
kind,
location,
tags,
etag,
identity
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ systemData }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
'{{ etag }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: accessPolicies
          value: []
        - name: cosmosDbConfiguration
          value:
            - name: offerThroughput
              value: integer
            - name: keyVaultKeyUri
              value: string
        - name: authenticationConfiguration
          value:
            - name: authority
              value: string
            - name: audience
              value: string
            - name: smartProxyEnabled
              value: boolean
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
            - - name: systemData
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
              - name: properties
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
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: kind
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: etag
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>private_link_services_for_edm_uploads</code> resource.

```sql
/*+ update */
UPDATE azure.security_and_compliance.private_link_services_for_edm_uploads
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
