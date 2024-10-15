---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.workspaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspaces', value: 'view', },
        { label: 'workspaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_data_collection_rule_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag of the workspace. |
| <CopyableCode code="features" /> | `text` | field from the `properties` object |
| <CopyableCode code="force_cmk_for_query" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="modified_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_scoped_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access_for_ingestion" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access_for_query" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_capping" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The etag of the workspace. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Workspace properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets a workspace instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the workspaces in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets workspaces in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Create or update a workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Deletes a workspace resource. To recover the workspace, create it again with the same name, in the same subscription, resource group and location. The name is kept for 14 days and cannot be used for another workspace. To remove the workspace completely and release the name, use the force flag. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Updates a workspace. |

## `SELECT` examples

Gets the workspaces in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspaces', value: 'view', },
        { label: 'workspaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
created_date,
customer_id,
default_data_collection_rule_resource_id,
etag,
features,
force_cmk_for_query,
identity,
location,
modified_date,
private_link_scoped_resources,
provisioning_state,
public_network_access_for_ingestion,
public_network_access_for_query,
resourceGroupName,
retention_in_days,
sku,
subscriptionId,
system_data,
tags,
workspaceName,
workspace_capping
FROM azure.log_analytics.vw_workspaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
location,
properties,
systemData,
tags
FROM azure.log_analytics.workspaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspaces</code> resource.

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
INSERT INTO azure.log_analytics.workspaces (
resourceGroupName,
subscriptionId,
workspaceName,
properties,
identity,
etag,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ properties }}',
'{{ identity }}',
'{{ etag }}',
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
        - name: provisioningState
          value: string
        - name: customerId
          value: string
        - name: sku
          value:
            - name: name
              value: string
            - name: capacityReservationLevel
              value: integer
            - name: lastSkuUpdate
              value: string
        - name: retentionInDays
          value: integer
        - name: workspaceCapping
          value:
            - name: dailyQuotaGb
              value: number
            - name: quotaNextResetTime
              value: string
            - name: dataIngestionStatus
              value: string
        - name: createdDate
          value: string
        - name: modifiedDate
          value: string
        - name: publicNetworkAccessForIngestion
          value: []
        - name: forceCmkForQuery
          value: boolean
        - name: privateLinkScopedResources
          value:
            - - name: resourceId
                value: string
              - name: scopeId
                value: string
        - name: features
          value:
            - name: enableDataExport
              value: boolean
            - name: immediatePurgeDataOn30Days
              value: boolean
            - name: enableLogAccessUsingOnlyResourcePermissions
              value: boolean
            - name: clusterResourceId
              value: string
            - name: disableLocalAuth
              value: boolean
            - name: unifiedSentinelBillingOnly
              value: boolean
        - name: defaultDataCollectionRuleResourceId
          value: string
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
    - name: etag
      value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspaces</code> resource.

```sql
/*+ update */
UPDATE azure.log_analytics.workspaces
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>workspaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.log_analytics.workspaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
