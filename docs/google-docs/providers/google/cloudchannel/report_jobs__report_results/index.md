---
title: report_jobs__report_results
hide_title: false
hide_table_of_contents: false
keywords:
  - report_jobs__report_results
  - cloudchannel
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
<tr><td><b>Name</b></td><td><code>report_jobs__report_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudchannel.report_jobs__report_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `rows` | `array` | The report's lists of values. Each row follows the settings and ordering of the columns from `report_metadata`. |
| `nextPageToken` | `string` | Pass this token to FetchReportResultsRequest.page_token to retrieve the next page of results. |
| `reportMetadata` | `object` | The features describing the data. Returned by CloudChannelReportsService.RunReportJob and CloudChannelReportsService.FetchReportResults. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `accounts_reportJobs_fetchReportResults` | `SELECT` | `accountsId, reportJobsId` |
