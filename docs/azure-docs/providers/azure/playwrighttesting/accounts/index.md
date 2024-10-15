---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - playwrighttesting
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.playwrighttesting.accounts" /></td></tr>
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
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dashboard_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="regional_affinity" /> | `text` | field from the `properties` object |
| <CopyableCode code="reporting" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scalable_execution" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Account resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get a Account |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Account resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Account resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Create a Account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Delete a Account |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Update a Account |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Adds check global name availability operation, normally used if a resource name must be globally unique. |

## `SELECT` examples

List Account resources by subscription ID

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
accountName,
dashboard_uri,
local_auth,
location,
provisioning_state,
regional_affinity,
reporting,
resourceGroupName,
scalable_execution,
subscriptionId,
tags
FROM azure.playwrighttesting.vw_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.playwrighttesting.accounts
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
INSERT INTO azure.playwrighttesting.accounts (
accountName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: dashboardUri
          value: string
        - name: regionalAffinity
          value: string
        - name: scalableExecution
          value: string
        - name: reporting
          value: string
        - name: localAuth
          value: string
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>accounts</code> resource.

```sql
/*+ update */
UPDATE azure.playwrighttesting.accounts
SET 
tags = '{{ tags }}',
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
DELETE FROM azure.playwrighttesting.accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
