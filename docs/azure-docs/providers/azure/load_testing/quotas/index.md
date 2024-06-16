---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - load_testing
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
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.load_testing.quotas" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, quotaBucketName, subscriptionId" /> | Get the available quota for a quota bucket per region per subscription. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List quotas for a given subscription Id. |
| <CopyableCode code="check_availability" /> | `EXEC` | <CopyableCode code="location, quotaBucketName, subscriptionId" /> | Check Quota Availability on quota bucket per region per subscription. |
