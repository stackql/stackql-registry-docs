---
title: terraform_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - terraform_versions
  - config
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
<tr><td><b>Name</b></td><td><code>terraform_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="config.terraform_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The version name is in the format: 'projects/&#123;project_id&#125;/locations/&#123;location&#125;/terraformVersions/&#123;terraform_version&#125;'. |
| <CopyableCode code="deprecateTime" /> | `string` | Output only. When the version is deprecated. |
| <CopyableCode code="obsoleteTime" /> | `string` | Output only. When the version is obsolete. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the version, ACTIVE, DEPRECATED or OBSOLETE. |
| <CopyableCode code="supportTime" /> | `string` | Output only. When the version is supported. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, terraformVersionsId" /> | Gets details about a TerraformVersion. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists TerraformVersions in a given project and location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists TerraformVersions in a given project and location. |
