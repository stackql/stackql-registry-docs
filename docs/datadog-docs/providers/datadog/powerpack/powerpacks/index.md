---
title: powerpacks
hide_title: false
hide_table_of_contents: false
keywords:
  - powerpacks
  - powerpack
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>powerpacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.powerpack.powerpacks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the powerpack. |
| <CopyableCode code="attributes" /> | `object` | Powerpack attribute object. |
| <CopyableCode code="relationships" /> | `object` | Powerpack relationship object. |
| <CopyableCode code="type" /> | `string` | Type of widget, must be powerpack. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_powerpack" /> | `SELECT` | <CopyableCode code="powerpack_id, dd_site" /> | Get a powerpack. |
| <CopyableCode code="list_powerpacks" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get a list of all powerpacks. |
| <CopyableCode code="create_powerpack" /> | `INSERT` | <CopyableCode code="dd_site" /> | Create a powerpack. |
| <CopyableCode code="delete_powerpack" /> | `DELETE` | <CopyableCode code="powerpack_id, dd_site" /> | Delete a powerpack. |
| <CopyableCode code="_get_powerpack" /> | `EXEC` | <CopyableCode code="powerpack_id, dd_site" /> | Get a powerpack. |
| <CopyableCode code="_list_powerpacks" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get a list of all powerpacks. |
| <CopyableCode code="update_powerpack" /> | `EXEC` | <CopyableCode code="powerpack_id, dd_site" /> | Update a powerpack. |
