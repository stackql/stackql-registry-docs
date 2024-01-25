---
title: images_upload_url_for_data
hide_title: false
hide_table_of_contents: false
keywords:
  - images_upload_url_for_data
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
<tr><td><b>Name</b></td><td><code>images_upload_url_for_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.images_upload_url_for_data</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `contentUrl` | `string` | Content URL for the image blob. |
| `imageExists` | `boolean` | Whether image exists already. |
| `relativePath` | `string` | Relative path of the image. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `hubName, resourceGroupName, subscriptionId` |
