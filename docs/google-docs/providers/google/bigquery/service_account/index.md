---
title: service_account
hide_title: false
hide_table_of_contents: false
keywords:
  - service_account
  - bigquery
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
<tr><td><b>Name</b></td><td><code>service_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.service_account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `email` | `string` | The service account email address. |
| `kind` | `string` | The resource type of the response. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_service_account` | `SELECT` | `projectId` |
