---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - cognitive_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.accounts" /></td></tr>
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
| <CopyableCode code="abuse_penalty" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_fqdn_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="aml_workspace" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="call_rate_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="commitment_plan_associations" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_sub_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="date_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="dynamic_throttling_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="internal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_migrated" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind (type) of cognitive service account. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_token" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_acls" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="quota_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="rai_monitor_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore" /> | `text` | field from the `properties` object |
| <CopyableCode code="restrict_outbound_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_purge_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="sku_change_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_owned_storage" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | The kind (type) of cognitive service account. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of Cognitive Services account. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Returns a Cognitive Services account specified by the parameters. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all the resources of a particular type belonging to a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all the resources of a particular type belonging to a resource group |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Create Cognitive Services Account. Accounts is a resource group wide resource type. It holds the keys for developer to access intelligent APIs. It's also the resource type for billing. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Deletes a Cognitive Services account from the resource group.  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updates a Cognitive Services account |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__keyName" /> | Regenerates the specified account key for the specified Cognitive Services account. |

## `SELECT` examples

Returns all the resources of a particular type belonging to a subscription.

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
abuse_penalty,
accountName,
allowed_fqdn_list,
aml_workspace,
api_properties,
call_rate_limit,
capabilities,
commitment_plan_associations,
custom_sub_domain_name,
date_created,
deletion_date,
disable_local_auth,
dynamic_throttling_enabled,
encryption,
endpoint,
endpoints,
etag,
identity,
internal_id,
is_migrated,
kind,
location,
locations,
migration_token,
network_acls,
private_endpoint_connections,
provisioning_state,
public_network_access,
quota_limit,
rai_monitor_config,
resourceGroupName,
restore,
restrict_outbound_network_access,
scheduled_purge_date,
sku,
sku_change_info,
subscriptionId,
system_data,
tags,
user_owned_storage
FROM azure.cognitive_services.vw_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
kind,
location,
properties,
sku,
systemData,
tags
FROM azure.cognitive_services.accounts
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
INSERT INTO azure.cognitive_services.accounts (
accountName,
resourceGroupName,
subscriptionId,
kind,
sku,
identity,
tags,
location,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ sku }}',
'{{ identity }}',
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
    - name: kind
      value: []
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
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
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: endpoint
          value: string
        - name: internalId
          value: string
        - name: capabilities
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: isMigrated
          value: boolean
        - name: migrationToken
          value: string
        - name: skuChangeInfo
          value:
            - name: countOfDowngrades
              value: number
            - name: countOfUpgradesAfterDowngrades
              value: number
            - name: lastChangeDate
              value: string
        - name: customSubDomainName
          value: string
        - name: networkAcls
          value:
            - name: defaultAction
              value: string
            - name: bypass
              value: string
            - name: ipRules
              value:
                - - name: value
                    value: string
            - name: virtualNetworkRules
              value:
                - - name: id
                    value: string
                  - name: state
                    value: string
                  - name: ignoreMissingVnetServiceEndpoint
                    value: boolean
        - name: encryption
          value:
            - name: keyVaultProperties
              value:
                - name: keyIdentifier
                  value: string
                - name: identity
                  value: string
            - name: keySource
              value: string
        - name: userOwnedStorage
          value:
            - - name: resourceId
                value: string
              - name: identityClientId
                value: string
        - name: amlWorkspace
          value:
            - name: resourceId
              value: string
            - name: identityClientId
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
                  - name: groupIds
                    value:
                      - string
              - name: location
                value: string
              - name: etag
                value: string
        - name: publicNetworkAccess
          value: string
        - name: apiProperties
          value:
            - name: qnaRuntimeEndpoint
              value: string
            - name: qnaAzureSearchEndpointKey
              value: string
            - name: qnaAzureSearchEndpointId
              value: string
            - name: statisticsEnabled
              value: boolean
            - name: eventHubConnectionString
              value: string
            - name: storageAccountConnectionString
              value: string
            - name: aadClientId
              value: string
            - name: aadTenantId
              value: string
            - name: superUser
              value: string
            - name: websiteName
              value: string
        - name: dateCreated
          value: string
        - name: callRateLimit
          value:
            - name: count
              value: number
            - name: renewalPeriod
              value: number
            - name: rules
              value:
                - - name: key
                    value: string
                  - name: renewalPeriod
                    value: number
                  - name: count
                    value: number
                  - name: minCount
                    value: number
                  - name: dynamicThrottlingEnabled
                    value: boolean
                  - name: matchPatterns
                    value:
                      - - name: path
                          value: string
                        - name: method
                          value: string
        - name: dynamicThrottlingEnabled
          value: boolean
        - name: quotaLimit
          value:
            - name: count
              value: number
            - name: renewalPeriod
              value: number
            - name: rules
              value:
                - - name: key
                    value: string
                  - name: renewalPeriod
                    value: number
                  - name: count
                    value: number
                  - name: minCount
                    value: number
                  - name: dynamicThrottlingEnabled
                    value: boolean
                  - name: matchPatterns
                    value:
                      - - name: path
                          value: string
                        - name: method
                          value: string
        - name: restrictOutboundNetworkAccess
          value: boolean
        - name: allowedFqdnList
          value:
            - string
        - name: disableLocalAuth
          value: boolean
        - name: endpoints
          value: object
        - name: restore
          value: boolean
        - name: deletionDate
          value: string
        - name: scheduledPurgeDate
          value: string
        - name: locations
          value:
            - name: routingMethod
              value: string
            - name: regions
              value:
                - - name: name
                    value: string
                  - name: value
                    value: number
                  - name: customsubdomain
                    value: string
        - name: commitmentPlanAssociations
          value:
            - - name: commitmentPlanId
                value: string
              - name: commitmentPlanLocation
                value: string
        - name: abusePenalty
          value:
            - name: action
              value: string
            - name: rateLimitPercentage
              value: number
            - name: expiration
              value: string
        - name: raiMonitorConfig
          value:
            - name: adxStorageResourceId
              value: string
            - name: identityClientId
              value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>accounts</code> resource.

```sql
/*+ update */
UPDATE azure.cognitive_services.accounts
SET 
kind = '{{ kind }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cognitive_services.accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
