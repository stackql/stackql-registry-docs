---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
  - roles
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
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.roles.permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the permission. |
| <CopyableCode code="attributes" /> | `object` | Attributes of a permission. |
| <CopyableCode code="type" /> | `string` | Permissions resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_permissions" /> | `SELECT` | <CopyableCode code="dd_site" /> |
| <CopyableCode code="_list_permissions" /> | `EXEC` | <CopyableCode code="dd_site" /> |
