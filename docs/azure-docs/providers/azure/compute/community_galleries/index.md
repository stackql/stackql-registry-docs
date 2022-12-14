---
title: community_galleries
hide_title: false
hide_table_of_contents: false
keywords:
  - community_galleries
  - compute
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
<tr><td><b>Name</b></td><td><code>community_galleries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.community_galleries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `type` | `string` | Resource type |
| `identifier` | `object` | The identifier information of community gallery. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `CommunityGalleries_Get` | `SELECT` | `location, publicGalleryName, subscriptionId` |
