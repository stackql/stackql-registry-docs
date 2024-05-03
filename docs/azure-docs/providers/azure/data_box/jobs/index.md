---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - data_box
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="identity" /> | `object` | Msi identity details of the resource |
| <CopyableCode code="location" /> | `string` | The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. |
| <CopyableCode code="properties" /> | `object` | Job Properties |
| <CopyableCode code="sku" /> | `object` | The Sku. |
| <CopyableCode code="systemData" /> | `object` | Provides details about resource creation and update time |
| <CopyableCode code="tags" /> | `object` | The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). |
| <CopyableCode code="type" /> | `string` | Type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Gets information about the specified job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the jobs available under the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the jobs available under the given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, data__properties" /> | Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Deletes a job. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the jobs available under the subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the jobs available under the given resource group. |
| <CopyableCode code="book_shipment_pick_up" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, data__endTime, data__shipmentLocation, data__startTime" /> | Book shipment pick up. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, data__reason" /> | CancelJob. |
| <CopyableCode code="jobs" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Request to mitigate for a given job |
| <CopyableCode code="mark_devices_shipped" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, data__deliverToDcPackageDetails" /> | Request to mark devices for a given job as shipped |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing job. |
