---
title: slos
hide_title: false
hide_table_of_contents: false
keywords:
  - slos
  - slos
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.slos.slos" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="slosCreate" /> | `EXEC` | <CopyableCode code="parentId, data__name, data__type, region" /> | Create a slo or folder in the slos library. |
| <CopyableCode code="slosDeleteById" /> | `EXEC` | <CopyableCode code="id, region" /> | Delete a slo or folder from the slos library. |
| <CopyableCode code="slosDeleteByIds" /> | `EXEC` | <CopyableCode code="ids, region" /> | Bulk delete a slo or folder by the given identifiers in the slos library. |
| <CopyableCode code="slosReadById" /> | `EXEC` | <CopyableCode code="id, region" /> | Get a slo or folder from the slos library. |
| <CopyableCode code="slosReadByIds" /> | `EXEC` | <CopyableCode code="ids, region" /> | Bulk read a slo or folder by the given identifiers from the slos library. |
| <CopyableCode code="slosUpdateById" /> | `EXEC` | <CopyableCode code="id, data__name, data__type, data__version, region" /> | Update a slo or folder in the slos library. |
