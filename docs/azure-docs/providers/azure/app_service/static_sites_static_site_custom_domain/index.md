---
title: static_sites_static_site_custom_domain
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites_static_site_custom_domain
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
<tr><td><b>Name</b></td><td><code>static_sites_static_site_custom_domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.static_sites_static_site_custom_domain" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | StaticSiteCustomDomainOverviewARMResource resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Gets an existing custom domain for a particular static site. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Creates a new static site custom domain in an existing resource group and static site. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Deletes a custom domain. |
