---
title: image_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - image_definitions
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
<tr><td><b>Name</b></td><td><code>image_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.image_definitions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `imageDefinitionName, resourceGroupName, subscriptionId, testBaseAccountName` | Get image properties under the image definition name created by test base custom image which derived from 'VHD' source. |
| `list_by_test_base_account` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | List all image definition properties created by test base custom images which are derived from 'VHD' source. |
| `create` | `INSERT` | `imageDefinitionName, resourceGroupName, subscriptionId, testBaseAccountName` | Create image definition for test base custom images which are derived from 'VHD' source. |
| `delete` | `DELETE` | `imageDefinitionName, resourceGroupName, subscriptionId, testBaseAccountName` | Delete a test base image definition resource. |
| `_list_by_test_base_account` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | List all image definition properties created by test base custom images which are derived from 'VHD' source. |
