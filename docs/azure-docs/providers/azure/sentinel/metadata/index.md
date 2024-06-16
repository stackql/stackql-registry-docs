---
title: metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata
  - sentinel
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
<tr><td><b>Name</b></td><td><code>metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Metadata property bag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="metadataName, resourceGroupName, subscriptionId, workspaceName" /> | Get a Metadata. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List of all metadata |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="metadataName, resourceGroupName, subscriptionId, workspaceName" /> | Create a Metadata. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="metadataName, resourceGroupName, subscriptionId, workspaceName" /> | Delete a Metadata. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="metadataName, resourceGroupName, subscriptionId, workspaceName" /> | Update an existing Metadata. |
