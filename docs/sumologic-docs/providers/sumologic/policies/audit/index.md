---
title: audit
hide_title: false
hide_table_of_contents: false
keywords:
  - audit
  - policies
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
<tr><td><b>Name</b></td><td><code>audit</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.policies.audit" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getAuditPolicy" /> | `SELECT` | <CopyableCode code="region" /> | Get the Audit policy. This policy specifies whether audit records for your account are enabled. You can access details about reported account events in the Sumo Logic Audit Index. [Learn More](https://help.sumologic.com/Manage/Security/Audit-Index) |
| <CopyableCode code="setAuditPolicy" /> | `EXEC` | <CopyableCode code="data__enabled, region" /> | Set the Audit policy. This policy specifies whether audit records for your account are enabled. You can access details about reported account events in the Sumo Logic Audit Index. [Learn More](https://help.sumologic.com/Manage/Security/Audit-Index) |
