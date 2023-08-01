---
title: findings_security_marks
hide_title: false
hide_table_of_contents: false
keywords:
  - findings_security_marks
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
<tr><td><b>Name</b></td><td><code>findings_security_marks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.findings_security_marks</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `folders_sources_findings_update_security_marks` | `EXEC` | `findingsId, foldersId, sourcesId` |
| `organizations_sources_findings_update_security_marks` | `EXEC` | `findingsId, organizationsId, sourcesId` |
| `projects_sources_findings_update_security_marks` | `EXEC` | `findingsId, projectsId, sourcesId` |
