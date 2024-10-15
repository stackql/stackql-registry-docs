---
title: security_partner_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - security_partner_providers
  - network
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

Creates, updates, deletes, gets or lists a <code>security_partner_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_partner_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.security_partner_providers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_partner_providers', value: 'view', },
        { label: 'security_partner_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityPartnerProviderName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_provider_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_hub" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the Security Partner Provider. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, securityPartnerProviderName, subscriptionId" /> | Gets the specified Security Partner Provider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the Security Partner Providers in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Security Partner Providers in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, securityPartnerProviderName, subscriptionId" /> | Creates or updates the specified Security Partner Provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, securityPartnerProviderName, subscriptionId" /> | Deletes the specified Security Partner Provider. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, securityPartnerProviderName, subscriptionId" /> | Updates tags of a Security Partner Provider resource. |

## `SELECT` examples

Gets all the Security Partner Providers in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_partner_providers', value: 'view', },
        { label: 'security_partner_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
connection_status,
etag,
location,
provisioning_state,
resourceGroupName,
securityPartnerProviderName,
security_provider_name,
subscriptionId,
tags,
type,
virtual_hub
FROM azure.network.vw_security_partner_providers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.security_partner_providers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_partner_providers</code> resource.

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
INSERT INTO azure.network.security_partner_providers (
resourceGroupName,
securityPartnerProviderName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ securityPartnerProviderName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ id }}',
'{{ location }}',
'{{ tags }}'
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
          value: []
        - name: securityProviderName
          value: []
        - name: connectionStatus
          value: []
        - name: virtualHub
          value:
            - name: id
              value: string
    - name: etag
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>security_partner_providers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.security_partner_providers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND securityPartnerProviderName = '{{ securityPartnerProviderName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
