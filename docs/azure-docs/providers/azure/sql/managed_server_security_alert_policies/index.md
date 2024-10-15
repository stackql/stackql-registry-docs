---
title: managed_server_security_alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_server_security_alert_policies
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

Creates, updates, deletes, gets or lists a <code>managed_server_security_alert_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_server_security_alert_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_server_security_alert_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_server_security_alert_policies', value: 'view', },
        { label: 'managed_server_security_alert_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="disabled_alerts" /> | `text` | field from the `properties` object |
| <CopyableCode code="email_account_admins" /> | `text` | field from the `properties` object |
| <CopyableCode code="email_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityAlertPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_access_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a security alert policy. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, securityAlertPolicyName, subscriptionId" /> | Get a managed server's threat detection policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedInstanceName, resourceGroupName, securityAlertPolicyName, subscriptionId" /> | Creates or updates a threat detection policy. |

## `SELECT` examples

Get a managed server's threat detection policy.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_server_security_alert_policies', value: 'view', },
        { label: 'managed_server_security_alert_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_time,
disabled_alerts,
email_account_admins,
email_addresses,
managedInstanceName,
resourceGroupName,
retention_days,
securityAlertPolicyName,
state,
storage_account_access_key,
storage_endpoint,
subscriptionId,
system_data
FROM azure.sql.vw_managed_server_security_alert_policies
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityAlertPolicyName = '{{ securityAlertPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.sql.managed_server_security_alert_policies
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityAlertPolicyName = '{{ securityAlertPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_server_security_alert_policies</code> resource.

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
INSERT INTO azure.sql.managed_server_security_alert_policies (
managedInstanceName,
resourceGroupName,
securityAlertPolicyName,
subscriptionId,
properties
)
SELECT 
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
'{{ securityAlertPolicyName }}',
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
