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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.custom_images" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customImageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a test base custom image. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the custom images under a test base account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customImageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Creates a test base custom image. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customImageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a test base custom image. |
| <CopyableCode code="_list_by_test_base_account" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the custom images under a test base account. |
| <CopyableCode code="check_image_name_availability" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName, data__definitionName, data__versionName" /> | Checks that the test vase custom image generated from VHD resource has valid and unique definition and version, return architecture and OS state of potential existing image definition. |
