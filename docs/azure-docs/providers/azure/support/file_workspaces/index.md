---
title: file_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - file_workspaces
  - support
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

Creates, updates, deletes, gets or lists a <code>file_workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.file_workspaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_workspaces', value: 'view', },
        { label: 'file_workspaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="fileWorkspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes the properties of a file workspace. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fileWorkspaceName, subscriptionId" /> | Gets details for a specific file workspace in an Azure subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fileWorkspaceName, subscriptionId" /> | Creates a new file workspace for the specified subscription. |

## `SELECT` examples

Gets details for a specific file workspace in an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_workspaces', value: 'view', },
        { label: 'file_workspaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
created_on,
expiration_time,
fileWorkspaceName,
subscriptionId
FROM azure.support.vw_file_workspaces
WHERE fileWorkspaceName = '{{ fileWorkspaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.support.file_workspaces
WHERE fileWorkspaceName = '{{ fileWorkspaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>file_workspaces</code> resource.

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
INSERT INTO azure.support.file_workspaces (
fileWorkspaceName,
subscriptionId
)
SELECT 
'{{ fileWorkspaceName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>
