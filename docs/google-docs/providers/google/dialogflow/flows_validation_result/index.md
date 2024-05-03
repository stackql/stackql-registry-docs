---
title: flows_validation_result
hide_title: false
hide_table_of_contents: false
keywords:
  - flows_validation_result
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
<tr><td><b>Name</b></td><td><code>flows_validation_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.flows_validation_result" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the flow validation result. Format: `projects//locations//agents//flows//validationResult`. |
| <CopyableCode code="updateTime" /> | `string` | Last time the flow was validated. |
| <CopyableCode code="validationMessages" /> | `array` | Contains all validation messages. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_agents_flows_get_validation_result" /> | `SELECT` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> |
