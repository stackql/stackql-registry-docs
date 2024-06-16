---
title: buildpack_binding
hide_title: false
hide_table_of_contents: false
keywords:
  - buildpack_binding
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>buildpack_binding</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.buildpack_binding" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId" /> | Get a buildpack binding by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all buildpack bindings in a builder. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId" /> | Create or update a buildpack binding. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete a Buildpack Binding |
