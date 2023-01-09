---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - doubleclickbidmanager
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.doubleclickbidmanager.reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metadata` | `object` | Report metadata. |
| `params` | `object` | Parameters of a query or report. |
| `key` | `object` | Key used to identify a report. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `queries_reports_get` | `SELECT` | `queryId, reportId` | Retrieves a report. |
| `queries_reports_list` | `SELECT` | `queryId` | Lists reports associated with a query. |
