---
title: sql_pool_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_blob_auditing_policies
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pool_blob_auditing_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_blob_auditing_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_blob_auditing_policies', value: 'view', },
        { label: 'sql_pool_blob_auditing_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="audit_actions_and_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="blobAuditingPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_azure_monitor_target_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_storage_secondary_key_in_use" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Resource kind. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_access_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Resource kind. |
| <CopyableCode code="properties" /> | `object` | Properties of a Sql pool blob auditing policy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blobAuditingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get a SQL pool's blob auditing policy. |
| <CopyableCode code="list_by_sql_pool" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Lists auditing settings of a Sql pool. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="blobAuditingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Creates or updates a SQL pool's blob auditing policy. |

## `SELECT` examples

Lists auditing settings of a Sql pool.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_blob_auditing_policies', value: 'view', },
        { label: 'sql_pool_blob_auditing_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
audit_actions_and_groups,
blobAuditingPolicyName,
is_azure_monitor_target_enabled,
is_storage_secondary_key_in_use,
kind,
resourceGroupName,
retention_days,
sqlPoolName,
state,
storage_account_access_key,
storage_account_subscription_id,
storage_endpoint,
subscriptionId,
workspaceName
FROM azure.synapse.vw_sql_pool_blob_auditing_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
properties
FROM azure.synapse.sql_pool_blob_auditing_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_pool_blob_auditing_policies</code> resource.

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
INSERT INTO azure.synapse.sql_pool_blob_auditing_policies (
blobAuditingPolicyName,
resourceGroupName,
sqlPoolName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ blobAuditingPolicyName }}',
'{{ resourceGroupName }}',
'{{ sqlPoolName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: properties
      value:
        - name: state
          value: string
        - name: storageEndpoint
          value: string
        - name: storageAccountAccessKey
          value: string
        - name: retentionDays
          value: integer
        - name: auditActionsAndGroups
          value:
            - string
        - name: storageAccountSubscriptionId
          value: string
        - name: isStorageSecondaryKeyInUse
          value: boolean
        - name: isAzureMonitorTargetEnabled
          value: boolean

```
</TabItem>
</Tabs>
