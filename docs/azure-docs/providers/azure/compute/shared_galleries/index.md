---
title: shared_galleries
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_galleries
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
<tr><td><b>Name</b></td><td><code>shared_galleries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.shared_galleries</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SharedGalleries_Get` | `SELECT` | `galleryUniqueName, location, subscriptionId` | Get a shared gallery by subscription id or tenant id. |
| `SharedGalleries_List` | `SELECT` | `location, subscriptionId` | List shared galleries by subscription id or tenant id. |
