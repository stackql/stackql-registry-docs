---
title: customer_usage_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_usage_reports
  - admin
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_usage_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.admin.customer_usage_reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `usageReports` | `array` | Various application parameter records. |
| `warnings` | `array` | Warnings, if any. |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | The type of API resource. For a usage report, the value is `admin#reports#usageReports`. |
| `nextPageToken` | `string` | Token to specify next page. A report with multiple pages has a `nextPageToken` property in the response. For your follow-on requests getting all of the report's pages, enter the `nextPageToken` value in the `pageToken` query string. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `reports_customerUsageReports_get` | `SELECT` | `date` |
