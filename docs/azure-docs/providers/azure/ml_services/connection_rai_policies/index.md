---
title: connection_rai_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_rai_policies
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>connection_rai_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_rai_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.connection_rai_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connection_rai_policies', value: 'view', },
        { label: 'connection_rai_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="base_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="completion_blocklists" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_filters" /> | `text` | field from the `properties` object |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="prompt_blocklists" /> | `text` | field from the `properties` object |
| <CopyableCode code="raiPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Azure OpenAI Content Filters properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, raiPolicyName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="connectionName, raiPolicyName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, raiPolicyName, resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connection_rai_policies', value: 'view', },
        { label: 'connection_rai_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
base_policy_name,
completion_blocklists,
connectionName,
content_filters,
mode,
prompt_blocklists,
raiPolicyName,
resourceGroupName,
subscriptionId,
system_data,
type,
workspaceName
FROM azure.ml_services.vw_connection_rai_policies
WHERE connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.ml_services.connection_rai_policies
WHERE connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connection_rai_policies</code> resource.

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
INSERT INTO azure.ml_services.connection_rai_policies (
connectionName,
raiPolicyName,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
properties
)
SELECT 
'{{ connectionName }}',
'{{ raiPolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
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
        - name: basePolicyName
          value: string
        - name: completionBlocklists
          value:
            - - name: blocking
                value: boolean
              - name: blocklistName
                value: string
        - name: contentFilters
          value:
            - - name: allowedContentLevel
                value: []
              - name: blocking
                value: boolean
              - name: enabled
                value: boolean
              - name: name
                value: string
              - name: source
                value: []
        - name: mode
          value: []
        - name: promptBlocklists
          value:
            - - name: blocking
                value: boolean
              - name: blocklistName
                value: string
        - name: type
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>connection_rai_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.connection_rai_policies
WHERE connectionName = '{{ connectionName }}'
AND raiPolicyName = '{{ raiPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
