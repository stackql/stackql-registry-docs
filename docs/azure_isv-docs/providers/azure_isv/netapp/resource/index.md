---
title: resource
hide_title: false
hide_table_of_contents: false
keywords:
  - resource
  - netapp
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
<tr><td><b>Name</b></td><td><code>resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.resource" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="check_file_path_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__subnetId" /> | Check if a file path is available. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__resourceGroup, data__type" /> | Check if a resource name is available. |
| <CopyableCode code="check_quota_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__resourceGroup, data__type" /> | Check if a quota is available. |
