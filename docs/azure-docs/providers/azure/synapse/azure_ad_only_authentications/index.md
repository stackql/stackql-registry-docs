---
title: azure_ad_only_authentications
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_ad_only_authentications
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

Creates, updates, deletes, gets or lists a <code>azure_ad_only_authentications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_ad_only_authentications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.azure_ad_only_authentications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_ad_only_authentications', value: 'view', },
        { label: 'azure_ad_only_authentications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azureADOnlyAuthenticationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_ad_only_authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a active directory only authentication. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureADOnlyAuthenticationName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a Azure Active Directory only authentication property |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets a list of Azure Active Directory only authentication property for a workspace |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="azureADOnlyAuthenticationName, resourceGroupName, subscriptionId, workspaceName" /> | Create or Update a Azure Active Directory only authentication property for the workspaces |

## `SELECT` examples

Gets a list of Azure Active Directory only authentication property for a workspace

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_ad_only_authentications', value: 'view', },
        { label: 'azure_ad_only_authentications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azureADOnlyAuthenticationName,
azure_ad_only_authentication,
creation_date,
resourceGroupName,
state,
subscriptionId,
workspaceName
FROM azure.synapse.vw_azure_ad_only_authentications
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.azure_ad_only_authentications
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>azure_ad_only_authentications</code> resource.

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
INSERT INTO azure.synapse.azure_ad_only_authentications (
azureADOnlyAuthenticationName,
resourceGroupName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ azureADOnlyAuthenticationName }}',
'{{ resourceGroupName }}',
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
        - name: azureADOnlyAuthentication
          value: boolean
        - name: state
          value: string
        - name: creationDate
          value: string

```
</TabItem>
</Tabs>
