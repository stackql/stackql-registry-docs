---
title: images_upload_url_for_entity_type
hide_title: false
hide_table_of_contents: false
keywords:
  - images_upload_url_for_entity_type
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images_upload_url_for_entity_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.images_upload_url_for_entity_type" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentUrl" /> | `string` | Content URL for the image blob. |
| <CopyableCode code="imageExists" /> | `boolean` | Whether image exists already. |
| <CopyableCode code="relativePath" /> | `string` | Relative path of the image. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> |
