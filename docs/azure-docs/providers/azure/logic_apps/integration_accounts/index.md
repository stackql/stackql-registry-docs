---
title: integration_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_accounts
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_accounts', value: 'view', },
        { label: 'integration_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="integrationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="integration_service_environment" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The integration account sku. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration account properties. |
| <CopyableCode code="sku" /> | `object` | The integration account sku. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | Gets an integration account. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of integration accounts by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of integration accounts by subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | Creates or updates an integration account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | Deletes an integration account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | Updates an integration account. |
| <CopyableCode code="log_tracking_events" /> | `EXEC` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId, data__events, data__sourceType" /> | Logs the integration account's tracking events. |
| <CopyableCode code="regenerate_access_key" /> | `EXEC` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | Regenerates the integration account access key. |

## `SELECT` examples

Gets a list of integration accounts by subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_accounts', value: 'view', },
        { label: 'integration_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
integrationAccountName,
integration_service_environment,
location,
resourceGroupName,
sku,
state,
subscriptionId,
tags,
type
FROM azure.logic_apps.vw_integration_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
sku,
tags,
type
FROM azure.logic_apps.integration_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_accounts</code> resource.

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
INSERT INTO azure.logic_apps.integration_accounts (
integrationAccountName,
resourceGroupName,
subscriptionId,
properties,
sku,
location,
tags
)
SELECT 
'{{ integrationAccountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ sku }}',
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
        - name: integrationServiceEnvironment
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: type
              value: string
        - name: state
          value: []
    - name: sku
      value:
        - name: name
          value: []
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

## `UPDATE` example

Updates a <code>integration_accounts</code> resource.

```sql
/*+ update */
UPDATE azure.logic_apps.integration_accounts
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>integration_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.logic_apps.integration_accounts
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
