---
title: assets_security_marks
hide_title: false
hide_table_of_contents: false
keywords:
  - assets_security_marks
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets_security_marks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.assets_security_marks" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="folders_assets_update_security_marks" /> | `EXEC` | <CopyableCode code="assetsId, foldersId" /> |
| <CopyableCode code="organizations_assets_update_security_marks" /> | `EXEC` | <CopyableCode code="assetsId, organizationsId" /> |
| <CopyableCode code="projects_assets_update_security_marks" /> | `EXEC` | <CopyableCode code="assetsId, projectsId" /> |
