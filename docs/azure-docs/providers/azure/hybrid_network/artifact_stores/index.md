---
title: artifact_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_stores
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>artifact_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.artifact_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Artifact store properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about the specified artifact store. |
| <CopyableCode code="list_by_publisher" /> | `SELECT` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Gets information of the ArtifactStores under publisher. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a artifact store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Deletes the specified artifact store. |
| <CopyableCode code="_list_by_publisher" /> | `EXEC` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Gets information of the ArtifactStores under publisher. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="artifactStoreName, publisherName, resourceGroupName, subscriptionId" /> | Update artifact store resource. |
