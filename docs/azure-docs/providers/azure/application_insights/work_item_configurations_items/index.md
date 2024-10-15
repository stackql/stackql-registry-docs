---
title: work_item_configurations_items
hide_title: false
hide_table_of_contents: false
keywords:
  - work_item_configurations_items
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

Creates, updates, deletes, gets or lists a <code>work_item_configurations_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>work_item_configurations_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.work_item_configurations_items" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, workItemConfigId" /> | Gets specified work item configuration for an Application Insights component. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, workItemConfigId" /> | Update a work item configuration for an Application Insights component. |

## `SELECT` examples

Gets specified work item configuration for an Application Insights component.


```sql
SELECT
ConfigDisplayName,
ConfigProperties,
ConnectorId,
Id,
IsDefault
FROM azure.application_insights.work_item_configurations_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workItemConfigId = '{{ workItemConfigId }}';
```
## `UPDATE` example

Updates a <code>work_item_configurations_items</code> resource.

```sql
/*+ update */
UPDATE azure.application_insights.work_item_configurations_items
SET 
ConnectorId = '{{ ConnectorId }}',
ConnectorDataConfiguration = '{{ ConnectorDataConfiguration }}',
ValidateOnly = true|false,
WorkItemProperties = '{{ WorkItemProperties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workItemConfigId = '{{ workItemConfigId }}';
```
