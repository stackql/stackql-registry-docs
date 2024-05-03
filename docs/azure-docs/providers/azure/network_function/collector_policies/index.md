---
title: collector_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - collector_policies
  - network_function
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
<tr><td><b>Name</b></td><td><code>collector_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network_function.collector_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Collection policy properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureTrafficCollectorName, collectorPolicyName, resourceGroupName, subscriptionId" /> | Gets the collector policy in a specified Traffic Collector |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="azureTrafficCollectorName, resourceGroupName, subscriptionId" /> | Return list of Collector policies in a Azure Traffic Collector |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="azureTrafficCollectorName, collectorPolicyName, resourceGroupName, subscriptionId" /> | Creates or updates a Collector Policy resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureTrafficCollectorName, collectorPolicyName, resourceGroupName, subscriptionId" /> | Deletes a specified Collector Policy resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="azureTrafficCollectorName, resourceGroupName, subscriptionId" /> | Return list of Collector policies in a Azure Traffic Collector |
