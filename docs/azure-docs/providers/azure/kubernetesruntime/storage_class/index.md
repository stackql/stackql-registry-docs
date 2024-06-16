---
title: storage_class
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_class
  - kubernetesruntime
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
<tr><td><b>Name</b></td><td><code>storage_class</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetesruntime.storage_class" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri, storageClassName" /> | Get a StorageClassResource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List StorageClassResource resources by parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceUri, storageClassName" /> | Create a StorageClassResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri, storageClassName" /> | Delete a StorageClassResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceUri, storageClassName" /> | Update a StorageClassResource |
