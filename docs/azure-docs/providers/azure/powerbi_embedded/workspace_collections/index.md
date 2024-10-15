---
title: workspace_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_collections
  - powerbi_embedded
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

Creates, updates, deletes, gets or lists a <code>workspace_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_embedded.workspace_collections" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceCollectionName" /> | Creates a new Power BI Workspace Collection with the specified properties. A Power BI Workspace Collection contains one or more workspaces, and can be used to provision keys that provide API access to those workspaces. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceCollectionName" /> | Delete a Power BI Workspace Collection. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceCollectionName" /> | Update an existing Power BI Workspace Collection with the specified properties. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Verify the specified Power BI Workspace Collection name is valid and not already in use. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Migrates an existing Power BI Workspace Collection to a different resource group and/or subscription. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceCollectionName" /> | Regenerates the primary or secondary access key for the specified Power BI Workspace Collection. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_collections</code> resource.

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
INSERT INTO azure.powerbi_embedded.workspace_collections (
resourceGroupName,
subscriptionId,
workspaceCollectionName,
location,
tags,
sku
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceCollectionName }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspace_collections</code> resource.

```sql
/*+ update */
UPDATE azure.powerbi_embedded.workspace_collections
SET 
tags = '{{ tags }}',
sku = '{{ sku }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceCollectionName = '{{ workspaceCollectionName }}';
```

## `DELETE` example

Deletes the specified <code>workspace_collections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.powerbi_embedded.workspace_collections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceCollectionName = '{{ workspaceCollectionName }}';
```
