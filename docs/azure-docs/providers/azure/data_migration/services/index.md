---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - data_migration
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | HTTP strong entity tag value. Ignored if submitted |
| <CopyableCode code="kind" /> | `string` | The resource kind. Only 'vm' (the default) is supported. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the Azure Database Migration Service (classic) instance |
| <CopyableCode code="sku" /> | `object` | An Azure SKU instance |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The GET method retrieves information about a service instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, groupName, subscriptionId" /> | The Services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, "vm", which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property. |
| <CopyableCode code="delete" /> | `DELETE` |  | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The DELETE method deletes a service. Any running tasks will be canceled. |
| <CopyableCode code="check_children_name_availability" /> | `EXEC` | <CopyableCode code="api-version, groupName, serviceName, subscriptionId" /> | This method checks whether a proposed nested resource name is valid and available. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="api-version, location, subscriptionId" /> | This method checks whether a proposed top-level resource name is valid and available. |
| <CopyableCode code="check_status" /> | `EXEC` | <CopyableCode code="api-version, groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action performs a health check and returns the status of the service and virtual machine size. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="api-version, groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action starts the service and the service can be used for data migration. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="api-version, groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action stops the service and the service cannot be used for data migration. The service owner won't be billed when the service is stopped. |
| <CopyableCode code="update" /> | `EXEC` |  | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PATCH method updates an existing service. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). |
