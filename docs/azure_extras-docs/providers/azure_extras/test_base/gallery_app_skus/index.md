---
title: gallery_app_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_app_skus
  - test_base
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
<tr><td><b>Name</b></td><td><code>gallery_app_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.gallery_app_skus</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `galleryAppName, galleryAppSkuName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets a gallery application SKU for test runs under a Test Base account. |
| `list` | `SELECT` | `galleryAppName, resourceGroupName, subscriptionId, testBaseAccountName` | Lists all SKUs of a gallery application currently available for test runs under a Test Base account. |
| `_list` | `EXEC` | `galleryAppName, resourceGroupName, subscriptionId, testBaseAccountName` | Lists all SKUs of a gallery application currently available for test runs under a Test Base account. |
