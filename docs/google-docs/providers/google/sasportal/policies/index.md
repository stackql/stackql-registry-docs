---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - sasportal
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sasportal.policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `policies_get` | `EXEC` |  | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `policies_set` | `EXEC` |  | Sets the access control policy on the specified resource. Replaces any existing policy. |
| `policies_test` | `EXEC` |  | Returns permissions that a caller has on the specified resource. |
