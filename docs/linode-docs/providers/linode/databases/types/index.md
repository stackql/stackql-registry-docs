---
title: types
hide_title: false
hide_table_of_contents: false
keywords:
  - types
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
<tr><td><b>Name</b></td><td><code>types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.databases.types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID representing the Managed Database node plan type. |
| <CopyableCode code="class" /> | `string` | The compute class category. |
| <CopyableCode code="deprecated" /> | `boolean` | Whether this Database plan type has been deprecated and is no longer available. |
| <CopyableCode code="disk" /> | `integer` | The amount of disk space set aside for Databases of this plan type. The value is represented in megabytes. |
| <CopyableCode code="engines" /> | `object` |  |
| <CopyableCode code="label" /> | `string` | A human-readable string that describes each plan type. For display purposes only. |
| <CopyableCode code="memory" /> | `integer` | The amount of RAM allocated to Database created of this plan type. The value is represented in megabytes. |
| <CopyableCode code="vcpus" /> | `integer` | The integer of number CPUs allocated to databases of this plan type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getDatabasesType" /> | `SELECT` | <CopyableCode code="typeId" /> | Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance.<br /> |
| <CopyableCode code="getDatabasesTypes" /> | `SELECT` |  | Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.<br /><br />Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type.<br /> |
| <CopyableCode code="_getDatabasesType" /> | `EXEC` | <CopyableCode code="typeId" /> | Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance.<br /> |
| <CopyableCode code="_getDatabasesTypes" /> | `EXEC` |  | Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.<br /><br />Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type.<br /> |
