---
title: environments_debugmask
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_debugmask
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
<tr><td><b>Name</b></td><td><code>environments_debugmask</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.environments_debugmask</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_get_debugmask` | `EXEC` | `environmentsId, organizationsId` | Gets the debug mask singleton resource for an environment. |
| `organizations_environments_update_debugmask` | `EXEC` | `environmentsId, organizationsId` | Updates the debug mask singleton resource for an environment. |
