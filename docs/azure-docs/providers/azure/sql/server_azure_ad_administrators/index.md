---
title: server_azure_ad_administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - server_azure_ad_administrators
  - sql
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

Creates, updates, deletes, gets or lists a <code>server_azure_ad_administrators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_azure_ad_administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_azure_ad_administrators" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_azure_ad_administrators', value: 'view', },
        { label: 'server_azure_ad_administrators', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administratorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrator_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_ad_only_authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="login" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a active directory administrator. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="administratorName, resourceGroupName, serverName, subscriptionId" /> | Gets a Azure Active Directory administrator. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of Azure Active Directory administrators in a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="administratorName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates an existing Azure Active Directory administrator. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="administratorName, resourceGroupName, serverName, subscriptionId" /> | Deletes the Azure Active Directory administrator with the given name. |

## `SELECT` examples

Gets a list of Azure Active Directory administrators in a server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_azure_ad_administrators', value: 'view', },
        { label: 'server_azure_ad_administrators', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administratorName,
administrator_type,
azure_ad_only_authentication,
login,
resourceGroupName,
serverName,
sid,
subscriptionId,
tenant_id
FROM azure.sql.vw_server_azure_ad_administrators
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.server_azure_ad_administrators
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_azure_ad_administrators</code> resource.

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
INSERT INTO azure.sql.server_azure_ad_administrators (
administratorName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ administratorName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: administratorType
          value: string
        - name: login
          value: string
        - name: sid
          value: string
        - name: tenantId
          value: string
        - name: azureADOnlyAuthentication
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>server_azure_ad_administrators</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.server_azure_ad_administrators
WHERE administratorName = '{{ administratorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
