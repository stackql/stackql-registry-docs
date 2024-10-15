---
title: server_dev_ops_audit_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - server_dev_ops_audit_settings
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

Creates, updates, deletes, gets or lists a <code>server_dev_ops_audit_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_dev_ops_audit_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_dev_ops_audit_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_dev_ops_audit_settings', value: 'view', },
        { label: 'server_dev_ops_audit_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="devOpsAuditingSettingsName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_azure_monitor_target_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_managed_identity_in_use" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_access_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a server DevOps audit settings. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devOpsAuditingSettingsName, resourceGroupName, serverName, subscriptionId" /> | Gets a server's DevOps audit settings. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Lists DevOps audit settings of a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="devOpsAuditingSettingsName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a server's DevOps audit settings. |

## `SELECT` examples

Lists DevOps audit settings of a server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_dev_ops_audit_settings', value: 'view', },
        { label: 'server_dev_ops_audit_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
devOpsAuditingSettingsName,
is_azure_monitor_target_enabled,
is_managed_identity_in_use,
resourceGroupName,
serverName,
state,
storage_account_access_key,
storage_account_subscription_id,
storage_endpoint,
subscriptionId,
system_data
FROM azure.sql.vw_server_dev_ops_audit_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.sql.server_dev_ops_audit_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_dev_ops_audit_settings</code> resource.

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
INSERT INTO azure.sql.server_dev_ops_audit_settings (
devOpsAuditingSettingsName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ devOpsAuditingSettingsName }}',
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
    - name: properties
      value:
        - name: isAzureMonitorTargetEnabled
          value: boolean
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
