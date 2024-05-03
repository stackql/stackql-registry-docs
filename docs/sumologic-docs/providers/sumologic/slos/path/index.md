---
title: path
hide_title: false
hide_table_of_contents: false
keywords:
  - path
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
<tr><td><b>Name</b></td><td><code>path</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.slos.path" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="path" /> | `string` | String representation of the path. |
| <CopyableCode code="pathItems" /> | `array` | Elements of the path. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getSlosFullPath" /> | `SELECT` | <CopyableCode code="id, region" /> | Get the full path of the slo or folder in the slos library. |
| <CopyableCode code="slosGetByPath" /> | `EXEC` | <CopyableCode code="path, region" /> | Read a slo or folder by its path in the slos library structure. |
