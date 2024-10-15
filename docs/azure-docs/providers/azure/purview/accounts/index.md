---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - purview
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

Creates, updates, deletes, gets or lists a <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_accounts', value: 'view', },
        { label: 'accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the identifier. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_connectors" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | The Managed Identity of the resource |
| <CopyableCode code="ingestion_storage" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Gets or sets the location. |
| <CopyableCode code="managed_event_hub_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_resource_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_resources_public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="merge_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Gets or sets the Sku. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags on the azure resource. |
| <CopyableCode code="tenant_endpoint_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets or sets the type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the identifier. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="identity" /> | `object` | The Managed Identity of the resource |
| <CopyableCode code="location" /> | `string` | Gets or sets the location. |
| <CopyableCode code="properties" /> | `object` | The account properties |
| <CopyableCode code="sku" /> | `object` | Gets or sets the Sku. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Tags on the azure resource. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get an account |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List accounts in ResourceGroup |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List accounts in Subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Creates or updates an account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Deletes an account resource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updates an account |
| <CopyableCode code="add_root_collection_admin" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Add the administrator for root collection associated with this account. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Checks if account name is available. |

## `SELECT` examples

List accounts in Subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_accounts', value: 'view', },
        { label: 'accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
account_status,
cloud_connectors,
created_at,
created_by,
created_by_object_id,
default_domain,
endpoints,
friendly_name,
identity,
ingestion_storage,
location,
managed_event_hub_state,
managed_resource_group_name,
managed_resources,
managed_resources_public_network_access,
merge_info,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
sku,
subscriptionId,
system_data,
tags,
tenant_endpoint_state,
type
FROM azure.purview.vw_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.purview.accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>accounts</code> resource.

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
INSERT INTO azure.purview.accounts (
accountName,
resourceGroupName,
subscriptionId,
identity,
location,
tags,
properties,
sku
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ identity }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
    - name: location
      value: string
    - name: name
      value: string
    - name: systemData
      value: string
    - name: tags
      value: object
    - name: type
      value: string
    - name: properties
      value:
        - name: accountStatus
          value: string
        - name: cloudConnectors
          value:
            - name: awsExternalId
              value: string
        - name: createdAt
          value: string
        - name: createdBy
          value: string
        - name: createdByObjectId
          value: string
        - name: defaultDomain
          value: string
        - name: endpoints
          value: string
        - name: friendlyName
          value: string
        - name: ingestionStorage
          value:
            - name: id
              value: string
            - name: primaryEndpoint
              value: string
            - name: publicNetworkAccess
              value: string
        - name: managedEventHubState
          value: string
        - name: managedResourceGroupName
          value: string
        - name: managedResources
          value: string
        - name: managedResourcesPublicNetworkAccess
          value: string
        - name: mergeInfo
          value:
            - name: accountLocation
              value: string
            - name: accountName
              value: string
            - name: accountResourceGroupName
              value: string
            - name: accountSubscriptionId
              value: string
            - name: deprovisioned
              value: boolean
            - name: mergeStatus
              value: string
            - name: typeOfAccount
              value: string
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: systemData
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: actionsRequired
                        value: string
                      - name: description
                        value: string
                      - name: status
                        value: string
                  - name: provisioningState
                    value: string
        - name: provisioningState
          value: string
        - name: publicNetworkAccess
          value: string
        - name: tenantEndpointState
          value: string
    - name: sku
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>accounts</code> resource.

```sql
/*+ update */
UPDATE azure.purview.accounts
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.purview.accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
