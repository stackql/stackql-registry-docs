---
title: examples
hide_title: false
hide_table_of_contents: false
keywords:
  - examples
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
<tr><td><b>Name</b></td><td><code>examples</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="translate.examples" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the example, in form of `projects/&#123;project-number-or-id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/examples/&#123;example_id&#125;' |
| <CopyableCode code="sourceText" /> | `string` | Sentence in source language. |
| <CopyableCode code="targetText" /> | `string` | Sentence in target language. |
| <CopyableCode code="usage" /> | `string` | Output only. Usage of the sentence pair. Options are TRAIN\|VALIDATION\|TEST. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_datasets_examples_list" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> |
| <CopyableCode code="_projects_locations_datasets_examples_list" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> |
