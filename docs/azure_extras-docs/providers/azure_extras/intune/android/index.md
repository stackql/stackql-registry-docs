---
title: android
hide_title: false
hide_table_of_contents: false
keywords:
  - android
  - intune
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>android</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.intune.android" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_app_for_mam_policy" /> | `EXEC` | <CopyableCode code="appName, hostName, policyName" /> | Add app to an AndroidMAMPolicy. |
| <CopyableCode code="add_group_for_mam_policy" /> | `EXEC` | <CopyableCode code="groupId, hostName, policyName" /> | Add group to an AndroidMAMPolicy. |
| <CopyableCode code="patch_mam_policy" /> | `EXEC` | <CopyableCode code="hostName, policyName" /> | Patch AndroidMAMPolicy. |
