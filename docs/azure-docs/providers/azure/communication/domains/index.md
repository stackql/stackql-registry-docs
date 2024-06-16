---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - communication
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | A class that describes the properties of a Domains resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | Get the Domains resource and its properties. |
| <CopyableCode code="list_by_email_service_resource" /> | `SELECT` | <CopyableCode code="emailServiceName, resourceGroupName, subscriptionId" /> | Handles requests to list all Domains resources under the parent EmailServices resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | Add a new Domains resource under the parent EmailService resource or update an existing Domains resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | Operation to delete a Domains resource. |
| <CopyableCode code="cancel_verification" /> | `EXEC` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, data__verificationType" /> | Cancel verification of DNS record. |
| <CopyableCode code="initiate_verification" /> | `EXEC` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, data__verificationType" /> | Initiate verification of DNS record. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | Operation to update an existing Domains resource. |
