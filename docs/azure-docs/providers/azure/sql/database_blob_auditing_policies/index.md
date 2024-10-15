---
title: database_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - database_blob_auditing_policies
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

Creates, updates, deletes, gets or lists a <code>database_blob_auditing_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.database_blob_auditing_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_blob_auditing_policies', value: 'view', },
        { label: 'database_blob_auditing_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="audit_actions_and_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="blobAuditingPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_azure_monitor_target_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_managed_identity_in_use" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_storage_secondary_key_in_use" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Resource kind. |
| <CopyableCode code="queue_delay_ms" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_access_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Resource kind. |
| <CopyableCode code="properties" /> | `object` | Properties of a database blob auditing policy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blobAuditingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a database's blob auditing policy. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Lists auditing settings of a database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="blobAuditingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a database's blob auditing policy. |

## `SELECT` examples

Lists auditing settings of a database.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_blob_auditing_policies', value: 'view', },
        { label: 'database_blob_auditing_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
audit_actions_and_groups,
blobAuditingPolicyName,
databaseName,
is_azure_monitor_target_enabled,
is_managed_identity_in_use,
is_storage_secondary_key_in_use,
kind,
queue_delay_ms,
resourceGroupName,
retention_days,
serverName,
state,
storage_account_access_key,
storage_account_subscription_id,
storage_endpoint,
subscriptionId
FROM azure.sql.vw_database_blob_auditing_policies
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
properties
FROM azure.sql.database_blob_auditing_policies
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_blob_auditing_policies</code> resource.

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
INSERT INTO azure.sql.database_blob_auditing_policies (
blobAuditingPolicyName,
databaseName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ blobAuditingPolicyName }}',
'{{ databaseName }}',
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
    - name: kind
      value: string
    - name: properties
      value:
        - name: retentionDays
          value: integer
        - name: auditActionsAndGroups
          value:
            - string
        - name: isStorageSecondaryKeyInUse
          value: boolean
        - name: isAzureMonitorTargetEnabled
          value: boolean
        - name: queueDelayMs
          value: integer
        - name: isManagedIdentityInUse
          value: boolean
        - name: state
          value: string
        - name: storageEndpoint
          value: string
        - name: storageAccountAccessKey
          value: string
        - name: storageAccountSubscriptionId
          value: string

```
</TabItem>
</Tabs>
