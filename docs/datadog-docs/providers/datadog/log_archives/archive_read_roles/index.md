---
title: archive_read_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - archive_read_roles
  - log_archives
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
<tr><td><b>Name</b></td><td><code>archive_read_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.log_archives.archive_read_roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier of the role. |
| <CopyableCode code="attributes" /> | `object` | Attributes of the role. |
| <CopyableCode code="relationships" /> | `object` | Relationships of the role object returned by the API. |
| <CopyableCode code="type" /> | `string` | Roles type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_archive_read_roles" /> | `SELECT` | <CopyableCode code="archive_id, dd_site" /> |
| <CopyableCode code="_list_archive_read_roles" /> | `EXEC` | <CopyableCode code="archive_id, dd_site" /> |
