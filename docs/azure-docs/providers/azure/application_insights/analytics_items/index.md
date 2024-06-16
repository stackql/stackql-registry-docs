---
title: analytics_items
hide_title: false
hide_table_of_contents: false
keywords:
  - analytics_items
  - application_insights
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




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
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, scopePath, subscriptionId" /> | Gets a list of Analytics Items defined within an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, scopePath, subscriptionId" /> | Deletes a specific Analytics Items defined within an Application Insights component. |
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, scopePath, subscriptionId" /> | Gets a specific Analytics Items defined within an Application Insights component. |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, scopePath, subscriptionId" /> | Adds or Updates a specific Analytics Item within an Application Insights component. |
