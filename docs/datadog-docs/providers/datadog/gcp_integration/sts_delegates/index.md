---
title: sts_delegates
hide_title: false
hide_table_of_contents: false
keywords:
  - sts_delegates
  - gcp_integration
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sts_delegates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.gcp_integration.sts_delegates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the delegate service account. |
| `attributes` | `object` | Your delegate account attributes. |
| `type` | `string` | The type of account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_gcpsts_delegate` | `SELECT` | `dd_site` | List your Datadog-GCP STS delegate account configured in your Datadog account. |
| `_get_gcpsts_delegate` | `EXEC` | `dd_site` | List your Datadog-GCP STS delegate account configured in your Datadog account. |
| `make_gcpsts_delegate` | `EXEC` | `dd_site` | Create a Datadog GCP principal. |
