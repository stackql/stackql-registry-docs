---
title: engines
hide_title: false
hide_table_of_contents: false
keywords:
  - engines
  - databases
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>engines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.databases.engines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Managed Database engine ID in engine/version format. |
| <CopyableCode code="engine" /> | `string` | The Managed Database engine type. |
| <CopyableCode code="version" /> | `string` | The Managed Database engine version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getDatabasesEngine" /> | `SELECT` | <CopyableCode code="engineId" /> | Display information for a single Managed Database engine type and version.<br /> |
| <CopyableCode code="getDatabasesEngines" /> | `SELECT` |  | Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases.<br /> |
| <CopyableCode code="_getDatabasesEngine" /> | `EXEC` | <CopyableCode code="engineId" /> | Display information for a single Managed Database engine type and version.<br /> |
| <CopyableCode code="_getDatabasesEngines" /> | `EXEC` |  | Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases.<br /> |
