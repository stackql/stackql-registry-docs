---
title: private_link_for_azure_ads
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_for_azure_ads
  - azure_active_directory
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

Creates, updates, deletes, gets or lists a <code>private_link_for_azure_ads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_for_azure_ads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_active_directory.private_link_for_azure_ads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `string` | Name of this resource. |
| <CopyableCode code="allTenants" /> | `boolean` | Flag indicating whether all tenants are allowed |
| <CopyableCode code="ownerTenantId" /> | `string` | Guid of the owner tenant |
| <CopyableCode code="resourceGroup" /> | `string` | Name of the resource group |
| <CopyableCode code="resourceName" /> | `string` | Name of the private link policy resource |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription Identifier |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="tenants" /> | `array` | The list of tenantIds. |
| <CopyableCode code="type" /> | `string` | Type of this resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Gets a private link policy with a given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Operation to return the list of Private Link Policies For AzureAD scoped to the resourceGroup. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all  Private Link Policies For AzureAD in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Creates a private link policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Deletes a private link policy. When operation completes, status code 200 returned without content. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Updates private link policy tags with specified values. |

## `SELECT` examples

Lists all  Private Link Policies For AzureAD in the given subscription.


```sql
SELECT
id,
name,
allTenants,
ownerTenantId,
resourceGroup,
resourceName,
subscriptionId,
tags,
tenants,
type
FROM azure.azure_active_directory.private_link_for_azure_ads
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_link_for_azure_ads</code> resource.

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
INSERT INTO azure.azure_active_directory.private_link_for_azure_ads (
policyName,
resourceGroupName,
subscriptionId,
name,
ownerTenantId,
allTenants,
tenants,
resourceName,
subscriptionId,
resourceGroup,
tags
)
SELECT 
'{{ policyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ name }}',
'{{ ownerTenantId }}',
{{ allTenants }},
'{{ tenants }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ resourceGroup }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: ownerTenantId
      value: string
    - name: allTenants
      value: boolean
    - name: tenants
      value:
        - string
    - name: resourceName
      value: string
    - name: subscriptionId
      value: string
    - name: resourceGroup
      value: string
    - name: tags
      value: object
    - name: id
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>private_link_for_azure_ads</code> resource.

```sql
/*+ update */
UPDATE azure.azure_active_directory.private_link_for_azure_ads
SET 
tags = '{{ tags }}'
WHERE 
policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>private_link_for_azure_ads</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_active_directory.private_link_for_azure_ads
WHERE policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
