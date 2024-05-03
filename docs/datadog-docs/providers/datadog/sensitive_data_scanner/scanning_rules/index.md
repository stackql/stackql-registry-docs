---
title: scanning_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - scanning_rules
  - sensitive_data_scanner
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
<tr><td><b>Name</b></td><td><code>scanning_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.sensitive_data_scanner.scanning_rules" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_scanning_rule" /> | `INSERT` | <CopyableCode code="data__data, data__meta, dd_site" /> | Create a scanning rule in a sensitive data scanner group, ordered last.<br />The posted rule MUST include a group relationship.<br />It MUST include either a standard_pattern relationship or a regex attribute, but not both.<br />If included_attributes is empty or missing, we will scan all attributes except<br />excluded_attributes. If both are missing, we will scan the whole event. |
| <CopyableCode code="delete_scanning_rule" /> | `DELETE` | <CopyableCode code="rule_id, data__meta, dd_site" /> | Delete a given rule. |
| <CopyableCode code="update_scanning_rule" /> | `EXEC` | <CopyableCode code="rule_id, data__data, data__meta, dd_site" /> | Update a scanning rule.<br />The request body MUST NOT include a standard_pattern relationship, as that relationship<br />is non-editable. Trying to edit the regex attribute of a rule with a standard_pattern<br />relationship will also result in an error. |
