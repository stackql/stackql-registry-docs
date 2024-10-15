---
title: tenant_accesses
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_accesses
  - api_management
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

Creates, updates, deletes, gets or lists a <code>tenant_accesses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tenant_accesses" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tenant_accesses', value: 'view', },
        { label: 'tenant_accesses', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="accessName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Tenant access information contract of the API Management service. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Get tenant access information details without secrets. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Returns list of access infos - for Git and Management endpoints. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="If-Match, accessName, resourceGroupName, serviceName, subscriptionId" /> | Update tenant access information details. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, accessName, resourceGroupName, serviceName, subscriptionId" /> | Update tenant access information details. |
| <CopyableCode code="regenerate_git_primary_key" /> | `EXEC` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Regenerate primary access key for GIT. |
| <CopyableCode code="regenerate_git_secondary_key" /> | `EXEC` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Regenerate secondary access key for GIT. |
| <CopyableCode code="regenerate_primary_key" /> | `EXEC` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Regenerate primary access key |
| <CopyableCode code="regenerate_secondary_key" /> | `EXEC` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Regenerate secondary access key |

## `SELECT` examples

Returns list of access infos - for Git and Management endpoints.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tenant_accesses', value: 'view', },
        { label: 'tenant_accesses', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
accessName,
enabled,
principal_id,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.api_management.vw_tenant_accesses
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.tenant_accesses
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tenant_accesses</code> resource.

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
INSERT INTO azure.api_management.tenant_accesses (
If-Match,
accessName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ If-Match }}',
'{{ accessName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: principalId
          value: string
        - name: primaryKey
          value: string
        - name: secondaryKey
          value: string
        - name: enabled
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tenant_accesses</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.tenant_accesses
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND accessName = '{{ accessName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
