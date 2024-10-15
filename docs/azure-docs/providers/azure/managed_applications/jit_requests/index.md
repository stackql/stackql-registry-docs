---
title: jit_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - jit_requests
  - managed_applications
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

Creates, updates, deletes, gets or lists a <code>jit_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jit_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_applications.jit_requests" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jit_requests', value: 'view', },
        { label: 'jit_requests', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="application_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="jitRequestName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jit_authorization_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="jit_request_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="jit_scheduling_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="updated_by" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Information about JIT request properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jitRequestName, resourceGroupName, subscriptionId" /> | Gets the JIT request. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all JIT requests within the resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all JIT requests within the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jitRequestName, resourceGroupName, subscriptionId" /> | Creates or updates the JIT request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jitRequestName, resourceGroupName, subscriptionId" /> | Deletes the JIT request. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="jitRequestName, resourceGroupName, subscriptionId" /> | Updates the JIT request. |

## `SELECT` examples

Lists all JIT requests within the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jit_requests', value: 'view', },
        { label: 'jit_requests', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
application_resource_id,
created_by,
jitRequestName,
jit_authorization_policies,
jit_request_state,
jit_scheduling_policy,
location,
provisioning_state,
publisher_tenant_id,
resourceGroupName,
subscriptionId,
system_data,
tags,
type,
updated_by
FROM azure.managed_applications.vw_jit_requests
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
tags,
type
FROM azure.managed_applications.jit_requests
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jit_requests</code> resource.

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
INSERT INTO azure.managed_applications.jit_requests (
jitRequestName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ jitRequestName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: applicationResourceId
          value: string
        - name: publisherTenantId
          value: string
        - name: jitAuthorizationPolicies
          value:
            - - name: principalId
                value: string
              - name: roleDefinitionId
                value: string
        - name: jitSchedulingPolicy
          value:
            - name: type
              value: []
            - name: duration
              value: string
            - name: startTime
              value: string
        - name: provisioningState
          value: []
        - name: jitRequestState
          value: []
        - name: createdBy
          value:
            - name: oid
              value: string
            - name: puid
              value: string
            - name: applicationId
              value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>jit_requests</code> resource.

```sql
/*+ update */
UPDATE azure.managed_applications.jit_requests
SET 
tags = '{{ tags }}'
WHERE 
jitRequestName = '{{ jitRequestName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>jit_requests</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_applications.jit_requests
WHERE jitRequestName = '{{ jitRequestName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
