---
title: tenant_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_configurations
  - portal
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

Creates, updates, deletes, gets or lists a <code>tenant_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.portal.tenant_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tenant_configurations', value: 'view', },
        { label: 'tenant_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enforce_private_markdown_storage" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Tenant Configuration Properties with Provisioning state |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName" /> | Gets the tenant configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Gets list of the tenant configurations. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="configurationName" /> | Create the tenant configuration. If configuration already exists - update it. User has to be a Tenant Admin for this operation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationName" /> | Delete the tenant configuration. User has to be a Tenant Admin for this operation. |

## `SELECT` examples

Gets list of the tenant configurations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tenant_configurations', value: 'view', },
        { label: 'tenant_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
configurationName,
enforce_private_markdown_storage,
provisioning_state
FROM azure.portal.vw_tenant_configurations
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.portal.tenant_configurations
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tenant_configurations</code> resource.

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
INSERT INTO azure.portal.tenant_configurations (
configurationName,
properties
)
SELECT 
'{{ configurationName }}',
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
        - name: enforcePrivateMarkdownStorage
          value: boolean
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>tenant_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.portal.tenant_configurations
WHERE configurationName = '{{ configurationName }}';
```
