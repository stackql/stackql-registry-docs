---
title: mediaservices
hide_title: false
hide_table_of_contents: false
keywords:
  - mediaservices
  - media_services
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

Creates, updates, deletes, gets or lists a <code>mediaservices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mediaservices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.mediaservices" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mediaservices', value: 'view', },
        { label: 'mediaservices', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_delivery" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="media_service_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="minimum_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the Media Services account. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get the details of a Media Services account |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Media Services accounts in the resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Media Services accounts in the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Creates or updates a Media Services account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Deletes a Media Services account |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updates an existing Media Services account |
| <CopyableCode code="sync_storage_keys" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Synchronizes storage account keys for a storage account associated with the Media Service account. |

## `SELECT` examples

List Media Services accounts in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mediaservices', value: 'view', },
        { label: 'mediaservices', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
encryption,
identity,
key_delivery,
location,
media_service_id,
minimum_tls_version,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
storage_accounts,
storage_authentication,
subscriptionId,
system_data,
tags
FROM azure.media_services.vw_mediaservices
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
systemData,
tags
FROM azure.media_services.mediaservices
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mediaservices</code> resource.

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
INSERT INTO azure.media_services.mediaservices (
accountName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
identity
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ identity }}'
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
        - name: mediaServiceId
          value: string
        - name: storageAccounts
          value:
            - - name: id
                value: string
              - name: type
                value: string
              - name: identity
                value:
                  - name: userAssignedIdentity
                    value: string
                  - name: useSystemAssignedIdentity
                    value: boolean
              - name: status
                value: string
        - name: storageAuthentication
          value: string
        - name: encryption
          value:
            - name: type
              value: string
            - name: keyVaultProperties
              value:
                - name: keyIdentifier
                  value: string
                - name: identity
                  value: string
            - name: status
              value: string
        - name: keyDelivery
          value:
            - name: accessControl
              value:
                - name: defaultAction
                  value: string
                - name: ipAllowList
                  value:
                    - string
        - name: publicNetworkAccess
          value: string
        - name: provisioningState
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
        - name: minimumTlsVersion
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>mediaservices</code> resource.

```sql
/*+ update */
UPDATE azure.media_services.mediaservices
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>mediaservices</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.mediaservices
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
