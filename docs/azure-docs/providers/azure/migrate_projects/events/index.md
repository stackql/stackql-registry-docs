---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - migrate_projects
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate_projects.events" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="_enumerate_events" /> | `EXEC` | <CopyableCode code="api-version, migrateProjectName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="enumerate_events" /> | `EXEC` | <CopyableCode code="api-version, migrateProjectName, resourceGroupName, subscriptionId" /> |
