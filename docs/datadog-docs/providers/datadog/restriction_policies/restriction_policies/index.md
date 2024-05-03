---
title: restriction_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - restriction_policies
  - restriction_policies
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
<tr><td><b>Name</b></td><td><code>restriction_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.restriction_policies.restriction_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, always equivalent to the value specified in the `resource_id` path parameter. |
| <CopyableCode code="attributes" /> | `object` | Restriction policy attributes. |
| <CopyableCode code="type" /> | `string` | Restriction policy type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_restriction_policy" /> | `SELECT` | <CopyableCode code="resource_id, dd_site" /> | Retrieves the restriction policy associated with a specified resource. |
| <CopyableCode code="delete_restriction_policy" /> | `DELETE` | <CopyableCode code="resource_id, dd_site" /> | Deletes the restriction policy associated with a specified resource. |
| <CopyableCode code="_get_restriction_policy" /> | `EXEC` | <CopyableCode code="resource_id, dd_site" /> | Retrieves the restriction policy associated with a specified resource. |
| <CopyableCode code="update_restriction_policy" /> | `EXEC` | <CopyableCode code="resource_id, data__data, dd_site" /> | Updates the restriction policy associated with a resource.<br /><br />#### Supported resources<br />Restriction policies can be applied to the following resources:<br />- Connections: `connection`<br />- Dashboards: `dashboard`<br />- Notebooks: `notebook`<br />- Security Rules: `security-rule`<br />- Service Level Objectives: `slo`<br /><br />#### Supported relations for resources<br />Resource Type            \| Supported Relations<br />-------------------------\|--------------------------<br />Connections              \| `viewer`, `editor`, `resolver`<br />Dashboards               \| `viewer`, `editor`<br />Notebooks                \| `viewer`, `editor`<br />Security Rules           \| `viewer`, `editor`<br />Service Level Objectives \| `viewer`, `editor` |
