---
title: custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_domains
  - cdn
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
<tr><td><b>Name</b></td><td><code>custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.custom_domains" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customDomainName, endpointName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing custom domain within an endpoint. |
| <CopyableCode code="list_by_endpoint" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing custom domains within an endpoint. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customDomainName, endpointName, profileName, resourceGroupName, subscriptionId" /> | Creates a new custom domain within an endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customDomainName, endpointName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing custom domain within an endpoint. |
| <CopyableCode code="disable_custom_https" /> | `EXEC` | <CopyableCode code="customDomainName, endpointName, profileName, resourceGroupName, subscriptionId" /> | Disable https delivery of the custom domain. |
| <CopyableCode code="enable_custom_https" /> | `EXEC` | <CopyableCode code="customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, data__certificateSource, data__protocolType" /> | Enable https delivery of the custom domain. |
