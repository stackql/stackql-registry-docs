---
title: web_test_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - web_test_locations
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_test_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.web_test_locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `DisplayName` | `string` | The display name of the web test location. |
| `Tag` | `string` | Internally defined geographic location tag. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `webTestLocations_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
