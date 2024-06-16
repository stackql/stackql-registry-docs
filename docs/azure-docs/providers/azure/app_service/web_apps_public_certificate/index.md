---
title: web_apps_public_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_public_certificate
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
<tr><td><b>Name</b></td><td><code>web_apps_public_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.web_apps_public_certificate" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | PublicCertificate resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, publicCertificateName, resourceGroupName, subscriptionId" /> | Description for Get the named public certificate for an app (or deployment slot, if specified). |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, publicCertificateName, resourceGroupName, subscriptionId" /> | Description for Creates a hostname binding for an app. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, publicCertificateName, resourceGroupName, subscriptionId" /> | Description for Deletes a hostname binding for an app. |
