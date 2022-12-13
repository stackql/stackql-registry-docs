---
title: integration_runtime_object_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_object_metadata
  - data_factory
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
<tr><td><b>Name</b></td><td><code>integration_runtime_object_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.integration_runtime_object_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `value` | `array` | List of SSIS object metadata. |
| `nextLink` | `string` | The link to the next page of results, if any remaining results exist. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationRuntimeObjectMetadata_Get` | `SELECT` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Get a SSIS integration runtime object metadata by specified path. The return is pageable metadata list. |
| `IntegrationRuntimeObjectMetadata_Refresh` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Refresh a SSIS integration runtime object metadata. |
