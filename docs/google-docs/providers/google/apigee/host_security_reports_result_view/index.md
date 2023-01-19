---
title: host_security_reports_result_view
hide_title: false
hide_table_of_contents: false
keywords:
  - host_security_reports_result_view
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_security_reports_result_view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.host_security_reports_result_view</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | State of retrieving ResultView. |
| `code` | `integer` | Error code when there is a failure. |
| `error` | `string` | Error message when there is a failure. |
| `metadata` | `object` | Metadata for the security report. |
| `rows` | `array` | Rows of security report result. Each row is a JSON object. Example: &#123;sum(message_count): 1, developer_app: "(not set)",…&#125; |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_hostSecurityReports_getResultView` | `SELECT` | `hostSecurityReportsId, organizationsId` |
