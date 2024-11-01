---
title: statement_exceptions
hide_title: false
hide_table_of_contents: false
keywords:
  - statement_exceptions
  - sql
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>statement_exceptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.sql.statement_exceptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the SQL statement exception. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="message" /> | `string` | Error message of the statement exception. |
| <CopyableCode code="timestamp" /> | `string` | The date and time at which the exception occurred. It is represented in RFC3339 format and is in UTC. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_sqlv1statement_exceptions" /> | `SELECT` | <CopyableCode code="environment_id, organization_id, statement_name" /> |
