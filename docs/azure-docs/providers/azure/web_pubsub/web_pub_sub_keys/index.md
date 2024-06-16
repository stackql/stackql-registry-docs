---
title: web_pub_sub_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub_keys
  - web_pubsub
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
<tr><td><b>Name</b></td><td><code>web_pub_sub_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.web_pub_sub_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primaryConnectionString" /> | `string` | Connection string constructed via the primaryKey |
| <CopyableCode code="primaryKey" /> | `string` | The primary access key. |
| <CopyableCode code="secondaryConnectionString" /> | `string` | Connection string constructed via the secondaryKey |
| <CopyableCode code="secondaryKey" /> | `string` | The secondary access key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |
