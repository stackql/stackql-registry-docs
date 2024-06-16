---
title: domains_ownership_identifier
hide_title: false
hide_table_of_contents: false
keywords:
  - domains_ownership_identifier
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
<tr><td><b>Name</b></td><td><code>domains_ownership_identifier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.domains_ownership_identifier" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | DomainOwnershipIdentifier resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Get ownership identifier for domain |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Delete ownership identifier for domain |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier |
