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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.image_definitions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageDefinitionName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Get image properties under the image definition name created by test base custom image which derived from 'VHD' source. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | List all image definition properties created by test base custom images which are derived from 'VHD' source. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="imageDefinitionName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Create image definition for test base custom images which are derived from 'VHD' source. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="imageDefinitionName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Delete a test base image definition resource. |
