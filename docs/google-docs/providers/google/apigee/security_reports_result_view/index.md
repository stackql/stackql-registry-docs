---
title: security_reports_result_view
hide_title: false
hide_table_of_contents: false
keywords:
  - security_reports_result_view
  - apigee
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
<tr><td><b>Name</b></td><td><code>security_reports_result_view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.security_reports_result_view" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="code" /> | `integer` | Error code when there is a failure. |
| <CopyableCode code="error" /> | `string` | Error message when there is a failure. |
| <CopyableCode code="metadata" /> | `object` | Metadata for the security report. |
| <CopyableCode code="rows" /> | `array` | Rows of security report result. Each row is a JSON object. Example: &#123;sum(message_count): 1, developer_app: "(not set)",…&#125; |
| <CopyableCode code="state" /> | `string` | State of retrieving ResultView. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="organizations_environments_security_reports_get_result_view" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, securityReportsId" /> |
