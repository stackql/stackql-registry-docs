---
title: user_memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - user_memberships
  - teams
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
<tr><td><b>Name</b></td><td><code>user_memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.teams.user_memberships" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of a user's relationship with a team |
| <CopyableCode code="attributes" /> | `object` | Team membership attributes |
| <CopyableCode code="relationships" /> | `object` | Relationship between membership and a user |
| <CopyableCode code="type" /> | `string` | Team membership type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_user_memberships" /> | `SELECT` | <CopyableCode code="user_uuid, dd_site" /> |
| <CopyableCode code="_get_user_memberships" /> | `EXEC` | <CopyableCode code="user_uuid, dd_site" /> |
