---
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
  - astro
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.astro.organizations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to Data Organization resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Get a OrganizationResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List OrganizationResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List OrganizationResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Create a OrganizationResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Delete a OrganizationResource |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List OrganizationResource resources by resource group |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List OrganizationResource resources by subscription ID |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Update a OrganizationResource |
