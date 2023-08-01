---
title: entities_relations
hide_title: false
hide_table_of_contents: false
keywords:
  - entities_relations
  - security_insights
  - azure    
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
<tr><td><b>Name</b></td><td><code>entities_relations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.entities_relations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Relation property bag. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `EntitiesRelations_List` | `SELECT` | `entityId, resourceGroupName, subscriptionId, workspaceName` |
