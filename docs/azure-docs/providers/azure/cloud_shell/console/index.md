---
title: console
hide_title: false
hide_table_of_contents: false
keywords:
  - console
  - cloud_shell
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
<tr><td><b>Name</b></td><td><code>console</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cloud_shell.console" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consoleName" /> | Gets the console for the user. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consoleName" /> | Deletes the console |
| <CopyableCode code="keep_alive" /> | `EXEC` | <CopyableCode code="consoleName" /> | Keep console alive |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="consoleName, data__properties" /> | Puts a request for a console |
