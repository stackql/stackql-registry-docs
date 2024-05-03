---
title: quota
hide_title: false
hide_table_of_contents: false
keywords:
  - quota
  - quota
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
<tr><td><b>Name</b></td><td><code>quota</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.quota" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | Quota properties for the specified resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceName, scope" /> | Get the quota limit of a resource. The response can be used to determine the remaining quota to calculate a new quota limit that can be submitted with a PUT request. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get a list of current quota limits of all resources for the specified scope. The response from this GET operation can be leveraged to submit requests to update a quota. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceName, scope" /> | Create or update the quota limit for the specified resource with the requested value. To update the quota, follow these steps:<br />1. Use the GET operation for quotas and usages to determine how much quota remains for the specific resource and to calculate the new quota limit. These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670).<br />2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed status of the request. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="scope" /> | Get a list of current quota limits of all resources for the specified scope. The response from this GET operation can be leveraged to submit requests to update a quota. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceName, scope" /> | Update the quota limit for a specific resource to the specified value:<br />1. Use the Usages-GET and Quota-GET operations to determine the remaining quota for the specific resource and to calculate the new quota limit. These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670).<br />2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed status of the request. |
