---
title: shared_gallery_image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_gallery_image_versions
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shared_gallery_image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.shared_gallery_image_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identifier" /> | `object` | The identifier information of shared gallery. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryImageVersionName, galleryUniqueName, location, subscriptionId" /> | Get a shared gallery image version by subscription id or tenant id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryUniqueName, location, subscriptionId" /> | List shared gallery image versions by subscription id or tenant id. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="galleryImageName, galleryUniqueName, location, subscriptionId" /> | List shared gallery image versions by subscription id or tenant id. |
