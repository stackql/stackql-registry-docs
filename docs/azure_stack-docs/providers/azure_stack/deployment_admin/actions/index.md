---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - deployment_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.deployment_admin.actions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="product_bootstrap_action" /> | `EXEC` | <CopyableCode code="productId, subscriptionId" /> | Invokes bootstrap action on the product deployment |
| <CopyableCode code="product_deploy_action" /> | `EXEC` | <CopyableCode code="productId, subscriptionId" /> | Invokes deploy action on the product |
| <CopyableCode code="product_execute_runner_action" /> | `EXEC` | <CopyableCode code="productId, subscriptionId" /> | Invokes execute runner action on the product deployment |
| <CopyableCode code="product_remove_action" /> | `EXEC` | <CopyableCode code="productId, subscriptionId" /> | Invokes remove action on the product deployment |
| <CopyableCode code="product_rotate_secrets_action" /> | `EXEC` | <CopyableCode code="productId, subscriptionId" /> | Invokes rotate secrets action on the product deployment |
