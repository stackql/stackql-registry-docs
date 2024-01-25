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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_migration.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `etag` | `string` | HTTP strong entity tag value. Ignored if submitted |
| `kind` | `string` | The resource kind. Only 'vm' (the default) is supported. |
| `location` | `string` |  |
| `properties` | `object` | Properties of the Azure Database Migration Service (classic) instance |
| `sku` | `object` | An Azure SKU instance |
| `systemData` | `object` |  |
| `tags` | `object` |  |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The GET method retrieves information about a service instance. |
| `list` | `SELECT` | `api-version, subscriptionId` | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a subscription. |
| `list_by_resource_group` | `SELECT` | `api-version, groupName, subscriptionId` | The Services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a resource group. |
| `create_or_update` | `INSERT` |  | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, "vm", which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property. |
| `delete` | `DELETE` |  | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The DELETE method deletes a service. Any running tasks will be canceled. |
| `_list` | `EXEC` | `api-version, subscriptionId` | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a subscription. |
| `_list_by_resource_group` | `EXEC` | `api-version, groupName, subscriptionId` | The Services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a resource group. |
| `check_children_name_availability` | `EXEC` | `api-version, groupName, serviceName, subscriptionId` | This method checks whether a proposed nested resource name is valid and available. |
| `check_name_availability` | `EXEC` | `api-version, location, subscriptionId` | This method checks whether a proposed top-level resource name is valid and available. |
| `check_status` | `EXEC` | `api-version, groupName, serviceName, subscriptionId` | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action performs a health check and returns the status of the service and virtual machine size. |
| `start` | `EXEC` | `api-version, groupName, serviceName, subscriptionId` | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action starts the service and the service can be used for data migration. |
| `stop` | `EXEC` | `api-version, groupName, serviceName, subscriptionId` | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action stops the service and the service cannot be used for data migration. The service owner won't be billed when the service is stopped. |
| `update` | `EXEC` |  | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PATCH method updates an existing service. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). |
