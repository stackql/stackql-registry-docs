---
title: supported_languages
hide_title: false
hide_table_of_contents: false
keywords:
  - supported_languages
  - translate
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
<tr><td><b>Name</b></td><td><code>supported_languages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.supported_languages" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_get_supported_languages" /> | `SELECT` | <CopyableCode code="projectsId" /> |
| <CopyableCode code="projects_locations_get_supported_languages" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> |
