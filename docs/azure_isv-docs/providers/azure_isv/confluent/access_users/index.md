---
title: access_users
hide_title: false
hide_table_of_contents: false
keywords:
  - access_users
  - confluent
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
<tr><td><b>Name</b></td><td><code>access_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.access_users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `array` | Data of the users list |
| <CopyableCode code="kind" /> | `string` | Type of response |
| <CopyableCode code="metadata" /> | `object` | Metadata of the list |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="invite_user" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> |
