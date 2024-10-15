---
title: analytics_items
hide_title: false
hide_table_of_contents: false
keywords:
  - analytics_items
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

Creates, updates, deletes, gets or lists a <code>analytics_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analytics_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.analytics_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="Content" /> | `string` | The content of this item |
| <CopyableCode code="Id" /> | `string` | Internally assigned unique id of the item definition. |
| <CopyableCode code="Name" /> | `string` | The user-defined name of the item. |
| <CopyableCode code="Properties" /> | `object` | A set of properties that can be defined in the context of a specific item type. Each type may have its own properties. |
| <CopyableCode code="Scope" /> | `string` | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. |
| <CopyableCode code="TimeCreated" /> | `string` | Date and time in UTC when this item was created. |
| <CopyableCode code="TimeModified" /> | `string` | Date and time in UTC of the last modification that was made to this item. |
| <CopyableCode code="Type" /> | `string` | Enum indicating the type of the Analytics item. |
| <CopyableCode code="Version" /> | `string` | This instance's version of the data model. This can change as new features are added. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, scopePath, subscriptionId" /> | Gets a specific Analytics Items defined within an Application Insights component. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, scopePath, subscriptionId" /> | Gets a list of Analytics Items defined within an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, scopePath, subscriptionId" /> | Deletes a specific Analytics Items defined within an Application Insights component. |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="resourceGroupName, resourceName, scopePath, subscriptionId" /> | Adds or Updates a specific Analytics Item within an Application Insights component. |

## `SELECT` examples

Gets a specific Analytics Items defined within an Application Insights component.


```sql
SELECT
Content,
Id,
Name,
Properties,
Scope,
TimeCreated,
TimeModified,
Type,
Version
FROM azure.application_insights.analytics_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND scopePath = '{{ scopePath }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>analytics_items</code> resource.

```sql
/*+ update */
REPLACE azure.application_insights.analytics_items
SET 
Id = '{{ Id }}',
Name = '{{ Name }}',
Content = '{{ Content }}',
Scope = '{{ Scope }}',
Type = '{{ Type }}',
Properties = '{{ Properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND scopePath = '{{ scopePath }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>analytics_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure.application_insights.analytics_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND scopePath = '{{ scopePath }}'
AND subscriptionId = '{{ subscriptionId }}';
```
