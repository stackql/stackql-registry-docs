---
title: workspace_named_values
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_named_values
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

Creates, updates, deletes, gets or lists a <code>workspace_named_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_named_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_named_values" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_named_values', value: 'view', },
        { label: 'workspace_named_values', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault" /> | `text` | field from the `properties` object |
| <CopyableCode code="namedValueId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | NamedValue Contract properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the details of the named value specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of named values defined within a workspace in a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates or updates named value. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes specific named value from the workspace in an API Management service instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Updates the specific named value. |
| <CopyableCode code="refresh_secret" /> | `EXEC` | <CopyableCode code="namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Refresh the secret of the named value specified by its identifier. |

## `SELECT` examples

Lists a collection of named values defined within a workspace in a service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_named_values', value: 'view', },
        { label: 'workspace_named_values', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
display_name,
key_vault,
namedValueId,
provisioning_state,
resourceGroupName,
secret,
serviceName,
subscriptionId,
tags,
value,
workspaceId
FROM azure.api_management.vw_workspace_named_values
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.workspace_named_values
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_named_values</code> resource.

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
INSERT INTO azure.api_management.workspace_named_values (
namedValueId,
resourceGroupName,
serviceName,
subscriptionId,
workspaceId,
properties
)
SELECT 
'{{ namedValueId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ workspaceId }}',
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
        - name: displayName
          value: string
        - name: value
          value: string
        - name: keyVault
          value:
            - name: secretIdentifier
              value: string
            - name: identityClientId
              value: string
        - name: tags
          value:
            - string
        - name: secret
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspace_named_values</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.workspace_named_values
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND namedValueId = '{{ namedValueId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```

## `DELETE` example

Deletes the specified <code>workspace_named_values</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.workspace_named_values
WHERE If-Match = '{{ If-Match }}'
AND namedValueId = '{{ namedValueId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
