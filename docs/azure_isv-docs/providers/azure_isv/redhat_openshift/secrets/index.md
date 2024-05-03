---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - redhat_openshift
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redhat_openshift.secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | SecretProperties represents the properties of a Secret |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a Secret. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of each Secret. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a Secret. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | The operation returns nothing. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of each Secret. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a Secret. |
