---
title: subscription_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_usages
  - sql
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
<tr><td><b>Name</b></td><td><code>subscription_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.subscription_usages" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId, usageName" /> | Gets a subscription usage metric. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Gets all subscription usage metrics in a given location. |
| <CopyableCode code="_list_by_location" /> | `EXEC` | <CopyableCode code="locationName, subscriptionId" /> | Gets all subscription usage metrics in a given location. |
