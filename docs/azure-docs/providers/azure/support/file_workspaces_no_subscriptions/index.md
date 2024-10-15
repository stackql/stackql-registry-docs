---
title: file_workspaces_no_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - file_workspaces_no_subscriptions
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

Creates, updates, deletes, gets or lists a <code>file_workspaces_no_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_workspaces_no_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.file_workspaces_no_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_workspaces_no_subscriptions', value: 'view', },
        { label: 'file_workspaces_no_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="fileWorkspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes the properties of a file workspace. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fileWorkspaceName" /> | Gets details for a specific file workspace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fileWorkspaceName" /> | Creates a new file workspace. |

## `SELECT` examples

Gets details for a specific file workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_workspaces_no_subscriptions', value: 'view', },
        { label: 'file_workspaces_no_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
created_on,
expiration_time,
fileWorkspaceName
FROM azure.support.vw_file_workspaces_no_subscriptions
WHERE fileWorkspaceName = '{{ fileWorkspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.support.file_workspaces_no_subscriptions
WHERE fileWorkspaceName = '{{ fileWorkspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>file_workspaces_no_subscriptions</code> resource.

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
INSERT INTO azure.support.file_workspaces_no_subscriptions (
fileWorkspaceName
)
SELECT 
'{{ fileWorkspaceName }}'
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
