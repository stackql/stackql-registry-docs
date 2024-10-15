---
title: bots
hide_title: false
hide_table_of_contents: false
keywords:
  - bots
  - bot_service
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

Creates, updates, deletes, gets or lists a <code>bots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.bots" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bots', value: 'view', },
        { label: 'bots', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `text` | Specifies the name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="all_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_password_hint" /> | `text` | field from the `properties` object |
| <CopyableCode code="cmek_encryption_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="cmek_key_vault_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="configured_channels" /> | `text` | field from the `properties` object |
| <CopyableCode code="developer_app_insight_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="developer_app_insights_api_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="developer_app_insights_application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_channels" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Entity Tag. |
| <CopyableCode code="icon_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_cmek_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_developer_app_insights_api_key_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_streaming_supported" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Indicates the type of bot service |
| <CopyableCode code="location" /> | `text` | Specifies the location of the resource. |
| <CopyableCode code="luis_app_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="luis_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="manifest_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_token" /> | `text` | field from the `properties` object |
| <CopyableCode code="msa_app_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="msa_app_msi_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="msa_app_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="msa_app_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_security_perimeter_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="open_with_hint" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="publishing_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema_transformation_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The SKU of the cognitive services account. |
| <CopyableCode code="storage_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Specifies the type of the resource. |
| <CopyableCode code="zones" /> | `text` | Entity zones |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `string` | Specifies the name of the resource. |
| <CopyableCode code="etag" /> | `string` | Entity Tag. |
| <CopyableCode code="kind" /> | `string` | Indicates the type of bot service |
| <CopyableCode code="location" /> | `string` | Specifies the location of the resource. |
| <CopyableCode code="properties" /> | `object` | The parameters to provide for the Bot. |
| <CopyableCode code="sku" /> | `object` | The SKU of the cognitive services account. |
| <CopyableCode code="tags" /> | `object` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the resource. |
| <CopyableCode code="zones" /> | `array` | Entity zones |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns a BotService specified by the parameters. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all the resources of a particular type belonging to a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all the resources of a particular type belonging to a resource group |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Creates a Bot Service. Bot Service is a resource group wide resource type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes a Bot Service from the resource group.  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a Bot Service |

## `SELECT` examples

Returns all the resources of a particular type belonging to a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bots', value: 'view', },
        { label: 'bots', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
all_settings,
app_password_hint,
cmek_encryption_status,
cmek_key_vault_url,
configured_channels,
developer_app_insight_key,
developer_app_insights_api_key,
developer_app_insights_application_id,
disable_local_auth,
display_name,
enabled_channels,
endpoint,
endpoint_version,
etag,
icon_url,
is_cmek_enabled,
is_developer_app_insights_api_key_set,
is_streaming_supported,
kind,
location,
luis_app_ids,
luis_key,
manifest_url,
migration_token,
msa_app_id,
msa_app_msi_resource_id,
msa_app_tenant_id,
msa_app_type,
network_security_perimeter_configurations,
open_with_hint,
parameters,
private_endpoint_connections,
provisioning_state,
public_network_access,
publishing_credentials,
resourceGroupName,
resourceName,
schema_transformation_version,
sku,
storage_resource_id,
subscriptionId,
tags,
tenant_id,
type,
zones
FROM azure.bot_service.vw_bots
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
kind,
location,
properties,
sku,
tags,
type,
zones
FROM azure.bot_service.bots
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bots</code> resource.

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
INSERT INTO azure.bot_service.bots (
resourceGroupName,
resourceName,
subscriptionId,
location,
tags,
sku,
kind,
etag,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ kind }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: []
        - name: tier
          value: string
    - name: kind
      value: []
    - name: etag
      value: string
    - name: zones
      value:
        - string
    - name: properties
      value:
        - name: displayName
          value: string
        - name: description
          value: string
        - name: iconUrl
          value: string
        - name: endpoint
          value: string
        - name: endpointVersion
          value: string
        - name: allSettings
          value: object
        - name: parameters
          value: object
        - name: manifestUrl
          value: string
        - name: msaAppType
          value: string
        - name: msaAppId
          value: string
        - name: msaAppTenantId
          value: string
        - name: msaAppMSIResourceId
          value: string
        - name: configuredChannels
          value:
            - string
        - name: enabledChannels
          value:
            - string
        - name: developerAppInsightKey
          value: string
        - name: developerAppInsightsApiKey
          value: string
        - name: developerAppInsightsApplicationId
          value: string
        - name: luisAppIds
          value:
            - string
        - name: luisKey
          value: string
        - name: isCmekEnabled
          value: boolean
        - name: cmekKeyVaultUrl
          value: string
        - name: cmekEncryptionStatus
          value: string
        - name: tenantId
          value: string
        - name: publicNetworkAccess
          value: string
        - name: isStreamingSupported
          value: boolean
        - name: isDeveloperAppInsightsApiKeySet
          value: boolean
        - name: migrationToken
          value: string
        - name: disableLocalAuth
          value: boolean
        - name: schemaTransformationVersion
          value: string
        - name: storageResourceId
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
              - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
        - name: networkSecurityPerimeterConfigurations
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: provisioningState
                    value: string
                  - name: provisioningIssues
                    value:
                      - - name: name
                          value: string
                        - name: properties
                          value:
                            - name: issueType
                              value: string
                            - name: severity
                              value: string
                            - name: description
                              value: string
                            - name: suggestedResourceIds
                              value:
                                - string
                            - name: suggestedAccessRules
                              value:
                                - - name: name
                                    value: string
                                  - name: properties
                                    value:
                                      - name: direction
                                        value: string
                                      - name: addressPrefixes
                                        value:
                                          - string
                                      - name: subscriptions
                                        value:
                                          - - name: id
                                              value: string
                                      - name: networkSecurityPerimeters
                                        value:
                                          - - name: id
                                              value: string
                                            - name: perimeterGuid
                                              value: string
                                            - name: location
                                              value: string
                                      - name: fullyQualifiedDomainNames
                                        value:
                                          - string
                                      - name: emailAddresses
                                        value:
                                          - string
                                      - name: phoneNumbers
                                        value:
                                          - string
                  - name: networkSecurityPerimeter
                    value:
                      - name: id
                        value: string
                      - name: perimeterGuid
                        value: string
                      - name: location
                        value: string
                  - name: resourceAssociation
                    value:
                      - name: name
                        value: string
                      - name: accessMode
                        value: string
                  - name: profile
                    value:
                      - name: name
                        value: string
                      - name: accessRulesVersion
                        value: integer
                      - name: accessRules
                        value:
                          - - name: name
                              value: string
                            - name: properties
                              value:
                                - name: direction
                                  value: string
                                - name: addressPrefixes
                                  value:
                                    - string
                                - name: subscriptions
                                  value:
                                    - - name: id
                                        value: string
                                - name: networkSecurityPerimeters
                                  value:
                                    - - name: id
                                        value: string
                                      - name: perimeterGuid
                                        value: string
                                      - name: location
                                        value: string
                                - name: fullyQualifiedDomainNames
                                  value:
                                    - string
                                - name: emailAddresses
                                  value:
                                    - string
                                - name: phoneNumbers
                                  value:
                                    - string
                      - name: diagnosticSettingsVersion
                        value: integer
                      - name: enabledLogCategories
                        value:
                          - string
        - name: openWithHint
          value: string
        - name: appPasswordHint
          value: string
        - name: provisioningState
          value: string
        - name: publishingCredentials
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>bots</code> resource.

```sql
/*+ update */
UPDATE azure.bot_service.bots
SET 
location = '{{ location }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
kind = '{{ kind }}',
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>bots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.bot_service.bots
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
