---
title: domain_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_topics
  - event_grid
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
<tr><td><b>Name</b></td><td><code>domain_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.domain_topics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the Domain Topic. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, domainTopicName, resourceGroupName, subscriptionId" /> | Get properties of a domain topic. |
| <CopyableCode code="list_by_domain" /> | `SELECT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | List all the topics in a domain. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, domainTopicName, resourceGroupName, subscriptionId" /> | Asynchronously creates or updates a new domain topic with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, domainTopicName, resourceGroupName, subscriptionId" /> | Delete existing domain topic. |
