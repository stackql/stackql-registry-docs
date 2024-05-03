---
title: vw_users
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_users
  - users
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
<tr><td><b>Name</b></td><td><code>vw_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.users.vw_users" /></td></tr>
</tbody></table>

## Fields
> This resource is a view. For the view definition, please refer to the provider spec in the [stackql-provider-registry](https://github.com/stackql/stackql-provider-registry/blob/dev/providers/src/datadog/v00.00.00000/services/users.yaml), located under `components -> x-stackQL-resources -> vw_users`.

| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `text` |
| <CopyableCode code="name" /> ||
| <CopyableCode code="allowed_login_methods" /> ||
| <CopyableCode code="created_at" /> ||
| <CopyableCode code="disabled" /> ||
| <CopyableCode code="email" /> ||
| <CopyableCode code="handle" /> ||
| <CopyableCode code="icon" /> ||
| <CopyableCode code="mfa_enabled" /> ||
| <CopyableCode code="modified_at" /> ||
| <CopyableCode code="service_account" /> ||
| <CopyableCode code="status" /> ||
| <CopyableCode code="title" /> ||
| <CopyableCode code="verified" /> ||
## Methods
No methods available for the resource
