---
title: credential_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - credential_reports
  - iam_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credential_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam_api.credential_reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `Content` | `string` | Contains the credential report. The report is Base64-encoded. |
| `GeneratedTime` | `string` |  The date and time when the credential report was created, in &lt;a href="http://www.iso.org/iso/iso8601"&gt;ISO 8601 date-time format&lt;/a&gt;. |
| `ReportFormat` | `string` | The format (MIME type) of the credential report. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `credential_reports_Get` | `SELECT` | `region` |  Retrieves a credential report for the Amazon Web Services account. For more information about the credential report, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html"&gt;Getting credential reports&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
| `credential_reports_Generate` | `EXEC` | `region` |  Generates a credential report for the Amazon Web Services account. For more information about the credential report, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html"&gt;Getting credential reports&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
