---
title: static_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites
  - app_service
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
<tr><td><b>Name</b></td><td><code>static_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.static_sites" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="identity" /> | `object` | Managed service identity. |
| <CopyableCode code="properties" /> | `object` | A static site. |
| <CopyableCode code="sku" /> | `object` | Description of a SKU for a scalable resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all Static Sites for a subscription. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for Get all Static Sites for a subscription. |
| <CopyableCode code="approve_or_reject_private_endpoint_connection" /> | `EXEC` | <CopyableCode code="name, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Description for Approves or rejects a private endpoint connection |
| <CopyableCode code="detach_static_site" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Detaches a static site. |
| <CopyableCode code="detach_user_provided_function_app_from_static_site" /> | `EXEC` | <CopyableCode code="functionAppName, name, resourceGroupName, subscriptionId" /> | Description for Detach the user provided function app from the static site |
| <CopyableCode code="detach_user_provided_function_app_from_static_site_build" /> | `EXEC` | <CopyableCode code="environmentName, functionAppName, name, resourceGroupName, subscriptionId" /> | Description for Detach the user provided function app from the static site build |
| <CopyableCode code="link_backend" /> | `EXEC` | <CopyableCode code="linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="link_backend_to_build" /> | `EXEC` | <CopyableCode code="environmentName, linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="preview_workflow" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Description for Generates a preview workflow file for the static site |
| <CopyableCode code="register_user_provided_function_app_with_static_site" /> | `EXEC` | <CopyableCode code="functionAppName, name, resourceGroupName, subscriptionId" /> | Description for Register a user provided function app with a static site |
| <CopyableCode code="register_user_provided_function_app_with_static_site_build" /> | `EXEC` | <CopyableCode code="environmentName, functionAppName, name, resourceGroupName, subscriptionId" /> | Description for Register a user provided function app with a static site build |
| <CopyableCode code="reset_static_site_api_key" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Resets the api key for an existing static site. |
| <CopyableCode code="unlink_backend" /> | `EXEC` | <CopyableCode code="linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="unlink_backend_from_build" /> | `EXEC` | <CopyableCode code="environmentName, linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="validate_backend" /> | `EXEC` | <CopyableCode code="linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="validate_backend_for_build" /> | `EXEC` | <CopyableCode code="environmentName, linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="validate_custom_domain_can_be_added_to_static_site" /> | `EXEC` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Validates a particular custom domain can be added to a static site. |
