---
title: gallery_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_apps
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
<tr><td><b>Name</b></td><td><code>gallery_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.gallery_apps</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `galleryAppName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets a gallery application to prepare a test run for a Test Base Account. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all gallery applications currently available for test runs under a Test Base Account which matches user query. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all gallery applications currently available for test runs under a Test Base Account which matches user query. |
