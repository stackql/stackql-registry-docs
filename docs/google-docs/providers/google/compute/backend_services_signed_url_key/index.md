---
title: backend_services_signed_url_key
hide_title: false
hide_table_of_contents: false
keywords:
  - backend_services_signed_url_key
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backend_services_signed_url_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.backend_services_signed_url_key" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_signed_url_key" /> | `EXEC` | <CopyableCode code="backendService, project" /> | Adds a key for validating requests with signed URLs for this backend service. |
| <CopyableCode code="delete_signed_url_key" /> | `EXEC` | <CopyableCode code="backendService, keyName, project" /> | Deletes a key for validating requests with signed URLs for this backend service. |
