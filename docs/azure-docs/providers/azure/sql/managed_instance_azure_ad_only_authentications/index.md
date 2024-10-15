---
title: managed_instance_azure_ad_only_authentications
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_azure_ad_only_authentications
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

Creates, updates, deletes, gets or lists a <code>managed_instance_azure_ad_only_authentications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instance_azure_ad_only_authentications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_azure_ad_only_authentications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_azure_ad_only_authentications', value: 'view', },
        { label: 'managed_instance_azure_ad_only_authentications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authenticationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_ad_only_authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a active directory only authentication for Managed Instance. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authenticationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a specific Azure Active Directory only authentication property. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authenticationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Sets Server Active Directory only authentication property or updates an existing server Active Directory only authentication property. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authenticationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes an existing server Active Directory only authentication property. |

## `SELECT` examples

Gets a specific Azure Active Directory only authentication property.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_azure_ad_only_authentications', value: 'view', },
        { label: 'managed_instance_azure_ad_only_authentications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authenticationName,
azure_ad_only_authentication,
managedInstanceName,
resourceGroupName,
subscriptionId
FROM azure.sql.vw_managed_instance_azure_ad_only_authentications
WHERE authenticationName = '{{ authenticationName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_instance_azure_ad_only_authentications
WHERE authenticationName = '{{ authenticationName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_instance_azure_ad_only_authentications</code> resource.

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
INSERT INTO azure.sql.managed_instance_azure_ad_only_authentications (
authenticationName,
managedInstanceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ authenticationName }}',
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
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
        - name: azureADOnlyAuthentication
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>managed_instance_azure_ad_only_authentications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.managed_instance_azure_ad_only_authentications
WHERE authenticationName = '{{ authenticationName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
