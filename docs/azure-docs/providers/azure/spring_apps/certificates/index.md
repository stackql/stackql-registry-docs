---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.certificates" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateName, resourceGroupName, serviceName, subscriptionId" /> | Get the certificate resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | List all the certificates of one user. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateName, resourceGroupName, serviceName, subscriptionId" /> | Create or update certificate resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateName, resourceGroupName, serviceName, subscriptionId" /> | Delete the certificate resource. |
