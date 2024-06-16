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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtime_object_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.integration_runtime_object_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Metadata id. |
| <CopyableCode code="name" /> | `string` | Metadata name. |
| <CopyableCode code="description" /> | `string` | Metadata description. |
| <CopyableCode code="type" /> | `string` | The type of SSIS object metadata. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Get a SSIS integration runtime object metadata by specified path. The return is pageable metadata list. |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Refresh a SSIS integration runtime object metadata. |
