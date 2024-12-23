---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - workspaces
  - provisioning
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>workspaces</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.workspaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'account_id', value: 'view', },
        { label: 'account_id', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="aws_region" /> | `string` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="credentials_id" /> | `string` |
| <CopyableCode code="custom_tags" /> | `object` |
| <CopyableCode code="deployment_name" /> | `string` |
| <CopyableCode code="is_no_public_ip_enabled" /> | `boolean` |
| <CopyableCode code="managed_services_customer_managed_key_id" /> | `string` |
| <CopyableCode code="network_id" /> | `string` |
| <CopyableCode code="pricing_tier" /> | `string` |
| <CopyableCode code="private_access_settings_id" /> | `string` |
| <CopyableCode code="storage_configuration_id" /> | `string` |
| <CopyableCode code="storage_customer_managed_key_id" /> | `string` |
| <CopyableCode code="workspace_id" /> | `integer` |
| <CopyableCode code="workspace_name" /> | `string` |
| <CopyableCode code="workspace_status" /> | `string` |
| <CopyableCode code="workspace_status_message" /> | `string` |
</TabItem>
<TabItem value="resource">

| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="aws_region" /> | `string` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="credentials_id" /> | `string` |
| <CopyableCode code="custom_tags" /> | `object` |
| <CopyableCode code="deployment_name" /> | `string` |
| <CopyableCode code="is_no_public_ip_enabled" /> | `boolean` |
| <CopyableCode code="managed_services_customer_managed_key_id" /> | `string` |
| <CopyableCode code="network_id" /> | `string` |
| <CopyableCode code="pricing_tier" /> | `string` |
| <CopyableCode code="private_access_settings_id" /> | `string` |
| <CopyableCode code="storage_configuration_id" /> | `string` |
| <CopyableCode code="storage_customer_managed_key_id" /> | `string` |
| <CopyableCode code="workspace_id" /> | `integer` |
| <CopyableCode code="workspace_name" /> | `string` |
| <CopyableCode code="workspace_status" /> | `string` |
| <CopyableCode code="workspace_status_message" /> | `string` |
</TabItem>
</Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, workspace_id" /> | Gets information including status for a Databricks workspace, specified by ID. In the response, the |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets a list of all workspaces associated with an account, specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a new workspace using a credential configuration and a storage configuration, an optional network configuration (if using a customer-managed VPC), an optional managed services key configuration (if using customer-managed keys for managed services), and an optional storage key configuration (if using customer-managed keys for storage). The key configurations used for managed services and storage encryption can be the same or different. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, workspace_id" /> | Terminates and deletes a Databricks workspace. From an API perspective, deletion is immediate. However, it might take a few minutes for all workspaces resources to be deleted, depending on the size and number of workspace resources. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="account_id, workspace_id" /> | Updates a workspace configuration for either a running workspace or a failed workspace. The elements that can be updated varies between these two use cases. |

## `SELECT` examples

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspaces', value: 'view' },
        { label: 'workspaces (list)', value: 'list' },
        { label: 'workspaces (get)', value: 'get' }
    ]
}>
<TabItem value="view">

```sql
SELECT
account_id,
aws_region,
creation_time,
credentials_id,
custom_tags,
deployment_name,
is_no_public_ip_enabled,
managed_services_customer_managed_key_id,
network_id,
pricing_tier,
private_access_settings_id,
storage_configuration_id,
storage_customer_managed_key_id,
workspace_id,
workspace_name,
workspace_status,
workspace_status_message
FROM databricks_account.provisioning.vw_workspaces;
```

</TabItem>
<TabItem value="list">

```sql
SELECT
account_id,
aws_region,
creation_time,
credentials_id,
custom_tags,
deployment_name,
is_no_public_ip_enabled,
managed_services_customer_managed_key_id,
network_id,
pricing_tier,
private_access_settings_id,
storage_configuration_id,
storage_customer_managed_key_id,
workspace_id,
workspace_name,
workspace_status,
workspace_status_message
FROM databricks_account.provisioning.workspaces
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
account_id,
aws_region,
creation_time,
credentials_id,
custom_tags,
deployment_name,
is_no_public_ip_enabled,
managed_services_customer_managed_key_id,
network_id,
pricing_tier,
private_access_settings_id,
storage_configuration_id,
storage_customer_managed_key_id,
workspace_id,
workspace_name,
workspace_status,
workspace_status_message
FROM databricks_account.provisioning.workspaces
WHERE account_id = '{{ account_id }}' AND
workspace_id = '{{ workspace_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspaces</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'workspaces', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.provisioning.workspaces (
account_id,
data__workspace_name,
data__network_id,
data__deployment_name,
data__aws_region,
data__credentials_id,
data__storage_configuration_id,
data__managed_services_customer_managed_key_id,
data__private_access_settings_id,
data__pricing_tier,
data__storage_customer_managed_key_id,
data__custom_tags
)
SELECT 
'{{ account_id }}',
'{{ workspace_name }}',
'{{ network_id }}',
'{{ deployment_name }}',
'{{ aws_region }}',
'{{ credentials_id }}',
'{{ storage_configuration_id }}',
'{{ managed_services_customer_managed_key_id }}',
'{{ private_access_settings_id }}',
'{{ pricing_tier }}',
'{{ storage_customer_managed_key_id }}',
'{{ custom_tags }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: workspace_name
    value: string
  - name: network_id
    value: fd0cc5bc-683c-47e9-b15e-144d7744a496
  - name: deployment_name
    value: workspace_1
  - name: aws_region
    value: us-west-2
  - name: credentials_id
    value: ccc64f28-ebdc-4c89-add9-5dcb6d7727d8
  - name: storage_configuration_id
    value: b43a6064-04c1-4e1c-88b6-d91e5b136b13
  - name: managed_services_customer_managed_key_id
    value: 849b3d6b-e68e-468d-b3e5-deb08b03c56d
  - name: private_access_settings_id
    value: 3b3bbcb5-46bd-4b03-944e-97eb44ed7991
  - name: pricing_tier
    value: PREMIUM
  - name: storage_customer_managed_key_id
    value: 14138d0f-a575-4ae2-be71-ddfd0b602286
  - name: custom_tags
    value:
      property1: string
      property2: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspaces</code> resource.

```sql
/*+ update */
UPDATE databricks_account.provisioning.workspaces
SET { field = value }
WHERE account_id = '{{ account_id }}' AND
workspace_id = '{{ workspace_id }}';
```

## `DELETE` example

Deletes a <code>workspaces</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.provisioning.workspaces
WHERE account_id = '{{ account_id }}' AND
workspace_id = '{{ workspace_id }}';
```
