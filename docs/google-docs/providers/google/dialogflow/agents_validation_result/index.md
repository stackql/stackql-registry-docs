---
title: agents_validation_result
hide_title: false
hide_table_of_contents: false
keywords:
  - agents_validation_result
  - dialogflow
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
<tr><td><b>Name</b></td><td><code>agents_validation_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.agents_validation_result" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the agent validation result. Format: `projects//locations//agents//validationResult`. |
| <CopyableCode code="flowValidationResults" /> | `array` | Contains all flow validation results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_agents_get_validation_result" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> |
