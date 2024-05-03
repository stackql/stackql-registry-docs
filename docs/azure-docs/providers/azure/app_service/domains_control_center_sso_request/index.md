---
title: domains_control_center_sso_request
hide_title: false
hide_table_of_contents: false
keywords:
  - domains_control_center_sso_request
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
<tr><td><b>Name</b></td><td><code>domains_control_center_sso_request</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.domains_control_center_sso_request" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="postParameterKey" /> | `string` | Post parameter key. |
| <CopyableCode code="postParameterValue" /> | `string` | Post parameter value. Client should use 'application/x-www-form-urlencoded' encoding for this value. |
| <CopyableCode code="url" /> | `string` | URL where the single sign-on request is to be made. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
