---
title: bots
hide_title: false
hide_table_of_contents: false
keywords:
  - bots
  - health_bot
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.health_bot.bots" /></td></tr>
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
| <CopyableCode code="botName" /> | `text` | field from the `properties` object |
| <CopyableCode code="bot_management_portal_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="key_vault_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a Azure Health Bot. The Health Bot Service is a cloud platform that empowers developers in Healthcare organizations to build and deploy their compliant, AI-powered virtual health assistants and health bots, that help them improve processes and reduce costs. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="botName, resourceGroupName, subscriptionId" /> | Get a HealthBot. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all the resources of a particular type belonging to a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all the resources of a particular type belonging to a resource group |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="botName, resourceGroupName, subscriptionId, data__sku" /> | Create a new Azure Health Bot. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="botName, resourceGroupName, subscriptionId" /> | Delete a HealthBot. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="botName, resourceGroupName, subscriptionId" /> | Patch a HealthBot. |
| <CopyableCode code="regenerate_api_jwt_secret" /> | `EXEC` | <CopyableCode code="botName, resourceGroupName, subscriptionId" /> | Regenerate the API JWT Secret of a HealthBot. |

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
botName,
bot_management_portal_link,
identity,
key_vault_properties,
location,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags
FROM azure_extras.health_bot.vw_bots
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
sku,
tags
FROM azure_extras.health_bot.bots
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
INSERT INTO azure_extras.health_bot.bots (
botName,
resourceGroupName,
subscriptionId,
data__sku,
tags,
location,
sku,
identity,
properties
)
SELECT 
'{{ botName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__sku }}',
'{{ tags }}',
'{{ location }}',
'{{ sku }}',
'{{ identity }}',
'{{ properties }}'
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
    - name: sku
      value:
        - name: name
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
          value: []
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: botManagementPortalLink
          value: string
        - name: keyVaultProperties
          value:
            - name: keyName
              value: string
            - name: keyVersion
              value: string
            - name: keyVaultUri
              value: string
            - name: userIdentity
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>bots</code> resource.

```sql
/*+ update */
UPDATE azure_extras.health_bot.bots
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
location = '{{ location }}'
WHERE 
botName = '{{ botName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>bots</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.health_bot.bots
WHERE botName = '{{ botName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
