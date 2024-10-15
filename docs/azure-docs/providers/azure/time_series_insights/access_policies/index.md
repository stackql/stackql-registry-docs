---
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
  - time_series_insights
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

Creates, updates, deletes, gets or lists a <code>access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.time_series_insights.access_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_policies', value: 'view', },
        { label: 'access_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accessPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="environmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="roles" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessPolicyName, environmentName, resourceGroupName, subscriptionId" /> | Gets the access policy with the specified name in the specified environment. |
| <CopyableCode code="list_by_environment" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Lists all the available access policies associated with the environment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accessPolicyName, environmentName, resourceGroupName, subscriptionId, data__properties" /> | Create or update an access policy in the specified environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessPolicyName, environmentName, resourceGroupName, subscriptionId" /> | Deletes the access policy with the specified name in the specified subscription, resource group, and environment |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accessPolicyName, environmentName, resourceGroupName, subscriptionId" /> | Updates the access policy with the specified name in the specified subscription, resource group, and environment. |

## `SELECT` examples

Lists all the available access policies associated with the environment.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_policies', value: 'view', },
        { label: 'access_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
accessPolicyName,
environmentName,
principal_object_id,
resourceGroupName,
roles,
subscriptionId,
type
FROM azure.time_series_insights.vw_access_policies
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.time_series_insights.access_policies
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_policies</code> resource.

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
INSERT INTO azure.time_series_insights.access_policies (
accessPolicyName,
environmentName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ accessPolicyName }}',
'{{ environmentName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: principalObjectId
          value: string
        - name: description
          value: string
        - name: roles
          value:
            - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>access_policies</code> resource.

```sql
/*+ update */
UPDATE azure.time_series_insights.access_policies
SET 
properties = '{{ properties }}'
WHERE 
accessPolicyName = '{{ accessPolicyName }}'
AND environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>access_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.time_series_insights.access_policies
WHERE accessPolicyName = '{{ accessPolicyName }}'
AND environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
