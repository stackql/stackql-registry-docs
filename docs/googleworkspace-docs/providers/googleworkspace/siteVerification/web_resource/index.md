---
title: web_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - web_resource
  - siteVerification
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
<tr><td><b>Name</b></td><td><code>web_resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.siteVerification.web_resource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The string used to identify this site. This value should be used in the "id" portion of the REST URL for the Get, Update, and Delete operations. |
| `owners` | `array` | The email addresses of all verified owners. |
| `site` | `object` | The address and type of a site that is verified or will be verified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `webResource_get` | `SELECT` | `id` | Get the most current data for a website or domain. |
| `webResource_list` | `SELECT` |  | Get the list of your verified websites and domains. |
| `webResource_delete` | `DELETE` | `id` | Relinquish ownership of a website or domain. |
| `webResource_insert` | `EXEC` | `verificationMethod` | Attempt verification of a website or domain. |
| `webResource_patch` | `EXEC` | `id` | Modify the list of owners for your website or domain. This method supports patch semantics. |
| `webResource_update` | `EXEC` | `id` | Modify the list of owners for your website or domain. |
