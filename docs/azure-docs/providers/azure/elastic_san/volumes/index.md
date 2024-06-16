---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - elastic_san
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elastic_san.volumes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName" /> | Get an Volume. |
| <CopyableCode code="list_by_volume_group" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName" /> | List Volumes in a VolumeGroup. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName, data__properties" /> | Create a Volume. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName" /> | Delete an Volume. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName" /> | Update an Volume. |
