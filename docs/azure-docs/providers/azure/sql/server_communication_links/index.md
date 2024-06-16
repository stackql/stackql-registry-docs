---
title: server_communication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - server_communication_links
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
<tr><td><b>Name</b></td><td><code>server_communication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_communication_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Communication link kind.  This property is used for Azure Portal metadata. |
| <CopyableCode code="location" /> | `string` | Communication link location. |
| <CopyableCode code="properties" /> | `object` | The properties of a server communication link. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="communicationLinkName, resourceGroupName, serverName, subscriptionId" /> | Returns a server communication link. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server communication links. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="communicationLinkName, resourceGroupName, serverName, subscriptionId" /> | Creates a server communication link. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="communicationLinkName, resourceGroupName, serverName, subscriptionId" /> | Deletes a server communication link. |
