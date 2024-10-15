---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - video_indexer
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.video_indexer.accounts" /></td></tr>
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
| <CopyableCode code="account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_services" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_seconds_indexed" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Azure Video Indexer account properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the properties of an Azure Video Indexer account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all Azure Video Indexer accounts available under the subscription |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all Azure Video Indexer accounts available under the resource group |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Creates or updates an Azure Video Indexer account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Delete an Azure Video Indexer account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing Azure Video Indexer account. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks that the Video Indexer account name is valid and is not already in use. |

## `SELECT` examples

List all Azure Video Indexer accounts available under the subscription

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
account_id,
account_name,
identity,
location,
provisioning_state,
resourceGroupName,
storage_services,
subscriptionId,
system_data,
tags,
tenant_id,
total_seconds_indexed
FROM azure_extras.video_indexer.vw_accounts
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
FROM azure_extras.video_indexer.accounts
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
INSERT INTO azure_extras.video_indexer.accounts (
accountName,
resourceGroupName,
subscriptionId,
properties,
identity,
tags,
location
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: tenantId
          value: string
        - name: accountId
          value: string
        - name: accountName
          value: string
        - name: storageServices
          value:
            - name: resourceId
              value: string
            - name: userAssignedIdentity
              value: string
        - name: totalSecondsIndexed
          value: integer
        - name: provisioningState
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>accounts</code> resource.

```sql
/*+ update */
UPDATE azure_extras.video_indexer.accounts
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
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
DELETE FROM azure_extras.video_indexer.accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
