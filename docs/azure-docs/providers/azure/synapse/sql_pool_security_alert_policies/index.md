---
title: sql_pool_security_alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_security_alert_policies
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

Creates, updates, deletes, gets or lists a <code>sql_pool_security_alert_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_security_alert_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_security_alert_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_security_alert_policies', value: 'view', },
        { label: 'sql_pool_security_alert_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="disabled_alerts" /> | `text` | field from the `properties` object |
| <CopyableCode code="email_account_admins" /> | `text` | field from the `properties` object |
| <CopyableCode code="email_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityAlertPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_access_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a security alert policy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, securityAlertPolicyName, sqlPoolName, subscriptionId, workspaceName" /> | Get a Sql pool's security alert policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get a list of Sql pool's security alert policies. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, securityAlertPolicyName, sqlPoolName, subscriptionId, workspaceName" /> | Create or update a Sql pool's security alert policy. |

## `SELECT` examples

Get a list of Sql pool's security alert policies.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_security_alert_policies', value: 'view', },
        { label: 'sql_pool_security_alert_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_time,
disabled_alerts,
email_account_admins,
email_addresses,
resourceGroupName,
retention_days,
securityAlertPolicyName,
sqlPoolName,
state,
storage_account_access_key,
storage_endpoint,
subscriptionId,
workspaceName
FROM azure.synapse.vw_sql_pool_security_alert_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.sql_pool_security_alert_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_pool_security_alert_policies</code> resource.

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
INSERT INTO azure.synapse.sql_pool_security_alert_policies (
resourceGroupName,
securityAlertPolicyName,
sqlPoolName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ securityAlertPolicyName }}',
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
    - name: properties
      value:
        - name: state
          value: string
        - name: disabledAlerts
          value:
            - string
        - name: emailAddresses
          value:
            - string
        - name: emailAccountAdmins
          value: boolean
        - name: storageEndpoint
          value: string
        - name: storageAccountAccessKey
          value: string
        - name: retentionDays
          value: integer
        - name: creationTime
          value: string

```
</TabItem>
</Tabs>
