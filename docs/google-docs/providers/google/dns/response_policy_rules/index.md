---
title: response_policy_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - response_policy_rules
  - dns
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_policy_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dns.response_policy_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="behavior" /> | `string` | Answer this query with a behavior rather than DNS data. |
| <CopyableCode code="dnsName" /> | `string` | The DNS name (wildcard or exact) to apply this rule to. Must be unique within the Response Policy Rule. |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="localData" /> | `object` |  |
| <CopyableCode code="ruleName" /> | `string` | An identifier for this rule. Must be unique with the ResponsePolicy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, responsePolicy, responsePolicyRule" /> | Fetches the representation of an existing Response Policy Rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, responsePolicy" /> | Enumerates all Response Policy Rules associated with a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="project, responsePolicy" /> | Creates a new Response Policy Rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, responsePolicy, responsePolicyRule" /> | Deletes a previously created Response Policy Rule. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="project, responsePolicy" /> | Enumerates all Response Policy Rules associated with a project. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="project, responsePolicy, responsePolicyRule" /> | Applies a partial update to an existing Response Policy Rule. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="project, responsePolicy, responsePolicyRule" /> | Updates an existing Response Policy Rule. |
