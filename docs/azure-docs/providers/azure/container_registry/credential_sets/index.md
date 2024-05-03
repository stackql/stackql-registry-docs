---
title: credential_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - credential_sets
  - container_registry
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
<tr><td><b>Name</b></td><td><code>credential_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.credential_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of a credential set resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="credentialSetName, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified credential set resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all credential set resources for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="credentialSetName, registryName, resourceGroupName, subscriptionId" /> | Creates a credential set for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="credentialSetName, registryName, resourceGroupName, subscriptionId" /> | Deletes a credential set from a container registry. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all credential set resources for the specified container registry. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="credentialSetName, registryName, resourceGroupName, subscriptionId" /> | Updates a credential set for a container registry with the specified parameters. |
