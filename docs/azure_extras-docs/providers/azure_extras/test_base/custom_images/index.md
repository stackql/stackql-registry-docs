---
title: custom_images
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_images
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
<tr><td><b>Name</b></td><td><code>custom_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.custom_images</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customImageName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets a test base custom image. |
| `list_by_test_base_account` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the custom images under a test base account. |
| `create` | `INSERT` | `customImageName, resourceGroupName, subscriptionId, testBaseAccountName` | Creates a test base custom image. |
| `delete` | `DELETE` | `customImageName, resourceGroupName, subscriptionId, testBaseAccountName` | Deletes a test base custom image. |
| `_list_by_test_base_account` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the custom images under a test base account. |
| `check_image_name_availability` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName, data__definitionName, data__versionName` | Checks that the test vase custom image generated from VHD resource has valid and unique definition and version, return architecture and OS state of potential existing image definition. |
