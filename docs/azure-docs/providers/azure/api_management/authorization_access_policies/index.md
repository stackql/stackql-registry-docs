---
title: authorization_access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_access_policies
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

Creates, updates, deletes, gets or lists a <code>authorization_access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorization_access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorization_access_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorization_access_policies', value: 'view', },
        { label: 'authorization_access_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="app_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorizationAccessPolicyId" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorizationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorizationProviderId" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Authorization Access Policy details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationAccessPolicyId, authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the authorization access policy specified by its identifier. |
| <CopyableCode code="list_by_authorization" /> | `SELECT` | <CopyableCode code="authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of authorization access policy defined within a authorization. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationAccessPolicyId, authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates Authorization Access Policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, authorizationAccessPolicyId, authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific access policy from the Authorization. |

## `SELECT` examples

Lists a collection of authorization access policy defined within a authorization.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorization_access_policies', value: 'view', },
        { label: 'authorization_access_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
app_ids,
authorizationAccessPolicyId,
authorizationId,
authorizationProviderId,
object_id,
resourceGroupName,
serviceName,
subscriptionId,
tenant_id
FROM azure.api_management.vw_authorization_access_policies
WHERE authorizationId = '{{ authorizationId }}'
AND authorizationProviderId = '{{ authorizationProviderId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.authorization_access_policies
WHERE authorizationId = '{{ authorizationId }}'
AND authorizationProviderId = '{{ authorizationProviderId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorization_access_policies</code> resource.

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
INSERT INTO azure.api_management.authorization_access_policies (
authorizationAccessPolicyId,
authorizationId,
authorizationProviderId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ authorizationAccessPolicyId }}',
'{{ authorizationId }}',
'{{ authorizationProviderId }}',
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
        - name: appIds
          value:
            - string
        - name: tenantId
          value: string
        - name: objectId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>authorization_access_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.authorization_access_policies
WHERE If-Match = '{{ If-Match }}'
AND authorizationAccessPolicyId = '{{ authorizationAccessPolicyId }}'
AND authorizationId = '{{ authorizationId }}'
AND authorizationProviderId = '{{ authorizationProviderId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
