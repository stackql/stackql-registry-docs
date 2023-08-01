---
title: data_exchanges_iam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - data_exchanges_iam_policies
  - analyticshub
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
<tr><td><b>Name</b></td><td><code>data_exchanges_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analyticshub.data_exchanges_iam_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_data_exchanges_get_iam_policy` | `EXEC` | `dataExchangesId, locationsId, projectsId` | Gets the IAM policy. |
| `projects_locations_data_exchanges_set_iam_policy` | `EXEC` | `dataExchangesId, locationsId, projectsId` | Sets the IAM policy. |
| `projects_locations_data_exchanges_test_iam_permissions` | `EXEC` | `dataExchangesId, locationsId, projectsId` | Returns the permissions that a caller has. |
