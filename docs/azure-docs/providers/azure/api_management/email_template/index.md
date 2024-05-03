---
title: email_template
hide_title: false
hide_table_of_contents: false
keywords:
  - email_template
  - api_management
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
<tr><td><b>Name</b></td><td><code>email_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.email_template" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, templateName" /> | Gets the details of the email template specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets all email templates |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, templateName" /> | Updates an Email Template. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, subscriptionId, templateName" /> | Reset the Email Template to default template provided by the API Management service instance. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets all email templates |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, resourceGroupName, serviceName, subscriptionId, templateName" /> | Updates API Management email template |
