---
title: work_item_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - work_item_configurations
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>work_item_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>work_item_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.work_item_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ConfigDisplayName" /> | `string` | Configuration friendly name |
| <CopyableCode code="ConfigProperties" /> | `string` | Serialized JSON object for detailed properties |
| <CopyableCode code="ConnectorId" /> | `string` | Connector identifier where work item is created |
| <CopyableCode code="Id" /> | `string` | Unique Id for work item |
| <CopyableCode code="IsDefault" /> | `boolean` | Boolean value indicating whether configuration is default |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the list work item configurations that exist for the application |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create a work item configuration for an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, workItemConfigId" /> | Delete a work item configuration of an Application Insights component. |

## `SELECT` examples

Gets the list work item configurations that exist for the application


```sql
SELECT
ConfigDisplayName,
ConfigProperties,
ConnectorId,
Id,
IsDefault
FROM azure.application_insights.work_item_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>work_item_configurations</code> resource.

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
INSERT INTO azure.application_insights.work_item_configurations (
resourceGroupName,
resourceName,
subscriptionId,
ConnectorId,
ConnectorDataConfiguration,
ValidateOnly,
WorkItemProperties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ ConnectorId }}',
'{{ ConnectorDataConfiguration }}',
{{ ValidateOnly }},
'{{ WorkItemProperties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: ConnectorId
      value: string
    - name: ConnectorDataConfiguration
      value: string
    - name: ValidateOnly
      value: boolean
    - name: WorkItemProperties
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>work_item_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.application_insights.work_item_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workItemConfigId = '{{ workItemConfigId }}';
```
