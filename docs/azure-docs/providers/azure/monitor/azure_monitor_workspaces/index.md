---
title: azure_monitor_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_monitor_workspaces
  - monitor
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

Creates, updates, deletes, gets or lists a <code>azure_monitor_workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_monitor_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.azure_monitor_workspaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource entity tag (ETag) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureMonitorWorkspaceName, resourceGroupName, subscriptionId" /> | Returns the specified Azure Monitor Workspace |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Azure Monitor Workspaces in the specified resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all Azure Monitor Workspaces in the specified subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="azureMonitorWorkspaceName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates an Azure Monitor Workspace |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureMonitorWorkspaceName, resourceGroupName, subscriptionId" /> | Deletes an Azure Monitor Workspace |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="azureMonitorWorkspaceName, resourceGroupName, subscriptionId" /> | Updates part of an Azure Monitor Workspace |

## `SELECT` examples

Lists all Azure Monitor Workspaces in the specified subscription


```sql
SELECT
etag,
location,
properties,
tags
FROM azure.monitor.azure_monitor_workspaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>azure_monitor_workspaces</code> resource.

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
INSERT INTO azure.monitor.azure_monitor_workspaces (
azureMonitorWorkspaceName,
resourceGroupName,
subscriptionId,
data__location,
properties,
tags,
location
)
SELECT 
'{{ azureMonitorWorkspaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value: string
    - name: etag
      value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>azure_monitor_workspaces</code> resource.

```sql
/*+ update */
UPDATE azure.monitor.azure_monitor_workspaces
SET 
tags = '{{ tags }}'
WHERE 
azureMonitorWorkspaceName = '{{ azureMonitorWorkspaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>azure_monitor_workspaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.azure_monitor_workspaces
WHERE azureMonitorWorkspaceName = '{{ azureMonitorWorkspaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
