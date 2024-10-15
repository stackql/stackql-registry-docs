---
title: extended_server_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - extended_server_blob_auditing_policies
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

Creates, updates, deletes, gets or lists a <code>extended_server_blob_auditing_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extended_server_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.extended_server_blob_auditing_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_extended_server_blob_auditing_policies', value: 'view', },
        { label: 'extended_server_blob_auditing_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="audit_actions_and_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="blobAuditingPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_azure_monitor_target_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_devops_audit_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_managed_identity_in_use" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_storage_secondary_key_in_use" /> | `text` | field from the `properties` object |
| <CopyableCode code="predicate_expression" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Properties of an extended server blob auditing policy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blobAuditingPolicyName, resourceGroupName, serverName, subscriptionId" /> | Gets an extended server's blob auditing policy. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Lists extended auditing settings of a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="blobAuditingPolicyName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates an extended server's blob auditing policy. |

## `SELECT` examples

Lists extended auditing settings of a server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_extended_server_blob_auditing_policies', value: 'view', },
        { label: 'extended_server_blob_auditing_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
audit_actions_and_groups,
blobAuditingPolicyName,
is_azure_monitor_target_enabled,
is_devops_audit_enabled,
is_managed_identity_in_use,
is_storage_secondary_key_in_use,
predicate_expression,
queue_delay_ms,
resourceGroupName,
retention_days,
serverName,
state,
storage_account_access_key,
storage_account_subscription_id,
storage_endpoint,
subscriptionId
FROM azure.sql.vw_extended_server_blob_auditing_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.extended_server_blob_auditing_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>extended_server_blob_auditing_policies</code> resource.

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
INSERT INTO azure.sql.extended_server_blob_auditing_policies (
blobAuditingPolicyName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ blobAuditingPolicyName }}',
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
        - name: isDevopsAuditEnabled
          value: boolean
        - name: predicateExpression
          value: string
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
