---
title: relationship_links
hide_title: false
hide_table_of_contents: false
keywords:
  - relationship_links
  - customer_insights
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relationship_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.relationship_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `properties` | `object` | The definition of relationship link. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RelationshipLinks_Get` | `SELECT` | `hubName, relationshipLinkName, resourceGroupName, subscriptionId` | Gets information about the specified relationship Link. |
| `RelationshipLinks_ListByHub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all relationship links in the hub. |
| `RelationshipLinks_CreateOrUpdate` | `INSERT` | `hubName, relationshipLinkName, resourceGroupName, subscriptionId` | Creates a relationship link or updates an existing relationship link within a hub. |
| `RelationshipLinks_Delete` | `DELETE` | `hubName, relationshipLinkName, resourceGroupName, subscriptionId` | Deletes a relationship link within a hub. |
