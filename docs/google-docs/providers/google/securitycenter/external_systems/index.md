---
title: external_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - external_systems
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
<tr><td><b>Name</b></td><td><code>external_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="securitycenter.external_systems" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="folders_sources_findings_external_systems_patch" /> | `EXEC` | <CopyableCode code="externalSystemsId, findingsId, foldersId, sourcesId" /> |
| <CopyableCode code="organizations_sources_findings_external_systems_patch" /> | `EXEC` | <CopyableCode code="externalSystemsId, findingsId, organizationsId, sourcesId" /> |
| <CopyableCode code="projects_sources_findings_external_systems_patch" /> | `EXEC` | <CopyableCode code="externalSystemsId, findingsId, projectsId, sourcesId" /> |
