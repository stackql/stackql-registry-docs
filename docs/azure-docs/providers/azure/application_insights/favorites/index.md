---
title: favorites
hide_title: false
hide_table_of_contents: false
keywords:
  - favorites
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
<tr><td><b>Name</b></td><td><code>favorites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.favorites" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="Category" /> | `string` | Favorite category, as defined by the user at creation time. |
| <CopyableCode code="Config" /> | `string` | Configuration of this particular favorite, which are driven by the Azure portal UX. Configuration data is a string containing valid JSON |
| <CopyableCode code="FavoriteId" /> | `string` | Internally assigned unique id of the favorite definition. |
| <CopyableCode code="FavoriteType" /> | `string` | Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component. |
| <CopyableCode code="IsGeneratedFromTemplate" /> | `boolean` | Flag denoting wether or not this favorite was generated from a template. |
| <CopyableCode code="Name" /> | `string` | The user-defined name of the favorite. |
| <CopyableCode code="SourceType" /> | `string` | The source of the favorite definition. |
| <CopyableCode code="Tags" /> | `array` | A list of 0 or more tags that are associated with this favorite definition |
| <CopyableCode code="TimeModified" /> | `string` | Date and time in UTC of the last modification that was made to this favorite definition. |
| <CopyableCode code="UserId" /> | `string` | Unique user id of the specific user that owns this favorite. |
| <CopyableCode code="Version" /> | `string` | This instance's version of the data model. This can change as new features are added that can be marked favorite. Current examples include MetricsExplorer (ME) and Search. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="favoriteId, resourceGroupName, resourceName, subscriptionId" /> | Get a single favorite by its FavoriteId, defined within an Application Insights component. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a list of favorites defined within an Application Insights component. |
| <CopyableCode code="add" /> | `INSERT` | <CopyableCode code="favoriteId, resourceGroupName, resourceName, subscriptionId" /> | Adds a new favorites to an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="favoriteId, resourceGroupName, resourceName, subscriptionId" /> | Remove a favorite that is associated to an Application Insights component. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="favoriteId, resourceGroupName, resourceName, subscriptionId" /> | Updates a favorite that has already been added to an Application Insights component. |
