---
title: sources_iam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sources_iam_policies
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>sources_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.sources_iam_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_sources_get_iam_policy` | `EXEC` | `organizationsId, sourcesId` | Gets the access control policy on the specified Source. |
| `organizations_sources_set_iam_policy` | `EXEC` | `organizationsId, sourcesId` | Sets the access control policy on the specified Source. |
| `organizations_sources_test_iam_permissions` | `EXEC` | `organizationsId, sourcesId` | Returns the permissions that a caller has on the specified source. |
