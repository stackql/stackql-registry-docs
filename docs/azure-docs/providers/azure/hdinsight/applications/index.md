---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - hdinsight
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag for the application |
| <CopyableCode code="properties" /> | `object` | The HDInsight cluster application GET response. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The tags for the application. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Gets properties of the specified application. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Lists all of the applications for the HDInsight cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Creates applications for the HDInsight cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, clusterName, resourceGroupName, subscriptionId" /> | Deletes the specified application on the HDInsight cluster. |
